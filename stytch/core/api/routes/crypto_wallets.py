#!/usr/bin/env python3

from typing import Any, Dict, Optional

import requests
import aiohttp

from stytch.core.api.base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


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
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
        }

        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        return self.sync_client.post(url, data=data)

    async def authenticate_start_async(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
        }

        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate/start")

        return await self.async_client.post(url, data=data)

    def authenticate(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        signature: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
            "signature": signature,
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

        return self.sync_client.post(url, data=data)

    async def authenticate_async(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        signature: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> aiohttp.ClientResponse:
        data: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
            "signature": signature,
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

        return await self.async_client.post(url, data=data)
