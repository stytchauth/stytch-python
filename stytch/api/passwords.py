#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.passwords import (
    CreateResponse,
    AuthenticateResponse,
    StrengthCheckResponse,
    MigrateResponse,
)
from stytch.api.passwords_email import Email
from stytch.api.passwords_existing_password import ExistingPassword
from stytch.api.passwords_session import Session


class Passwords:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.passwords_email = Email(api_base, sync_client, async_client)
        self.passwords_existing_password = ExistingPassword(
            api_base, sync_client, async_client
        )
        self.passwords_session = Session(api_base, sync_client, async_client)

    @property
    def sub_url(self) -> str:
        return "passwords"

    def create(
        self,
        email: str,
        password: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        data: Dict[str, Any] = {
            "email": email,
            "password": password,
        }

        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        resp = self.sync_client.post(url, data=data)
        return CreateResponse(**resp.json())

    async def create_async(
        self,
        email: str,
        password: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        data: Dict[str, Any] = {
            "email": email,
            "password": password,
        }

        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        resp = await self.async_client.post(url, data=data)
        return CreateResponse(**await resp.json())

    def authenticate(
        self,
        email: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        data: Dict[str, Any] = {
            "email": email,
            "password": password,
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
        email: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        data: Dict[str, Any] = {
            "email": email,
            "password": password,
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

    def strength_check(
        self,
        password: str,
        email: Optional[str] = None,
    ) -> StrengthCheckResponse:
        data: Dict[str, Any] = {
            "password": password,
        }

        if email is not None:
            data["email"] = email

        url = self.api_base.route_with_sub_url(self.sub_url, "strength_check")

        resp = self.sync_client.post(url, data=data)
        return StrengthCheckResponse(**resp.json())

    async def strength_check_async(
        self,
        password: str,
        email: Optional[str] = None,
    ) -> StrengthCheckResponse:
        data: Dict[str, Any] = {
            "password": password,
        }

        if email is not None:
            data["email"] = email

        url = self.api_base.route_with_sub_url(self.sub_url, "strength_check")

        resp = await self.async_client.post(url, data=data)
        return StrengthCheckResponse(**await resp.json())

    def migrate(
        self,
        email: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        data: Dict[str, Any] = {
            "email": email,
            "hash": hash,
            "hash_type": hash_type,
        }

        if md_5_config is not None:
            data["md_5_config"] = md_5_config
        if argon_2_config is not None:
            data["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            data["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            data["scrypt_config"] = scrypt_config

        url = self.api_base.route_with_sub_url(self.sub_url, "migrate")

        resp = self.sync_client.post(url, data=data)
        return MigrateResponse(**resp.json())

    async def migrate_async(
        self,
        email: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        data: Dict[str, Any] = {
            "email": email,
            "hash": hash,
            "hash_type": hash_type,
        }

        if md_5_config is not None:
            data["md_5_config"] = md_5_config
        if argon_2_config is not None:
            data["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            data["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            data["scrypt_config"] = scrypt_config

        url = self.api_base.route_with_sub_url(self.sub_url, "migrate")

        resp = await self.async_client.post(url, data=data)
        return MigrateResponse(**await resp.json())
