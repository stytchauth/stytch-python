# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from stytch.b2b.api.discovery_intermediate_sessions import IntermediateSessions
from stytch.b2b.api.discovery_organizations import Organizations
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Discovery:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.intermediate_sessions = IntermediateSessions(
            api_base=api_base,
            sync_client=sync_client,
            async_client=async_client,
        )
        self.organizations = Organizations(
            api_base=api_base,
            sync_client=sync_client,
            async_client=async_client,
        )
