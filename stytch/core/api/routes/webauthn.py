#!/usr/bin/env python3

from typing import Any, Dict, Optional

import requests
import aiohttp

from stytch.core.api.base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class WebAuthn:
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
        return "webauthn"

    def register_start(
        self,
        user_id: str,
        domain: str,
        user_agent: Optional[str] = None,
        authenticator_type: Optional[str] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        if user_agent is not None:
            data["user_agent"] = user_agent
        if authenticator_type is not None:
            data["authenticator_type"] = authenticator_type

        url = self.api_base.route_with_sub_url(self.sub_url, "register/start")

        return self.sync_client.post(url, data=data)

    async def register_start_async(
        self,
        user_id: str,
        domain: str,
        user_agent: Optional[str] = None,
        authenticator_type: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        if user_agent is not None:
            data["user_agent"] = user_agent
        if authenticator_type is not None:
            data["authenticator_type"] = authenticator_type

        url = self.api_base.route_with_sub_url(self.sub_url, "register/start")

        return await self.async_client.post(url, data=data)

    def register(
        self,
        user_id: str,
        public_key_credential: str,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "register")

        return self.sync_client.post(url, data=data)

    async def register_async(
        self,
        user_id: str,
        public_key_credential: str,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "register")

        return await self.async_client.post(url, data=data)

    def authenticate_start(
        self,
        user_id: str,
        domain: str,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        return self.sync_client.post(url, data=data)

    async def authenticate_start_async(
        self,
        user_id: str,
        domain: str,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        return await self.async_client.post(url, data=data)

    def authenticate(
        self,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "public_key_credential": public_key_credential,
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
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "public_key_credential": public_key_credential,
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
