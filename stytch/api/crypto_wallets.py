#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.crypto_wallets import (
    AuthenticateStartResponse,
    AuthenticateResponse,
)


class CryptoWallets:
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
        return "crypto_wallets"

    def authenticate_start(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> AuthenticateStartResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
        }

        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        resp = self.sync_client.post(url, json=payload)
        return AuthenticateStartResponse.from_json(resp.json())

    async def authenticate_start_async(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> AuthenticateStartResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
        }

        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        resp = await self.async_client.post(url, json=payload)
        return AuthenticateStartResponse.from_json(await resp.json())

    def authenticate(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        signature: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
            "signature": signature,
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
        return AuthenticateResponse.from_json(resp.json())

    async def authenticate_async(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        signature: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
            "signature": signature,
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
        return AuthenticateResponse.from_json(await resp.json())
