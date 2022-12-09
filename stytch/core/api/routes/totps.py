#!/usr/bin/env python3

from typing import Any, Dict, Optional

import requests
import aiohttp

from stytch.core.api.base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class TOTPs:
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
        return "totps"

    def create(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        return self.sync_client.post(url, data=data)

    async def create_async(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        return await self.async_client.post(url, data=data)

    def authenticate(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "totp_code": totp_code,
        }

        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        return self.sync_client.post(url, data=data)

    async def authenticate_async(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "totp_code": totp_code,
        }

        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        return await self.async_client.post(url, data=data)

    def recovery_codes(
        self,
        user_id: str,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "recovery_codes")

        return self.sync_client.post(url, data=data)

    async def recovery_codes_async(
        self,
        user_id: str,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "recovery_codes")

        return await self.async_client.post(url, data=data)

    def recover(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "recovery_code": recovery_code,
        }

        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "recover")

        return self.sync_client.post(url, data=data)

    async def recover_async(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "recovery_code": recovery_code,
        }

        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "recover")

        return await self.async_client.post(url, data=data)
