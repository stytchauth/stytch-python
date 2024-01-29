# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict

from stytch.b2b.models.rbac import PolicyResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class RBAC:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def policy(
        self,
    ) -> PolicyResponse:
        """Get the active RBAC Policy for your current Stytch Project. An RBAC Policy is the canonical document that stores all defined Resources and Roles within your RBAC permissioning model.

        When using the backend SDKs, the RBAC Policy will be cached to allow for local evaluations, eliminating the need for an extra request to Stytch. The policy will be refreshed if an authorization check is requested and the RBAC policy was last updated more than 5 minutes ago.

        Resources and Roles can be created and managed within the [Dashboard](/dashboard/rbac). Additionally, [Role assignment](https://stytch.com/docs/b2b/guides/rbac/role-assignment) can be programmatically managed through certain Stytch API endpoints.

        Check out the [RBAC overview](https://stytch.com/docs/b2b/guides/rbac/overview) to learn more about Stytch's RBAC permissioning model.

        Fields:
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}

        url = self.api_base.url_for("/v1/b2b/rbac/policy", data)
        res = self.sync_client.get(url, data, headers)
        return PolicyResponse.from_json(res.response.status_code, res.json)

    async def policy_async(
        self,
    ) -> PolicyResponse:
        """Get the active RBAC Policy for your current Stytch Project. An RBAC Policy is the canonical document that stores all defined Resources and Roles within your RBAC permissioning model.

        When using the backend SDKs, the RBAC Policy will be cached to allow for local evaluations, eliminating the need for an extra request to Stytch. The policy will be refreshed if an authorization check is requested and the RBAC policy was last updated more than 5 minutes ago.

        Resources and Roles can be created and managed within the [Dashboard](/dashboard/rbac). Additionally, [Role assignment](https://stytch.com/docs/b2b/guides/rbac/role-assignment) can be programmatically managed through certain Stytch API endpoints.

        Check out the [RBAC overview](https://stytch.com/docs/b2b/guides/rbac/overview) to learn more about Stytch's RBAC permissioning model.

        Fields:
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}

        url = self.api_base.url_for("/v1/b2b/rbac/policy", data)
        res = await self.async_client.get(url, data, headers)
        return PolicyResponse.from_json(res.response.status, res.json)
