from typing import Optional

from stytch.b2b.api.rbac import RBAC
from stytch.b2b.models.rbac import Policy
from stytch.shared.lazy_cache import LazyCache

DEFAULT_REFRESH_INTERVAL = 10 * 60  # 10 minutes


class PolicyCache(LazyCache[Policy]):
    def __init__(
        self,
        rbac: RBAC,
        refresh_interval_seconds: int = DEFAULT_REFRESH_INTERVAL,
    ) -> None:
        self.rbac = rbac
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
