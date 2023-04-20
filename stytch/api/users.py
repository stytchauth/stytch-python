# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

import time
from typing import Any, AsyncGenerator, Dict, Generator, List, Optional, Union

import jwt
import pydantic
from stytch.core.api_base import ApiBase
from stytch.core.b2b.models import B2BStytchSession, Member, Organization
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import (
    Name,
    SearchQuery,
    SearchResultsMetadata,
    StytchSession,
    User,
)
from stytch.models.users import (
    CreateResponse,
    DeleteEmailResponse,
    DeleteOauthUserRegistrationResponse,
    DeletePhoneNumberResponse,
    DeleteuserbiometricregistrationResponse,
    DeleteusercryptowalletResponse,
    DeleteuserpasswordResponse,
    DeleteuserResponse,
    DeleteusertotpResponse,
    DeleteuserwebauthnregistrationResponse,
    GetbyemailandprojectidResponse,
    GetpendingusersResponse,
    GetResponse,
    SearchusersexternalResponse,
    UpdateuserResponse,
)


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
        name: TODO,
        attributes: Optional[Dict[str, str]] = None,
        phone_number: Optional[str] = None,
        create_user_as_pending: bool,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """[Stytch docs](https://stytch.com/docs/api/create-user)

    Add a user to Stytch. A `user_id` is returned in the response that can then be used to perform other operations within Stytch. An `email` or a `phone_number` is required.
        """  # noqa

        payload: Dict[str, Any] = {
            "name": name,

            "create_user_as_pending": create_user_as_pending,

        }

        if email is not None:
            payload["email"] = email

        if attributes is not None:
            payload["attributes"] = attributes

        if phone_number is not None:
            payload["phone_number"] = phone_number

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users")

        res = self.sync_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
      self,
      email: Optional[str] = None,
      name: TODO,
      attributes: Optional[Dict[str, str]] = None,
      phone_number: Optional[str] = None,
      create_user_as_pending: bool,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """[Stytch docs](https://stytch.com/docs/api/create-user)

    Add a user to Stytch. A `user_id` is returned in the response that can then be used to perform other operations within Stytch. An `email` or a `phone_number` is required.
        """  # noqa

        payload: Dict[str, Any] = {
            "name": name,

            "create_user_as_pending": create_user_as_pending,

        }

        if email is not None:
            payload["email"] = email

        if attributes is not None:
            payload["attributes"] = attributes

        if phone_number is not None:
            payload["phone_number"] = phone_number

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users")

        res = await self.async_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status, res.json)

    def GetPendingUsers(
        self,
        starting_after_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> GetpendingusersResponse:

        payload: Dict[str, Any] = {
        }

        if starting_after_id is not None:
            payload["starting_after_id"] = starting_after_id

        if limit is not None:
            payload["limit"] = limit


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/pending")

        res = self.sync_client.get(url, params=payload)
        return GetpendingusersResponse.from_json(res.response.status_code, res.json)

    async def GetPendingUsers_async(
      self,
      starting_after_id: Optional[str] = None,
      limit: Optional[int] = None,
    ) -> GetpendingusersResponse:

        payload: Dict[str, Any] = {
        }

        if starting_after_id is not None:
            payload["starting_after_id"] = starting_after_id

        if limit is not None:
            payload["limit"] = limit


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/pending")

        res = await self.async_client.get(url, params=payload)
        return GetpendingusersResponse.from_json(res.response.status, res.json)

    def get(
        self,
        user_id: str,
    ) -> GetResponse:
        """[Stytch docs](https://stytch.com/docs/api/get-user)

    Fetch a given user to see what their various attributes are. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
        """  # noqa

        payload: Dict[str, Any] = {
            "user_id": user_id,

        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/{user_id}")

        res = self.sync_client.get(url, params=payload)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
      self,
      user_id: str,
    ) -> GetResponse:
        """[Stytch docs](https://stytch.com/docs/api/get-user)

    Fetch a given user to see what their various attributes are. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
        """  # noqa

        payload: Dict[str, Any] = {
            "user_id": user_id,

        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/{user_id}")

        res = await self.async_client.get(url, params=payload)
        return GetResponse.from_json(res.response.status, res.json)

    def SearchUsersExternal(
        self,
        cursor: str,
        limit: Optional[int] = None,
        query: TODO,
    ) -> SearchusersexternalResponse:

        payload: Dict[str, Any] = {
            "cursor": cursor,

            "query": query,

        }

        if limit is not None:
            payload["limit"] = limit


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/search")

        res = self.sync_client.post(url, json=payload)
        return SearchusersexternalResponse.from_json(res.response.status_code, res.json)

    async def SearchUsersExternal_async(
      self,
      cursor: str,
      limit: Optional[int] = None,
      query: TODO,
    ) -> SearchusersexternalResponse:

        payload: Dict[str, Any] = {
            "cursor": cursor,

            "query": query,

        }

        if limit is not None:
            payload["limit"] = limit


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/search")

        res = await self.async_client.post(url, json=payload)
        return SearchusersexternalResponse.from_json(res.response.status, res.json)

    def UpdateUser(
        self,
        user_id: str,
        name: TODO,
        emails: TODO,
        attributes: Optional[Dict[str, str]] = None,
        phone_numbers: TODO,
        crypto_wallets: TODO,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateuserResponse:

        payload: Dict[str, Any] = {
            "user_id": user_id,

            "name": name,

            "emails": emails,

            "phone_numbers": phone_numbers,

            "crypto_wallets": crypto_wallets,

        }

        if attributes is not None:
            payload["attributes"] = attributes

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/{user_id}")

        res = self.sync_client.put(url, json=payload)
        return UpdateuserResponse.from_json(res.response.status_code, res.json)

    async def UpdateUser_async(
      self,
      user_id: str,
      name: TODO,
      emails: TODO,
      attributes: Optional[Dict[str, str]] = None,
      phone_numbers: TODO,
      crypto_wallets: TODO,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateuserResponse:

        payload: Dict[str, Any] = {
            "user_id": user_id,

            "name": name,

            "emails": emails,

            "phone_numbers": phone_numbers,

            "crypto_wallets": crypto_wallets,

        }

        if attributes is not None:
            payload["attributes"] = attributes

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/{user_id}")

        res = await self.async_client.put(url, json=payload)
        return UpdateuserResponse.from_json(res.response.status, res.json)

    def DeleteUser(
        self,
        user_id: str,
    ) -> DeleteuserResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/{user_id}")

        res = self.sync_client.delete(url)
        return DeleteuserResponse.from_json(res.response.status_code, res.json)

    async def DeleteUser_async(
      self,
      user_id: str,
    ) -> DeleteuserResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/{user_id}")

        res = await self.async_client.delete(url)
        return DeleteuserResponse.from_json(res.response.status, res.json)

    def getByEmailAndProjectID(
        self,
        email: str,
        project_id: str,
    ) -> GetbyemailandprojectidResponse:

        payload: Dict[str, Any] = {
            "email": email,

            "project_id": project_id,

        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/sdk/users")

        res = self.sync_client.get(url, params=payload)
        return GetbyemailandprojectidResponse.from_json(res.response.status_code, res.json)

    async def getByEmailAndProjectID_async(
      self,
      email: str,
      project_id: str,
    ) -> GetbyemailandprojectidResponse:

        payload: Dict[str, Any] = {
            "email": email,

            "project_id": project_id,

        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/sdk/users")

        res = await self.async_client.get(url, params=payload)
        return GetbyemailandprojectidResponse.from_json(res.response.status, res.json)

    def delete_email(
        self,
        email_id: str,
    ) -> DeleteEmailResponse:
        """[Stytch docs](https://stytch.com/docs/api/delete-user-email)

    Remove an email from a given user.
        """  # noqa


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/emails/{email_id}")

        res = self.sync_client.delete(url)
        return DeleteEmailResponse.from_json(res.response.status_code, res.json)

    async def delete_email_async(
      self,
      email_id: str,
    ) -> DeleteEmailResponse:
        """[Stytch docs](https://stytch.com/docs/api/delete-user-email)

    Remove an email from a given user.
        """  # noqa


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/emails/{email_id}")

        res = await self.async_client.delete(url)
        return DeleteEmailResponse.from_json(res.response.status, res.json)

    def delete_phone_number(
        self,
        phone_id: str,
    ) -> DeletePhoneNumberResponse:
        """[Stytch docs](https://stytch.com/docs/api/delete-user-phone-number)

    Remove a phone number from a given user.
        """  # noqa


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/phone_numbers/{phone_id}")

        res = self.sync_client.delete(url)
        return DeletePhoneNumberResponse.from_json(res.response.status_code, res.json)

    async def delete_phone_number_async(
      self,
      phone_id: str,
    ) -> DeletePhoneNumberResponse:
        """[Stytch docs](https://stytch.com/docs/api/delete-user-phone-number)

    Remove a phone number from a given user.
        """  # noqa


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/phone_numbers/{phone_id}")

        res = await self.async_client.delete(url)
        return DeletePhoneNumberResponse.from_json(res.response.status, res.json)

    def DeleteUserWebAuthnRegistration(
        self,
        webauthn_registration_id: str,
    ) -> DeleteuserwebauthnregistrationResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/webauthn_registrations/{webauthn_registration_id}")

        res = self.sync_client.delete(url)
        return DeleteuserwebauthnregistrationResponse.from_json(res.response.status_code, res.json)

    async def DeleteUserWebAuthnRegistration_async(
      self,
      webauthn_registration_id: str,
    ) -> DeleteuserwebauthnregistrationResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/webauthn_registrations/{webauthn_registration_id}")

        res = await self.async_client.delete(url)
        return DeleteuserwebauthnregistrationResponse.from_json(res.response.status, res.json)

    def DeleteUserBiometricRegistration(
        self,
        biometric_registration_id: str,
    ) -> DeleteuserbiometricregistrationResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/biometric_registrations/{biometric_registration_id}")

        res = self.sync_client.delete(url)
        return DeleteuserbiometricregistrationResponse.from_json(res.response.status_code, res.json)

    async def DeleteUserBiometricRegistration_async(
      self,
      biometric_registration_id: str,
    ) -> DeleteuserbiometricregistrationResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/biometric_registrations/{biometric_registration_id}")

        res = await self.async_client.delete(url)
        return DeleteuserbiometricregistrationResponse.from_json(res.response.status, res.json)

    def DeleteUserTOTP(
        self,
        totp_id: str,
    ) -> DeleteusertotpResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/totps/{totp_id}")

        res = self.sync_client.delete(url)
        return DeleteusertotpResponse.from_json(res.response.status_code, res.json)

    async def DeleteUserTOTP_async(
      self,
      totp_id: str,
    ) -> DeleteusertotpResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/totps/{totp_id}")

        res = await self.async_client.delete(url)
        return DeleteusertotpResponse.from_json(res.response.status, res.json)

    def DeleteUserCryptoWallet(
        self,
        crypto_wallet_id: str,
    ) -> DeleteusercryptowalletResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/crypto_wallets/{crypto_wallet_id}")

        res = self.sync_client.delete(url)
        return DeleteusercryptowalletResponse.from_json(res.response.status_code, res.json)

    async def DeleteUserCryptoWallet_async(
      self,
      crypto_wallet_id: str,
    ) -> DeleteusercryptowalletResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/crypto_wallets/{crypto_wallet_id}")

        res = await self.async_client.delete(url)
        return DeleteusercryptowalletResponse.from_json(res.response.status, res.json)

    def DeleteUserPassword(
        self,
        password_id: str,
    ) -> DeleteuserpasswordResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/passwords/{password_id}")

        res = self.sync_client.delete(url)
        return DeleteuserpasswordResponse.from_json(res.response.status_code, res.json)

    async def DeleteUserPassword_async(
      self,
      password_id: str,
    ) -> DeleteuserpasswordResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/passwords/{password_id}")

        res = await self.async_client.delete(url)
        return DeleteuserpasswordResponse.from_json(res.response.status, res.json)

    def delete_oauth_user_registration(
        self,
        oauth_user_registration_id: str,
    ) -> DeleteOauthUserRegistrationResponse:
        """[Stytch docs](https://stytch.com/docs/api/delete-user-oauth-registration)

    Delete an oauth user registration.
        """  # noqa


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/oauth/{oauth_user_registration_id}")

        res = self.sync_client.delete(url)
        return DeleteOauthUserRegistrationResponse.from_json(res.response.status_code, res.json)

    async def delete_oauth_user_registration_async(
      self,
      oauth_user_registration_id: str,
    ) -> DeleteOauthUserRegistrationResponse:
        """[Stytch docs](https://stytch.com/docs/api/delete-user-oauth-registration)

    Delete an oauth user registration.
        """  # noqa


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/users/oauth/{oauth_user_registration_id}")

        res = await self.async_client.delete(url)
        return DeleteOauthUserRegistrationResponse.from_json(res.response.status, res.json)

