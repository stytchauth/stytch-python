#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.otp import (
    AuthenticateResponse,
)
from stytch.api.otp_email import Email
from stytch.api.otp_sms import SMS
from stytch.api.otp_whatsapp import Whatsapp


class OTP:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.otp_email = Email(api_base, sync_client, async_client)
        self.otp_sms = SMS(api_base, sync_client, async_client)
        self.otp_whatsapp = Whatsapp(api_base, sync_client, async_client)

    @property
    def sub_url(self) -> str:
        return "otps"

    def authenticate(
        self,
        method_id: str,
        code: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "method_id": method_id,
            "code": code,
        }

        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
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
        return AuthenticateResponse.from_json(resp.json())

    async def authenticate_async(
        self,
        method_id: str,
        code: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "method_id": method_id,
            "code": code,
        }

        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
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
        return AuthenticateResponse.from_json(await resp.json())
