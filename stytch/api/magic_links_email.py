#!/usr/bin/env python3

# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import Name
from stytch.models.magic_links_email import (
    InviteResponse,
    LoginOrCreateResponse,
    RevokeInviteResponse,
    SendResponse,
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
        return "magic_links/email"

    def send(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        code_challenge: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> SendResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "send")

        resp = self.sync_client.post(url, json=payload)
        return SendResponse.from_json(resp.json())

    async def send_async(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        code_challenge: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> SendResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "send")

        resp = await self.async_client.post(url, json=payload)
        return SendResponse.from_json(await resp.json())

    def login_or_create(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        create_user_as_pending: Optional[bool] = None,
        locale: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if create_user_as_pending is not None:
            payload["create_user_as_pending"] = create_user_as_pending
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "login_or_create")

        resp = self.sync_client.post(url, json=payload)
        return LoginOrCreateResponse.from_json(resp.json())

    async def login_or_create_async(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        create_user_as_pending: Optional[bool] = None,
        locale: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if create_user_as_pending is not None:
            payload["create_user_as_pending"] = create_user_as_pending
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "login_or_create")

        resp = await self.async_client.post(url, json=payload)
        return LoginOrCreateResponse.from_json(await resp.json())

    def invite(
        self,
        email: str,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        name: Optional[Name] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
    ) -> InviteResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if invite_magic_link_url is not None:
            payload["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if name is not None:
            payload["name"] = name
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes

        url = self.api_base.route_with_sub_url(self.sub_url, "invite")

        resp = self.sync_client.post(url, json=payload)
        return InviteResponse.from_json(resp.json())

    async def invite_async(
        self,
        email: str,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        name: Optional[Name] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
    ) -> InviteResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if invite_magic_link_url is not None:
            payload["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if name is not None:
            payload["name"] = name
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes

        url = self.api_base.route_with_sub_url(self.sub_url, "invite")

        resp = await self.async_client.post(url, json=payload)
        return InviteResponse.from_json(await resp.json())

    def revoke_invite(
        self,
        email: str,
    ) -> RevokeInviteResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "revoke_invite")

        resp = self.sync_client.post(url, json=payload)
        return RevokeInviteResponse.from_json(resp.json())

    async def revoke_invite_async(
        self,
        email: str,
    ) -> RevokeInviteResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "revoke_invite")

        resp = await self.async_client.post(url, json=payload)
        return RevokeInviteResponse.from_json(await resp.json())
