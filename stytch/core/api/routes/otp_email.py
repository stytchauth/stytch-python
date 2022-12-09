#!/usr/bin/env python3

from typing import Any, Dict, Optional

import requests
import aiohttp

from stytch.core.api.base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


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
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "email": email,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes
        if locale is not None:
            data["locale"] = locale
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "email/send")

        return self.sync_client.post(url, data=data)

    async def send_async(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        locale: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "email": email,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes
        if locale is not None:
            data["locale"] = locale
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "email/send")

        return await self.async_client.post(url, data=data)

    def login_or_create(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool = False,
        locale: Optional[str] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "email/login_or_create")

        return self.sync_client.post(url, data=data)

    async def login_or_create_async(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool = False,
        locale: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "email/login_or_create")

        return await self.async_client.post(url, data=data)
