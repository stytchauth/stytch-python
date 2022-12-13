#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.otp_email import (
    SendResponse,
    LoginOrCreateResponse,
)


class Email:
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
        return "otps"

    def send(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        locale: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> SendResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "email/send")

        resp = self.sync_client.post(url, json=payload)
        return SendResponse.from_json(resp.json())

    async def send_async(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        locale: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> SendResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "email/send")

        resp = await self.async_client.post(url, json=payload)
        return SendResponse.from_json(await resp.json())

    def login_or_create(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool = False,
        locale: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        payload: Dict[str, Any] = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "email/login_or_create")

        resp = self.sync_client.post(url, json=payload)
        return LoginOrCreateResponse.from_json(resp.json())

    async def login_or_create_async(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool = False,
        locale: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        payload: Dict[str, Any] = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "email/login_or_create")

        resp = await self.async_client.post(url, json=payload)
        return LoginOrCreateResponse.from_json(await resp.json())
