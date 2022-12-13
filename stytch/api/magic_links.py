#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.magic_links import (
    CreateResponse,
    AuthenticateResponse,
)


class MagicLinks:
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
        return "magic_links"

    def create(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
    ) -> CreateResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        resp = self.sync_client.post(url, json=payload)
        return CreateResponse.from_json(resp.json())

    async def create_async(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
    ) -> CreateResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        resp = await self.async_client.post(url, json=payload)
        return CreateResponse.from_json(await resp.json())

    def authenticate(
        self,
        token: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "token": token,
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
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        resp = self.sync_client.post(url, json=payload)
        return AuthenticateResponse.from_json(resp.json())

    async def authenticate_async(
        self,
        token: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "token": token,
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
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        resp = await self.async_client.post(url, json=payload)
        return AuthenticateResponse.from_json(await resp.json())
