#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.sessions import (
    GetResponse,
    AuthenticateResponse,
    RevokeResponse,
    JwksResponse,
)


class Sessions:
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
        return "sessions"

    def get(
        self,
        user_id: str,
    ) -> GetResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        resp = self.sync_client.get(url, params=payload)
        return GetResponse.from_json(resp.json())

    async def get_async(
        self,
        user_id: str,
    ) -> GetResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        resp = await self.async_client.get(url, params=payload)
        return GetResponse.from_json(await resp.json())

    def authenticate(
        self,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {}

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
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {}

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

    # MANUAL(authenticate_jwt)
    def authenticate_jwt(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> None:
        # 1. Check if this method should be async or not
        # 2. Set the return type appropriately
        # 3. Fill out the method details
        # 4. Remember to write a test since this is manually generated
        raise NotImplementedError("Fill me out!")

    # ENDMANUAL(authenticate_jwt)

    # MANUAL(authenticate_jwt_local)
    def authenticate_jwt_local(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        leeway: int = 0,
    ) -> None:
        # 1. Check if this method should be async or not
        # 2. Set the return type appropriately
        # 3. Fill out the method details
        # 4. Remember to write a test since this is manually generated
        raise NotImplementedError("Fill me out!")

    # ENDMANUAL(authenticate_jwt_local)

    def revoke(
        self,
        session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> RevokeResponse:
        payload: Dict[str, Any] = {}

        if session_id is not None:
            payload["session_id"] = session_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "revoke")

        resp = self.sync_client.post(url, json=payload)
        return RevokeResponse.from_json(resp.json())

    async def revoke_async(
        self,
        session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> RevokeResponse:
        payload: Dict[str, Any] = {}

        if session_id is not None:
            payload["session_id"] = session_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "revoke")

        resp = await self.async_client.post(url, json=payload)
        return RevokeResponse.from_json(await resp.json())

    def jwks(
        self,
        project_id: str,
    ) -> JwksResponse:
        payload: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.route_with_sub_url(
            self.sub_url, "jwks/{}".format(project_id)
        )

        resp = self.sync_client.get(url, params=payload)
        return JwksResponse.from_json(resp.json())

    async def jwks_async(
        self,
        project_id: str,
    ) -> JwksResponse:
        payload: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.route_with_sub_url(
            self.sub_url, "jwks/{}".format(project_id)
        )

        resp = await self.async_client.get(url, params=payload)
        return JwksResponse.from_json(await resp.json())
