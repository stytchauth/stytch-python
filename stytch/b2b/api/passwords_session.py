# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.passwords_session import ResetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Sessions:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def reset(
        self,
        organization_id: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the Member's password using their existing session. The endpoint will error if the session does not contain an authentication factor that has been issued within the last 5 minutes. Either `session_token` or `session_jwt` should be provided.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - password: The password to authenticate.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/b2b/passwords/session/reset", data)
        res = self.sync_client.post(url, data)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        organization_id: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the Member's password using their existing session. The endpoint will error if the session does not contain an authentication factor that has been issued within the last 5 minutes. Either `session_token` or `session_jwt` should be provided.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - password: The password to authenticate.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/b2b/passwords/session/reset", data)
        res = await self.async_client.post(url, data)
        return ResetResponse.from_json(res.response.status, res.json)
