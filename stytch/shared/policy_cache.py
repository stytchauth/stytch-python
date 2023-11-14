from stytch.b2b.models.rbac import RBAC, Policy
from stytch.shared.lazy_cache import LazyCache

DEFAULT_REFRESH_INTERVAL = 10 * 60  # 10 minutes


class PolicyCache(LazyCache[Policy]):
    def __init__(
        self,
        rbac: RBAC,
        refresh_interval_seconds: int = DEFAULT_REFRESH_INTERVAL,
    ) -> None:
        super().__init__(
            reload_func=rbac.policy,
            async_reload_func=rbac.policy_async,
            refresh_interval_seconds=refresh_interval_seconds,
        )
