#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.passwords_session import (
    ResetResponse,
)


class Session:
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
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        data: Dict[str, Any] = {
            "password": password,
        }

        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        resp = self.sync_client.post(url, data=data)
        return ResetResponse(**resp.json())

    async def reset_async(
        self,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        data: Dict[str, Any] = {
            "password": password,
        }

        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        resp = await self.async_client.post(url, data=data)
        return ResetResponse(**await resp.json())
