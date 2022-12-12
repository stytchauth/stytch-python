#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.totps import (
    CreateResponse,
    AuthenticateResponse,
    RecoveryCodesResponse,
    RecoverResponse,
)


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
    ) -> CreateResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        resp = self.sync_client.post(url, data=data)
        return CreateResponse(**resp.json())

    async def create_async(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ) -> CreateResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        resp = await self.async_client.post(url, data=data)
        return CreateResponse(**await resp.json())

    def authenticate(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
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

        resp = self.sync_client.post(url, data=data)
        return AuthenticateResponse(**resp.json())

    async def authenticate_async(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
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

        resp = await self.async_client.post(url, data=data)
        return AuthenticateResponse(**await resp.json())

    def recovery_codes(
        self,
        user_id: str,
    ) -> RecoveryCodesResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "recovery_codes")

        resp = self.sync_client.post(url, data=data)
        return RecoveryCodesResponse(**resp.json())

    async def recovery_codes_async(
        self,
        user_id: str,
    ) -> RecoveryCodesResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "recovery_codes")

        resp = await self.async_client.post(url, data=data)
        return RecoveryCodesResponse(**await resp.json())

    def recover(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> RecoverResponse:
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

        resp = self.sync_client.post(url, data=data)
        return RecoverResponse(**resp.json())

    async def recover_async(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> RecoverResponse:
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

        resp = await self.async_client.post(url, data=data)
        return RecoverResponse(**await resp.json())
