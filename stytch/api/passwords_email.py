#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.passwords_email import (
    ResetStartResponse,
    ResetResponse,
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
        return "passwords"

    def reset_start(
        self,
        email: str,
        login_redirect_url: Optional[str] = None,
        reset_password_redirect_url: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        code_challenge: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> ResetStartResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_redirect_url is not None:
            payload["login_redirect_url"] = login_redirect_url
        if reset_password_redirect_url is not None:
            payload["reset_password_redirect_url"] = reset_password_redirect_url
        if reset_password_expiration_minutes is not None:
            payload[
                "reset_password_expiration_minutes"
            ] = reset_password_expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "reset/start")

        resp = self.sync_client.post(url, json=payload)
        return ResetStartResponse(**resp.json())

    async def reset_start_async(
        self,
        email: str,
        login_redirect_url: Optional[str] = None,
        reset_password_redirect_url: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        code_challenge: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> ResetStartResponse:
        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_redirect_url is not None:
            payload["login_redirect_url"] = login_redirect_url
        if reset_password_redirect_url is not None:
            payload["reset_password_redirect_url"] = reset_password_redirect_url
        if reset_password_expiration_minutes is not None:
            payload[
                "reset_password_expiration_minutes"
            ] = reset_password_expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "reset/start")

        resp = await self.async_client.post(url, json=payload)
        return ResetStartResponse(**await resp.json())

    def reset(
        self,
        token: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        code_verifier: Optional[str] = None,
    ) -> ResetResponse:
        payload: Dict[str, Any] = {
            "token": token,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        resp = self.sync_client.post(url, json=payload)
        return ResetResponse(**resp.json())

    async def reset_async(
        self,
        token: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        code_verifier: Optional[str] = None,
    ) -> ResetResponse:
        payload: Dict[str, Any] = {
            "token": token,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        resp = await self.async_client.post(url, json=payload)
        return ResetResponse(**await resp.json())
