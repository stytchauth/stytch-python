#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.passwords_existing_password import (
    ResetResponse,
)


class ExistingPassword:
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
        return "passwords"

    def reset(
        self,
        email: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        payload: Dict[str, Any] = {
            "email": email,
            "existing_password": existing_password,
            "new_password": new_password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        resp = self.sync_client.post(url, json=payload)
        return ResetResponse.from_json(resp.json())

    async def reset_async(
        self,
        email: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        payload: Dict[str, Any] = {
            "email": email,
            "existing_password": existing_password,
            "new_password": new_password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        resp = await self.async_client.post(url, json=payload)
        return ResetResponse.from_json(await resp.json())
