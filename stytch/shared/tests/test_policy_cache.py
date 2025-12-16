import time
import unittest
from typing import Dict, Optional

from stytch.b2b.models.rbac import (
    OrgPolicy,
    Policy,
    PolicyResource,
    PolicyRole,
    PolicyRolePermission,
    PolicyScope,
    PolicyResponse,
)
from stytch.b2b.models.rbac_organizations import GetOrgPolicyResponse
from stytch.shared.policy_cache import PolicyCache, _merge_policies


class FakeOrganizations:
    def __init__(self, org_policies: Dict[str, Optional[OrgPolicy]]):
        self.org_policies = org_policies
        self.call_count = 0

    def get_org_policy(self, organization_id: str) -> GetOrgPolicyResponse:
        self.call_count += 1
        return GetOrgPolicyResponse(
            status_code=200,
            request_id="test",
            org_policy=self.org_policies.get(organization_id),
        )

    async def get_org_policy_async(self, organization_id: str) -> GetOrgPolicyResponse:
        return self.get_org_policy(organization_id)


class FakeRBAC:
    def __init__(
        self, project_policy: Policy, org_policies: Dict[str, Optional[OrgPolicy]]
    ):
        self._project_policy = project_policy
        self.organizations = FakeOrganizations(org_policies)

    def policy(self) -> PolicyResponse:
        return PolicyResponse(
            status_code=200, request_id="test", policy=self._project_policy
        )

    async def policy_async(self) -> PolicyResponse:
        return self.policy()


class TestMergePolicies(unittest.TestCase):
    def test_none_org_policy_returns_project_policy(self) -> None:
        project_policy = Policy(
            roles=[
                PolicyRole(
                    role_id="admin",
                    description="Admin",
                    permissions=[PolicyRolePermission(actions=["*"], resource_id="r")],
                )
            ],
            resources=[],
            scopes=[],
        )

        result = _merge_policies(project_policy, None)

        self.assertIs(result, project_policy)

    def test_combines_roles_from_both_policies(self) -> None:
        project_policy = Policy(
            roles=[
                PolicyRole(
                    role_id="project_role",
                    description="Project role",
                    permissions=[
                        PolicyRolePermission(actions=["read"], resource_id="resource")
                    ],
                )
            ],
            resources=[
                PolicyResource(
                    resource_id="resource",
                    description="Resource",
                    actions=["read", "write"],
                )
            ],
            scopes=[PolicyScope(scope="read:all", description="Read all", permissions=[])],
        )
        org_policy = OrgPolicy(
            roles=[
                PolicyRole(
                    role_id="org_role",
                    description="Org role",
                    permissions=[
                        PolicyRolePermission(actions=["write"], resource_id="resource")
                    ],
                )
            ]
        )

        result = _merge_policies(project_policy, org_policy)

        self.assertEqual(len(result.roles), 2)
        role_ids = [role.role_id for role in result.roles]
        self.assertIn("project_role", role_ids)
        self.assertIn("org_role", role_ids)
        # Resources and scopes come from the project policy only
        self.assertEqual(result.resources, project_policy.resources)
        self.assertEqual(result.scopes, project_policy.scopes)


class TestPolicyCacheOrgPolicy(unittest.TestCase):
    def setUp(self) -> None:
        self.project_policy = Policy(
            roles=[
                PolicyRole(
                    role_id="project_role",
                    description="Project role",
                    permissions=[
                        PolicyRolePermission(actions=["read"], resource_id="resource"),
                    ],
                )
            ],
            resources=[],
            scopes=[],
        )
        self.org_policy = OrgPolicy(
            roles=[
                PolicyRole(
                    role_id="org_role",
                    description="Org role",
                    permissions=[
                        PolicyRolePermission(actions=["write"], resource_id="resource"),
                    ],
                )
            ]
        )

    def test_get_with_org_returns_merged_policy(self) -> None:
        rbac = FakeRBAC(self.project_policy, {"org-123": self.org_policy})
        cache = PolicyCache(rbac, refresh_interval_seconds=600)  # type: ignore[arg-type]

        result = cache.get_with_org("org-123")

        self.assertEqual(len(result.roles), 2)
        role_ids = [role.role_id for role in result.roles]
        self.assertIn("project_role", role_ids)
        self.assertIn("org_role", role_ids)

    def test_org_policy_is_cached(self) -> None:
        rbac = FakeRBAC(self.project_policy, {"org-123": self.org_policy})
        cache = PolicyCache(rbac, refresh_interval_seconds=600)  # type: ignore[arg-type]

        cache.get_with_org("org-123")
        cache.get_with_org("org-123")

        self.assertEqual(rbac.organizations.call_count, 1)

    def test_correct_org_policy_with_multiple_cached(self) -> None:
        org_123_policy = OrgPolicy(
            roles=[
                PolicyRole(
                    role_id="org_123_role",
                    description="Org 123 role",
                    permissions=[
                        PolicyRolePermission(actions=["read"], resource_id="resource")
                    ],
                )
            ]
        )
        org_456_policy = OrgPolicy(
            roles=[
                PolicyRole(
                    role_id="org_456_role",
                    description="Org 456 role",
                    permissions=[
                        PolicyRolePermission(actions=["write"], resource_id="resource")
                    ],
                )
            ]
        )
        rbac = FakeRBAC(
            self.project_policy, {"org-123": org_123_policy, "org-456": org_456_policy}
        )
        cache = PolicyCache(rbac, refresh_interval_seconds=600)  # type: ignore[arg-type]

        result_123 = cache.get_with_org("org-123")
        result_456 = cache.get_with_org("org-456")

        self.assertIn("org_123_role", [r.role_id for r in result_123.roles])
        self.assertNotIn("org_456_role", [r.role_id for r in result_123.roles])
        self.assertIn("org_456_role", [r.role_id for r in result_456.roles])
        self.assertNotIn("org_123_role", [r.role_id for r in result_456.roles])

    def test_none_org_policy_is_cached(self) -> None:
        rbac = FakeRBAC(self.project_policy, {})
        cache = PolicyCache(rbac, refresh_interval_seconds=600)  # type: ignore[arg-type]

        cache.get_with_org("org-no-policy")
        cache.get_with_org("org-no-policy")
        cache.get_with_org("org-no-policy")

        self.assertEqual(rbac.organizations.call_count, 1)

    def test_cache_respects_refresh_interval(self) -> None:
        rbac = FakeRBAC(self.project_policy, {"org-123": self.org_policy})
        cache = PolicyCache(rbac, refresh_interval_seconds=1)  # type: ignore[arg-type]

        cache.get_with_org("org-123")
        self.assertEqual(rbac.organizations.call_count, 1)

        cache.get_with_org("org-123")
        self.assertEqual(rbac.organizations.call_count, 1)

        time.sleep(1.1)

        cache.get_with_org("org-123")
        self.assertEqual(rbac.organizations.call_count, 2)
