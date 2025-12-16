import time
from typing import Dict, Optional

from stytch.b2b.api.rbac import RBAC
from stytch.b2b.models.rbac import OrgPolicy, Policy
from stytch.shared.lazy_cache import LazyCache

DEFAULT_REFRESH_INTERVAL = 10 * 60  # 10 minutes


def _merge_policies(project_policy: Policy, org_policy: Optional[OrgPolicy]) -> Policy:
    """Merge project-level and organization-level policies.

    Organization policies supplement the project policy by adding additional roles.
    The merged policy combines roles from both, with org roles added to project roles.
    Resources and scopes come only from the project policy.
    """
    if org_policy is None:
        return project_policy

    return Policy(
        roles=list(project_policy.roles) + list(org_policy.roles),
        resources=project_policy.resources,
        scopes=project_policy.scopes,
    )


class _OrgPolicyCacheEntry:
    def __init__(self, org_policy: Optional[OrgPolicy], last_refresh_time: float):
        self.org_policy = org_policy
        self.last_refresh_time = last_refresh_time


class PolicyCache(LazyCache[Policy]):
    def __init__(
        self,
        rbac: RBAC,
        refresh_interval_seconds: int = DEFAULT_REFRESH_INTERVAL,
    ) -> None:
        self.rbac = rbac
        self.refresh_interval_seconds = refresh_interval_seconds
        self._org_cache: Dict[str, _OrgPolicyCacheEntry] = {}
        super().__init__(
            reload_func=self.reload_policy,
            async_reload_func=self.reload_policy_async,
            refresh_interval_seconds=refresh_interval_seconds,
        )

    def reload_policy(self, _: Optional[Policy]) -> Policy:
        resp = self.rbac.policy()
        assert resp.policy is not None
        return resp.policy

    async def reload_policy_async(self, _: Optional[Policy]) -> Policy:
        resp = await self.rbac.policy_async()
        assert resp.policy is not None
        return resp.policy

    def _org_needs_refresh(self, organization_id: str) -> bool:
        if organization_id not in self._org_cache:
            return True
        entry = self._org_cache[organization_id]
        return time.time() - entry.last_refresh_time > self.refresh_interval_seconds

    def _get_org_policy(self, organization_id: str) -> Optional[OrgPolicy]:
        """Get the organization policy, fetching and caching if needed."""
        if self._org_needs_refresh(organization_id):
            resp = self.rbac.organizations.get_org_policy(organization_id)
            self._org_cache[organization_id] = _OrgPolicyCacheEntry(
                org_policy=resp.org_policy,
                last_refresh_time=time.time(),
            )
        return self._org_cache[organization_id].org_policy

    async def _get_org_policy_async(self, organization_id: str) -> Optional[OrgPolicy]:
        """Get the organization policy, fetching and caching if needed (async)."""
        if self._org_needs_refresh(organization_id):
            resp = await self.rbac.organizations.get_org_policy_async(organization_id)
            self._org_cache[organization_id] = _OrgPolicyCacheEntry(
                org_policy=resp.org_policy,
                last_refresh_time=time.time(),
            )
        return self._org_cache[organization_id].org_policy

    def get_with_org(self, organization_id: str) -> Policy:
        """Get the project policy merged with the organization policy.

        This fetches both the project-level RBAC policy and the organization-specific
        policy, merging the org roles into the project policy for authorization checks.
        """
        project_policy = self.get()
        org_policy = self._get_org_policy(organization_id)
        return _merge_policies(project_policy, org_policy)

    async def get_with_org_async(self, organization_id: str) -> Policy:
        """Get the project policy merged with the organization policy (async).

        This fetches both the project-level RBAC policy and the organization-specific
        policy, merging the org roles into the project policy for authorization checks.
        """
        project_policy = await self.get_async()
        org_policy = await self._get_org_policy_async(organization_id)
        return _merge_policies(project_policy, org_policy)
