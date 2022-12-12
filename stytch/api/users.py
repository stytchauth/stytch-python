#!/usr/bin/env python3

from typing import Any, Dict, List, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.users import (
    CreateResponse,
    GetResponse,
    GetPendingResponse,
    SearchResponse,
    DeleteResponse,
    UpdateResponse,
    DeleteEmailResponse,
    DeletePhoneNumberResponse,
    DeleteWebauthnRegistrationResponse,
    DeleteTotpResponse,
    DeleteCryptoWalletResponse,
    DeletePasswordResponse,
    DeleteBiometricRegistrationResponse,
    DeleteOauthUserRegistrationResponse,
)
import dataclasses
from stytch.models.common import Name, SearchQuery


class Users:
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
        return "users"

    def create(
        self,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        name: Optional[Name] = None,
        create_user_as_pending: bool = False,
        attributes: Optional[Dict[str, str]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        data: Dict[str, Any] = {
            "create_user_as_pending": create_user_as_pending,
        }

        if email is not None:
            data["email"] = email
        if phone_number is not None:
            data["phone_number"] = phone_number
        if name is not None:
            data["name"] = dataclasses.asdict(name)
        if attributes is not None:
            data["attributes"] = attributes
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        resp = self.sync_client.post(url, data=data)
        return CreateResponse(**resp.json())

    async def create_async(
        self,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        name: Optional[Name] = None,
        create_user_as_pending: bool = False,
        attributes: Optional[Dict[str, str]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        data: Dict[str, Any] = {
            "create_user_as_pending": create_user_as_pending,
        }

        if email is not None:
            data["email"] = email
        if phone_number is not None:
            data["phone_number"] = phone_number
        if name is not None:
            data["name"] = name
        if attributes is not None:
            data["attributes"] = attributes
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "/")

        resp = await self.async_client.post(url, data=data)
        return CreateResponse(**await resp.json())

    def get(
        self,
        user_id: str,
    ) -> GetResponse:
        params: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, user_id)

        resp = self.sync_client.get(url, params=params)
        return GetResponse(**resp.json())

    async def get_async(
        self,
        user_id: str,
    ) -> GetResponse:
        params: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, user_id)

        resp = await self.async_client.get(url, params=params)
        return GetResponse(**await resp.json())

    def get_pending(
        self,
        limit: Optional[int] = None,
        starting_after_id: Optional[str] = None,
    ) -> GetPendingResponse:
        params: Dict[str, Any] = {}

        if limit is not None:
            params["limit"] = limit
        if starting_after_id is not None:
            params["starting_after_id"] = starting_after_id

        url = self.api_base.route_with_sub_url(self.sub_url, "pending")

        resp = self.sync_client.get(url, params=params)
        return GetPendingResponse(**resp.json())

    async def get_pending_async(
        self,
        limit: Optional[int] = None,
        starting_after_id: Optional[str] = None,
    ) -> GetPendingResponse:
        params: Dict[str, Any] = {}

        if limit is not None:
            params["limit"] = limit
        if starting_after_id is not None:
            params["starting_after_id"] = starting_after_id

        url = self.api_base.route_with_sub_url(self.sub_url, "pending")

        resp = await self.async_client.get(url, params=params)
        return GetPendingResponse(**await resp.json())

    def search(
        self,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        query: Optional[SearchQuery] = None,
    ) -> SearchResponse:
        data: Dict[str, Any] = {}

        if limit is not None:
            data["limit"] = limit
        if cursor is not None:
            data["cursor"] = cursor
        if query is not None:
            data["query"] = dataclasses.asdict(query)

        url = self.api_base.route_with_sub_url(self.sub_url, "search")

        resp = self.sync_client.post(url, data=data)
        return SearchResponse(**resp.json())

    async def search_async(
        self,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        query: Optional[SearchQuery] = None,
    ) -> SearchResponse:
        data: Dict[str, Any] = {}

        if limit is not None:
            data["limit"] = limit
        if cursor is not None:
            data["cursor"] = cursor
        if query is not None:
            data["query"] = query

        url = self.api_base.route_with_sub_url(self.sub_url, "search")

        resp = await self.async_client.post(url, data=data)
        return SearchResponse(**await resp.json())

    # MANUAL(search_all)
    def search_all(
        self,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        query: Optional[SearchQuery] = None,
    ) -> None:
        # 1. Check if this method should be async or not
        # 2. Set the return type appropriately
        # 3. Fill out the method details
        # 4. Remember to write a test since this is manually generated
        raise NotImplementedError("Fill me out!")

    # ENDMANUAL(search_all)

    def delete(
        self,
        user_id: str,
    ) -> DeleteResponse:

        url = self.api_base.route_with_sub_url(self.sub_url, user_id)

        resp = self.sync_client.delete(url)

    async def delete_async(
        self,
        user_id: str,
    ) -> DeleteResponse:

        url = self.api_base.route_with_sub_url(self.sub_url, user_id)

        resp = await self.async_client.delete(url)

    def update(
        self,
        user_id: str,
        emails: Optional[List[str]] = None,
        phone_numbers: Optional[List[str]] = None,
        crypto_wallets: Optional[List[str]] = None,
        name: Optional[Name] = None,
        attributes: Optional[Dict[str, str]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        if emails is not None:
            data["emails"] = emails
        if phone_numbers is not None:
            data["phone_numbers"] = phone_numbers
        if crypto_wallets is not None:
            data["crypto_wallets"] = crypto_wallets
        if name is not None:
            data["name"] = dataclasses.asdict(name)
        if attributes is not None:
            data["attributes"] = attributes
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, user_id)

        resp = self.sync_client.put(url, data=data)
        return UpdateResponse(**resp.json())

    async def update_async(
        self,
        user_id: str,
        emails: Optional[List[str]] = None,
        phone_numbers: Optional[List[str]] = None,
        crypto_wallets: Optional[List[str]] = None,
        name: Optional[Name] = None,
        attributes: Optional[Dict[str, str]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateResponse:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        if emails is not None:
            data["emails"] = emails
        if phone_numbers is not None:
            data["phone_numbers"] = phone_numbers
        if crypto_wallets is not None:
            data["crypto_wallets"] = crypto_wallets
        if name is not None:
            data["name"] = name
        if attributes is not None:
            data["attributes"] = attributes
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, user_id)

        resp = await self.async_client.put(url, data=data)
        return UpdateResponse(**await resp.json())

    def delete_email(
        self,
        email_id: str,
    ) -> DeleteEmailResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "emails/{}".format(email_id)
        )

        resp = self.sync_client.delete(url)

    async def delete_email_async(
        self,
        email_id: str,
    ) -> DeleteEmailResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "emails/{}".format(email_id)
        )

        resp = await self.async_client.delete(url)

    def delete_phone_number(
        self,
        phone_id: str,
    ) -> DeletePhoneNumberResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "phone_numbers/{}".format(phone_id)
        )

        resp = self.sync_client.delete(url)

    async def delete_phone_number_async(
        self,
        phone_id: str,
    ) -> DeletePhoneNumberResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "phone_numbers/{}".format(phone_id)
        )

        resp = await self.async_client.delete(url)

    def delete_webauthn_registration(
        self,
        webauthn_registration: str,
    ) -> DeleteWebauthnRegistrationResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "webauthn_registrations/{}".format(webauthn_registration)
        )

        resp = self.sync_client.delete(url)

    async def delete_webauthn_registration_async(
        self,
        webauthn_registration: str,
    ) -> DeleteWebauthnRegistrationResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "webauthn_registrations/{}".format(webauthn_registration)
        )

        resp = await self.async_client.delete(url)

    def delete_totp(
        self,
        totp_id: str,
    ) -> DeleteTotpResponse:

        url = self.api_base.route_with_sub_url(self.sub_url, "totps/{}".format(totp_id))

        resp = self.sync_client.delete(url)

    async def delete_totp_async(
        self,
        totp_id: str,
    ) -> DeleteTotpResponse:

        url = self.api_base.route_with_sub_url(self.sub_url, "totps/{}".format(totp_id))

        resp = await self.async_client.delete(url)

    def delete_crypto_wallet(
        self,
        crypto_wallet_id: str,
    ) -> DeleteCryptoWalletResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "crypto_wallets/{}".format(crypto_wallet_id)
        )

        resp = self.sync_client.delete(url)

    async def delete_crypto_wallet_async(
        self,
        crypto_wallet_id: str,
    ) -> DeleteCryptoWalletResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "crypto_wallets/{}".format(crypto_wallet_id)
        )

        resp = await self.async_client.delete(url)

    def delete_password(
        self,
        password_id: str,
    ) -> DeletePasswordResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "passwords/{}".format(password_id)
        )

        resp = self.sync_client.delete(url)

    async def delete_password_async(
        self,
        password_id: str,
    ) -> DeletePasswordResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "passwords/{}".format(password_id)
        )

        resp = await self.async_client.delete(url)

    def delete_biometric_registration(
        self,
        biometric_registration_id: str,
    ) -> DeleteBiometricRegistrationResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "biometric_registrations/{}".format(biometric_registration_id)
        )

        resp = self.sync_client.delete(url)

    async def delete_biometric_registration_async(
        self,
        biometric_registration_id: str,
    ) -> DeleteBiometricRegistrationResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "biometric_registrations/{}".format(biometric_registration_id)
        )

        resp = await self.async_client.delete(url)

    def delete_oauth_user_registration(
        self,
        oauth_user_registration_id: str,
    ) -> DeleteOauthUserRegistrationResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "oauth/{}".format(oauth_user_registration_id)
        )

        resp = self.sync_client.delete(url)

    async def delete_oauth_user_registration_async(
        self,
        oauth_user_registration_id: str,
    ) -> DeleteOauthUserRegistrationResponse:

        url = self.api_base.route_with_sub_url(
            self.sub_url, "oauth/{}".format(oauth_user_registration_id)
        )

        resp = await self.async_client.delete(url)
