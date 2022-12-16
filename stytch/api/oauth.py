# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.oauth import AttachResponse, AuthenticateResponse


class OAuth:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "oauth"

    def authenticate(
        self,
        token: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "token": token,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        resp = self.sync_client.post(url, json=payload)
        json = {}
        try:
            json = resp.json()
        except Exception:
            pass
        return AuthenticateResponse.from_json(resp.status_code, json)

    async def authenticate_async(
        self,
        token: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "token": token,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        resp = await self.async_client.post(url, json=payload)
        json = {}
        try:
            json = await resp.json()
        except Exception:
            pass
        return AuthenticateResponse.from_json(resp.status, json)

    def attach(
        self,
        provider: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> AttachResponse:
        payload: Dict[str, Any] = {
            "provider": provider,
        }

        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "attach")

        resp = self.sync_client.post(url, json=payload)
        json = {}
        try:
            json = resp.json()
        except Exception:
            pass
        return AttachResponse.from_json(resp.status_code, json)

    async def attach_async(
        self,
        provider: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> AttachResponse:
        payload: Dict[str, Any] = {
            "provider": provider,
        }

        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "attach")

        resp = await self.async_client.post(url, json=payload)
        json = {}
        try:
            json = await resp.json()
        except Exception:
            pass
        return AttachResponse.from_json(resp.status, json)
