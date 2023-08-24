# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, AsyncGenerator, Dict, Generator, Optional

from stytch.consumer.models.attribute import Attributes
from stytch.consumer.models.users import (
    CreateResponse,
    DeleteBiometricRegistrationResponse,
    DeleteCryptoWalletResponse,
    DeleteEmailResponse,
    DeleteOAuthRegistrationResponse,
    DeletePasswordResponse,
    DeletePhoneNumberResponse,
    DeleteResponse,
    DeleteTOTPResponse,
    DeleteWebAuthnRegistrationResponse,
    ExchangePrimaryFactorResponse,
    GetResponse,
    Name,
    SearchResponse,
    SearchUsersQuery,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


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

    def create(
        self,
        email: Optional[str] = None,
        name: Optional[Name] = None,
        attributes: Optional[Attributes] = None,
        phone_number: Optional[str] = None,
        create_user_as_pending: Optional[bool] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """Add a User to Stytch. A `user_id` is returned in the response that can then be used to perform other operations within Stytch. An `email` or a `phone_number` is required.

        Fields:
          - email: The email address of the end user.
          - name: The name of the user. Each field in the name object is optional.
          - attributes: Provided attributes help with fraud detection.
          - phone_number: The phone number to use for one-time passcodes. The phone number should be in E.164 format (i.e. +1XXXXXXXXXX). You may use +10000000000 to test this endpoint, see [Testing](https://stytch.com/docs/home#resources_testing) for more detail.
          - create_user_as_pending: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false.
                If true, users will be saved with status pending in Stytch's backend until authenticated.
                If false, users will be created as active. An example usage of
                a true flag would be to require users to verify their phone by entering the OTP code before creating
                an account for them.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
          - untrusted_metadata: The `untrusted_metadata` field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end users directly via the SDK, and **cannot be used to store critical information.** See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {}
        if email is not None:
            data["email"] = email
        if name is not None:
            data["name"] = name.dict()
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if phone_number is not None:
            data["phone_number"] = phone_number
        if create_user_as_pending is not None:
            data["create_user_as_pending"] = create_user_as_pending
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.url_for("/v1/users", data)
        res = self.sync_client.post(url, data)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        email: Optional[str] = None,
        name: Optional[Name] = None,
        attributes: Optional[Attributes] = None,
        phone_number: Optional[str] = None,
        create_user_as_pending: Optional[bool] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """Add a User to Stytch. A `user_id` is returned in the response that can then be used to perform other operations within Stytch. An `email` or a `phone_number` is required.

        Fields:
          - email: The email address of the end user.
          - name: The name of the user. Each field in the name object is optional.
          - attributes: Provided attributes help with fraud detection.
          - phone_number: The phone number to use for one-time passcodes. The phone number should be in E.164 format (i.e. +1XXXXXXXXXX). You may use +10000000000 to test this endpoint, see [Testing](https://stytch.com/docs/home#resources_testing) for more detail.
          - create_user_as_pending: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false.
                If true, users will be saved with status pending in Stytch's backend until authenticated.
                If false, users will be created as active. An example usage of
                a true flag would be to require users to verify their phone by entering the OTP code before creating
                an account for them.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
          - untrusted_metadata: The `untrusted_metadata` field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end users directly via the SDK, and **cannot be used to store critical information.** See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {}
        if email is not None:
            data["email"] = email
        if name is not None:
            data["name"] = name.dict()
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if phone_number is not None:
            data["phone_number"] = phone_number
        if create_user_as_pending is not None:
            data["create_user_as_pending"] = create_user_as_pending
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.url_for("/v1/users", data)
        res = await self.async_client.post(url, data)
        return CreateResponse.from_json(res.response.status, res.json)

    def get(
        self,
        user_id: str,
    ) -> GetResponse:
        """Get information about a specific User.

        Fields:
          - user_id: The unique ID of a specific User.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/users/{user_id}", data)
        res = self.sync_client.get(url, data)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        user_id: str,
    ) -> GetResponse:
        """Get information about a specific User.

        Fields:
          - user_id: The unique ID of a specific User.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/users/{user_id}", data)
        res = await self.async_client.get(url, data)
        return GetResponse.from_json(res.response.status, res.json)

    def search(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchUsersQuery] = None,
    ) -> SearchResponse:
        """Search for Users within your Stytch Project. Submit an empty `query` in the request to return all Users.

        Fields:
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all results with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {}
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/users/search", data)
        res = self.sync_client.post(url, data)
        return SearchResponse.from_json(res.response.status_code, res.json)

    async def search_async(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchUsersQuery] = None,
    ) -> SearchResponse:
        """Search for Users within your Stytch Project. Submit an empty `query` in the request to return all Users.

        Fields:
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all results with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {}
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/users/search", data)
        res = await self.async_client.post(url, data)
        return SearchResponse.from_json(res.response.status, res.json)

    def update(
        self,
        user_id: str,
        name: Optional[Name] = None,
        attributes: Optional[Attributes] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateResponse:
        """Update a User's attributes.

        **Note:** In order to add a new email address or phone number to an existing User object, pass the new email address or phone number into the respective `/send` endpoint for the authentication method of your choice. If you specify the existing User's `user_id` while calling the `/send` endpoint, the new email address or phone number will be added to the existing User object upon successful authentication. We require this process to guard against an account takeover vulnerability.

        Fields:
          - user_id: The unique ID of a specific User.
          - name: The name of the user. Each field in the name object is optional.
          - attributes: Provided attributes help with fraud detection.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
          - untrusted_metadata: The `untrusted_metadata` field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end users directly via the SDK, and **cannot be used to store critical information.** See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if name is not None:
            data["name"] = name.dict()
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.url_for("/v1/users/{user_id}", data)
        res = self.sync_client.put(url, data)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        user_id: str,
        name: Optional[Name] = None,
        attributes: Optional[Attributes] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateResponse:
        """Update a User's attributes.

        **Note:** In order to add a new email address or phone number to an existing User object, pass the new email address or phone number into the respective `/send` endpoint for the authentication method of your choice. If you specify the existing User's `user_id` while calling the `/send` endpoint, the new email address or phone number will be added to the existing User object upon successful authentication. We require this process to guard against an account takeover vulnerability.

        Fields:
          - user_id: The unique ID of a specific User.
          - name: The name of the user. Each field in the name object is optional.
          - attributes: Provided attributes help with fraud detection.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
          - untrusted_metadata: The `untrusted_metadata` field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end users directly via the SDK, and **cannot be used to store critical information.** See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if name is not None:
            data["name"] = name.dict()
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.url_for("/v1/users/{user_id}", data)
        res = await self.async_client.put(url, data)
        return UpdateResponse.from_json(res.response.status, res.json)

    def exchange_primary_factor(
        self,
        user_id: str,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
    ) -> ExchangePrimaryFactorResponse:
        """Exchange a user's email address or phone number for another.

        Must pass either an `email_address` or a `phone_number`.

        This endpoint only works if the user has exactly one factor. You are able to exchange the type of factor for another as well, i.e. exchange an `email_address` for a `phone_number`.

        Use this endpoint with caution as it performs an admin level action.

        Fields:
          - user_id: The unique ID of a specific User.
          - email_address: The email address to exchange to.
          - phone_number: The phone number to exchange to. The phone number should be in E.164 format (i.e. +1XXXXXXXXXX).
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if email_address is not None:
            data["email_address"] = email_address
        if phone_number is not None:
            data["phone_number"] = phone_number

        url = self.api_base.url_for("/v1/users/{user_id}/exchange_primary_factor", data)
        res = self.sync_client.put(url, data)
        return ExchangePrimaryFactorResponse.from_json(
            res.response.status_code, res.json
        )

    async def exchange_primary_factor_async(
        self,
        user_id: str,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
    ) -> ExchangePrimaryFactorResponse:
        """Exchange a user's email address or phone number for another.

        Must pass either an `email_address` or a `phone_number`.

        This endpoint only works if the user has exactly one factor. You are able to exchange the type of factor for another as well, i.e. exchange an `email_address` for a `phone_number`.

        Use this endpoint with caution as it performs an admin level action.

        Fields:
          - user_id: The unique ID of a specific User.
          - email_address: The email address to exchange to.
          - phone_number: The phone number to exchange to. The phone number should be in E.164 format (i.e. +1XXXXXXXXXX).
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if email_address is not None:
            data["email_address"] = email_address
        if phone_number is not None:
            data["phone_number"] = phone_number

        url = self.api_base.url_for("/v1/users/{user_id}/exchange_primary_factor", data)
        res = await self.async_client.put(url, data)
        return ExchangePrimaryFactorResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        user_id: str,
    ) -> DeleteResponse:
        """Delete a User from Stytch.

        Fields:
          - user_id: The unique ID of a specific User.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/users/{user_id}", data)
        res = self.sync_client.delete(url)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
        self,
        user_id: str,
    ) -> DeleteResponse:
        """Delete a User from Stytch.

        Fields:
          - user_id: The unique ID of a specific User.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/users/{user_id}", data)
        res = await self.async_client.delete(url)
        return DeleteResponse.from_json(res.response.status, res.json)

    def delete_email(
        self,
        email_id: str,
    ) -> DeleteEmailResponse:
        """Delete an email from a User.

        Fields:
          - email_id: The `email_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "email_id": email_id,
        }

        url = self.api_base.url_for("/v1/users/emails/{email_id}", data)
        res = self.sync_client.delete(url)
        return DeleteEmailResponse.from_json(res.response.status_code, res.json)

    async def delete_email_async(
        self,
        email_id: str,
    ) -> DeleteEmailResponse:
        """Delete an email from a User.

        Fields:
          - email_id: The `email_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "email_id": email_id,
        }

        url = self.api_base.url_for("/v1/users/emails/{email_id}", data)
        res = await self.async_client.delete(url)
        return DeleteEmailResponse.from_json(res.response.status, res.json)

    def delete_phone_number(
        self,
        phone_id: str,
    ) -> DeletePhoneNumberResponse:
        """Delete a phone number from a User.

        Fields:
          - phone_id: The `phone_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "phone_id": phone_id,
        }

        url = self.api_base.url_for("/v1/users/phone_numbers/{phone_id}", data)
        res = self.sync_client.delete(url)
        return DeletePhoneNumberResponse.from_json(res.response.status_code, res.json)

    async def delete_phone_number_async(
        self,
        phone_id: str,
    ) -> DeletePhoneNumberResponse:
        """Delete a phone number from a User.

        Fields:
          - phone_id: The `phone_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "phone_id": phone_id,
        }

        url = self.api_base.url_for("/v1/users/phone_numbers/{phone_id}", data)
        res = await self.async_client.delete(url)
        return DeletePhoneNumberResponse.from_json(res.response.status, res.json)

    def delete_webauthn_registration(
        self,
        webauthn_registration_id: str,
    ) -> DeleteWebAuthnRegistrationResponse:
        """Delete a WebAuthn registration from a User.

        Fields:
          - webauthn_registration_id: The `webauthn_registration_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "webauthn_registration_id": webauthn_registration_id,
        }

        url = self.api_base.url_for(
            "/v1/users/webauthn_registrations/{webauthn_registration_id}", data
        )
        res = self.sync_client.delete(url)
        return DeleteWebAuthnRegistrationResponse.from_json(
            res.response.status_code, res.json
        )

    async def delete_webauthn_registration_async(
        self,
        webauthn_registration_id: str,
    ) -> DeleteWebAuthnRegistrationResponse:
        """Delete a WebAuthn registration from a User.

        Fields:
          - webauthn_registration_id: The `webauthn_registration_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "webauthn_registration_id": webauthn_registration_id,
        }

        url = self.api_base.url_for(
            "/v1/users/webauthn_registrations/{webauthn_registration_id}", data
        )
        res = await self.async_client.delete(url)
        return DeleteWebAuthnRegistrationResponse.from_json(
            res.response.status, res.json
        )

    def delete_biometric_registration(
        self,
        biometric_registration_id: str,
    ) -> DeleteBiometricRegistrationResponse:
        """Delete a biometric registration from a User.

        Fields:
          - biometric_registration_id: The `biometric_registration_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "biometric_registration_id": biometric_registration_id,
        }

        url = self.api_base.url_for(
            "/v1/users/biometric_registrations/{biometric_registration_id}", data
        )
        res = self.sync_client.delete(url)
        return DeleteBiometricRegistrationResponse.from_json(
            res.response.status_code, res.json
        )

    async def delete_biometric_registration_async(
        self,
        biometric_registration_id: str,
    ) -> DeleteBiometricRegistrationResponse:
        """Delete a biometric registration from a User.

        Fields:
          - biometric_registration_id: The `biometric_registration_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "biometric_registration_id": biometric_registration_id,
        }

        url = self.api_base.url_for(
            "/v1/users/biometric_registrations/{biometric_registration_id}", data
        )
        res = await self.async_client.delete(url)
        return DeleteBiometricRegistrationResponse.from_json(
            res.response.status, res.json
        )

    def delete_totp(
        self,
        totp_id: str,
    ) -> DeleteTOTPResponse:
        """Delete a TOTP from a User.

        Fields:
          - totp_id: The `totp_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "totp_id": totp_id,
        }

        url = self.api_base.url_for("/v1/users/totps/{totp_id}", data)
        res = self.sync_client.delete(url)
        return DeleteTOTPResponse.from_json(res.response.status_code, res.json)

    async def delete_totp_async(
        self,
        totp_id: str,
    ) -> DeleteTOTPResponse:
        """Delete a TOTP from a User.

        Fields:
          - totp_id: The `totp_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "totp_id": totp_id,
        }

        url = self.api_base.url_for("/v1/users/totps/{totp_id}", data)
        res = await self.async_client.delete(url)
        return DeleteTOTPResponse.from_json(res.response.status, res.json)

    def delete_crypto_wallet(
        self,
        crypto_wallet_id: str,
    ) -> DeleteCryptoWalletResponse:
        """Delete a crypto wallet from a User.

        Fields:
          - crypto_wallet_id: The `crypto_wallet_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "crypto_wallet_id": crypto_wallet_id,
        }

        url = self.api_base.url_for("/v1/users/crypto_wallets/{crypto_wallet_id}", data)
        res = self.sync_client.delete(url)
        return DeleteCryptoWalletResponse.from_json(res.response.status_code, res.json)

    async def delete_crypto_wallet_async(
        self,
        crypto_wallet_id: str,
    ) -> DeleteCryptoWalletResponse:
        """Delete a crypto wallet from a User.

        Fields:
          - crypto_wallet_id: The `crypto_wallet_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "crypto_wallet_id": crypto_wallet_id,
        }

        url = self.api_base.url_for("/v1/users/crypto_wallets/{crypto_wallet_id}", data)
        res = await self.async_client.delete(url)
        return DeleteCryptoWalletResponse.from_json(res.response.status, res.json)

    def delete_password(
        self,
        password_id: str,
    ) -> DeletePasswordResponse:
        """Delete a password from a User.

        Fields:
          - password_id: The `password_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "password_id": password_id,
        }

        url = self.api_base.url_for("/v1/users/passwords/{password_id}", data)
        res = self.sync_client.delete(url)
        return DeletePasswordResponse.from_json(res.response.status_code, res.json)

    async def delete_password_async(
        self,
        password_id: str,
    ) -> DeletePasswordResponse:
        """Delete a password from a User.

        Fields:
          - password_id: The `password_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "password_id": password_id,
        }

        url = self.api_base.url_for("/v1/users/passwords/{password_id}", data)
        res = await self.async_client.delete(url)
        return DeletePasswordResponse.from_json(res.response.status, res.json)

    def delete_oauth_registration(
        self,
        oauth_user_registration_id: str,
    ) -> DeleteOAuthRegistrationResponse:
        """Delete an OAuth registration from a User.

        Fields:
          - oauth_user_registration_id: The `oauth_user_registration_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "oauth_user_registration_id": oauth_user_registration_id,
        }

        url = self.api_base.url_for(
            "/v1/users/oauth/{oauth_user_registration_id}", data
        )
        res = self.sync_client.delete(url)
        return DeleteOAuthRegistrationResponse.from_json(
            res.response.status_code, res.json
        )

    async def delete_oauth_registration_async(
        self,
        oauth_user_registration_id: str,
    ) -> DeleteOAuthRegistrationResponse:
        """Delete an OAuth registration from a User.

        Fields:
          - oauth_user_registration_id: The `oauth_user_registration_id` to be deleted.
        """  # noqa
        data: Dict[str, Any] = {
            "oauth_user_registration_id": oauth_user_registration_id,
        }

        url = self.api_base.url_for(
            "/v1/users/oauth/{oauth_user_registration_id}", data
        )
        res = await self.async_client.delete(url)
        return DeleteOAuthRegistrationResponse.from_json(res.response.status, res.json)

    # MANUAL(search_all)(SERVICE_METHOD)
    # ADDIMPORT: from typing import AsyncGenerator, Generator
    def search_all(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchUsersQuery] = None,
    ) -> Generator[SearchResponse, None, None]:
        """Iterate through a search query continuously until there are no more results.
        This method will yield batches of results until the search has been exhausted.
        """
        while True:
            results = self.search(limit=limit, cursor=cursor, query=query)
            yield results
            cursor = results.results_metadata.next_cursor
            if cursor is None:
                break

    async def search_all_async(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchUsersQuery] = None,
    ) -> AsyncGenerator[SearchResponse, None]:
        """Iterate through a search query continuously until there are no more results.
        This method will yield batches of results until the search has been exhausted.
        """
        while True:
            results = await self.search_async(limit=limit, cursor=cursor, query=query)
            yield results
            cursor = results.results_metadata.next_cursor
            if cursor is None:
                break

    # ENDMANUAL(search_all)
