#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.webauthn import (
    RegisterStartResponse,
    RegisterResponse,
    AuthenticateStartResponse,
    AuthenticateResponse,
)


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
    ) -> RegisterStartResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        if user_agent is not None:
            payload["user_agent"] = user_agent
        if authenticator_type is not None:
            payload["authenticator_type"] = authenticator_type

        url = self.api_base.route_with_sub_url(self.sub_url, "register/start")

        resp = self.sync_client.post(url, json=payload)
        return RegisterStartResponse(**resp.json())

    async def register_start_async(
        self,
        user_id: str,
        domain: str,
        user_agent: Optional[str] = None,
        authenticator_type: Optional[str] = None,
    ) -> RegisterStartResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        if user_agent is not None:
            payload["user_agent"] = user_agent
        if authenticator_type is not None:
            payload["authenticator_type"] = authenticator_type

        url = self.api_base.route_with_sub_url(self.sub_url, "register/start")

        resp = await self.async_client.post(url, json=payload)
        return RegisterStartResponse(**await resp.json())

    def register(
        self,
        user_id: str,
        public_key_credential: str,
    ) -> RegisterResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "register")

        resp = self.sync_client.post(url, json=payload)
        return RegisterResponse(**resp.json())

    async def register_async(
        self,
        user_id: str,
        public_key_credential: str,
    ) -> RegisterResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "register")

        resp = await self.async_client.post(url, json=payload)
        return RegisterResponse(**await resp.json())

    def authenticate_start(
        self,
        user_id: str,
        domain: str,
    ) -> AuthenticateStartResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        resp = self.sync_client.post(url, json=payload)
        return AuthenticateStartResponse(**resp.json())

    async def authenticate_start_async(
        self,
        user_id: str,
        domain: str,
    ) -> AuthenticateStartResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        resp = await self.async_client.post(url, json=payload)
        return AuthenticateStartResponse(**await resp.json())

    def authenticate(
        self,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "public_key_credential": public_key_credential,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        resp = self.sync_client.post(url, json=payload)
        return AuthenticateResponse(**resp.json())

    async def authenticate_async(
        self,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "public_key_credential": public_key_credential,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        resp = await self.async_client.post(url, json=payload)
        return AuthenticateResponse(**await resp.json())
