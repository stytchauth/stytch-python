# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.consumer.models.webauthn import (
    AuthenticateResponse,
    AuthenticateStartResponse,
    RegisterResponse,
    RegisterStartResponse,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class WebAuthn:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def register_start(
        self,
        user_id: str,
        domain: str,
        user_agent: Optional[str] = None,
        authenticator_type: Optional[str] = None,
        return_passkey_credential_options: Optional[bool] = None,
        override_id: Optional[str] = None,
        override_name: Optional[str] = None,
        override_display_name: Optional[str] = None,
    ) -> RegisterStartResponse:
        """Initiate the process of creating a new Passkey or WebAuthn registration.

        To optimize for Passkeys, set the `return_passkey_credential_options` field to `true`.

        After calling this endpoint, the browser will need to call [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) with the data from [public_key_credential_creation_options](https://w3c.github.io/webauthn/#dictionary-makecredentialoptions) passed to the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) request via the public key argument. We recommend using the `create()` wrapper provided by the webauthn-json library.

        If you are not using the [webauthn-json](https://github.com/github/webauthn-json) library, the `public_key_credential_creation_options` will need to be converted to a suitable public key by unmarshalling the JSON, base64 decoding the user ID field, and converting user ID and the challenge fields into an array buffer.

        Fields:
          - user_id: The `user_id` of an active user the Passkey or WebAuthn registration should be tied to.
          - domain: The domain for Passkeys or WebAuthn. Defaults to `window.location.hostname`.
          - user_agent: The user agent of the User.
          - authenticator_type: The requested authenticator type of the Passkey or WebAuthn device. The two valid values are platform and cross-platform. If no value passed, we assume both values are allowed.
          - return_passkey_credential_options: If true, the `public_key_credential_creation_options` returned will be optimized for Passkeys with `residentKey` set to `"required"` and `userVerification` set to `"preferred"`.

          - override_id: (no documentation yet)
          - override_name: (no documentation yet)
          - override_display_name: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }
        if user_agent is not None:
            data["user_agent"] = user_agent
        if authenticator_type is not None:
            data["authenticator_type"] = authenticator_type
        if return_passkey_credential_options is not None:
            data[
                "return_passkey_credential_options"
            ] = return_passkey_credential_options
        if override_id is not None:
            data["override_id"] = override_id
        if override_name is not None:
            data["override_name"] = override_name
        if override_display_name is not None:
            data["override_display_name"] = override_display_name

        url = self.api_base.url_for("/v1/webauthn/register/start", data)
        res = self.sync_client.post(url, data, headers)
        return RegisterStartResponse.from_json(res.response.status_code, res.json)

    async def register_start_async(
        self,
        user_id: str,
        domain: str,
        user_agent: Optional[str] = None,
        authenticator_type: Optional[str] = None,
        return_passkey_credential_options: Optional[bool] = None,
        override_id: Optional[str] = None,
        override_name: Optional[str] = None,
        override_display_name: Optional[str] = None,
    ) -> RegisterStartResponse:
        """Initiate the process of creating a new Passkey or WebAuthn registration.

        To optimize for Passkeys, set the `return_passkey_credential_options` field to `true`.

        After calling this endpoint, the browser will need to call [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) with the data from [public_key_credential_creation_options](https://w3c.github.io/webauthn/#dictionary-makecredentialoptions) passed to the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) request via the public key argument. We recommend using the `create()` wrapper provided by the webauthn-json library.

        If you are not using the [webauthn-json](https://github.com/github/webauthn-json) library, the `public_key_credential_creation_options` will need to be converted to a suitable public key by unmarshalling the JSON, base64 decoding the user ID field, and converting user ID and the challenge fields into an array buffer.

        Fields:
          - user_id: The `user_id` of an active user the Passkey or WebAuthn registration should be tied to.
          - domain: The domain for Passkeys or WebAuthn. Defaults to `window.location.hostname`.
          - user_agent: The user agent of the User.
          - authenticator_type: The requested authenticator type of the Passkey or WebAuthn device. The two valid values are platform and cross-platform. If no value passed, we assume both values are allowed.
          - return_passkey_credential_options: If true, the `public_key_credential_creation_options` returned will be optimized for Passkeys with `residentKey` set to `"required"` and `userVerification` set to `"preferred"`.

          - override_id: (no documentation yet)
          - override_name: (no documentation yet)
          - override_display_name: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
            "domain": domain,
        }
        if user_agent is not None:
            data["user_agent"] = user_agent
        if authenticator_type is not None:
            data["authenticator_type"] = authenticator_type
        if return_passkey_credential_options is not None:
            data[
                "return_passkey_credential_options"
            ] = return_passkey_credential_options
        if override_id is not None:
            data["override_id"] = override_id
        if override_name is not None:
            data["override_name"] = override_name
        if override_display_name is not None:
            data["override_display_name"] = override_display_name

        url = self.api_base.url_for("/v1/webauthn/register/start", data)
        res = await self.async_client.post(url, data, headers)
        return RegisterStartResponse.from_json(res.response.status, res.json)

    def register(
        self,
        user_id: str,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> RegisterResponse:
        """Complete the creation of a WebAuthn registration by passing the response from the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) request to this endpoint as the `public_key_credential` parameter.

        If the [webauthn-json](https://github.com/github/webauthn-json) library's `create()` method was used, the response can be passed directly to the [register endpoint](https://stytch.com/docs/api/webauthn-register). If not, some fields (the client data and the attestation object) from the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) response will need to be converted from array buffers to strings and marshalled into JSON.

        Fields:
          - user_id: The `user_id` of an active user the Passkey or WebAuthn registration should be tied to.
          - public_key_credential: The response of the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential).
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/webauthn/register", data)
        res = self.sync_client.post(url, data, headers)
        return RegisterResponse.from_json(res.response.status_code, res.json)

    async def register_async(
        self,
        user_id: str,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> RegisterResponse:
        """Complete the creation of a WebAuthn registration by passing the response from the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) request to this endpoint as the `public_key_credential` parameter.

        If the [webauthn-json](https://github.com/github/webauthn-json) library's `create()` method was used, the response can be passed directly to the [register endpoint](https://stytch.com/docs/api/webauthn-register). If not, some fields (the client data and the attestation object) from the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential) response will need to be converted from array buffers to strings and marshalled into JSON.

        Fields:
          - user_id: The `user_id` of an active user the Passkey or WebAuthn registration should be tied to.
          - public_key_credential: The response of the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential).
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/webauthn/register", data)
        res = await self.async_client.post(url, data, headers)
        return RegisterResponse.from_json(res.response.status, res.json)

    def authenticate_start(
        self,
        domain: str,
        user_id: Optional[str] = None,
        return_passkey_credential_options: Optional[bool] = None,
    ) -> AuthenticateStartResponse:
        """Initiate the authentication of a Passkey or WebAuthn registration.

        To optimize for Passkeys, set the `return_passkey_credential_options` field to `true`.

        After calling this endpoint, the browser will need to call [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) with the data from `public_key_credential_request_options` passed to the [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) request via the public key argument. We recommend using the `get()` wrapper provided by the webauthn-json library.

        If you are not using the [webauthn-json](https://github.com/github/webauthn-json) library, `the public_key_credential_request_options` will need to be converted to a suitable public key by unmarshalling the JSON and converting some the fields to array buffers.

        Fields:
          - domain: The domain for Passkeys or WebAuthn. Defaults to `window.location.hostname`.
          - user_id: The `user_id` of an active user the Passkey or WebAuthn registration should be tied to.
          - return_passkey_credential_options: If true, the `public_key_credential_creation_options` returned will be optimized for Passkeys with `userVerification` set to `"preferred"`.

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "domain": domain,
        }
        if user_id is not None:
            data["user_id"] = user_id
        if return_passkey_credential_options is not None:
            data[
                "return_passkey_credential_options"
            ] = return_passkey_credential_options

        url = self.api_base.url_for("/v1/webauthn/authenticate/start", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateStartResponse.from_json(res.response.status_code, res.json)

    async def authenticate_start_async(
        self,
        domain: str,
        user_id: Optional[str] = None,
        return_passkey_credential_options: Optional[bool] = None,
    ) -> AuthenticateStartResponse:
        """Initiate the authentication of a Passkey or WebAuthn registration.

        To optimize for Passkeys, set the `return_passkey_credential_options` field to `true`.

        After calling this endpoint, the browser will need to call [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) with the data from `public_key_credential_request_options` passed to the [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) request via the public key argument. We recommend using the `get()` wrapper provided by the webauthn-json library.

        If you are not using the [webauthn-json](https://github.com/github/webauthn-json) library, `the public_key_credential_request_options` will need to be converted to a suitable public key by unmarshalling the JSON and converting some the fields to array buffers.

        Fields:
          - domain: The domain for Passkeys or WebAuthn. Defaults to `window.location.hostname`.
          - user_id: The `user_id` of an active user the Passkey or WebAuthn registration should be tied to.
          - return_passkey_credential_options: If true, the `public_key_credential_creation_options` returned will be optimized for Passkeys with `userVerification` set to `"preferred"`.

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "domain": domain,
        }
        if user_id is not None:
            data["user_id"] = user_id
        if return_passkey_credential_options is not None:
            data[
                "return_passkey_credential_options"
            ] = return_passkey_credential_options

        url = self.api_base.url_for("/v1/webauthn/authenticate/start", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateStartResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Complete the authentication of a Passkey or WebAuthn registration by passing the response from the [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) request to the authenticate endpoint.

        If the [webauthn-json](https://github.com/github/webauthn-json) library's `get()` method was used, the response can be passed directly to the [authenticate endpoint](https://stytch.com/docs/api/webauthn-authenticate). If not some fields from the [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) response will need to be converted from array buffers to strings and marshalled into JSON.

        Fields:
          - public_key_credential: The response of the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential).
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "public_key_credential": public_key_credential,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/webauthn/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Complete the authentication of a Passkey or WebAuthn registration by passing the response from the [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) request to the authenticate endpoint.

        If the [webauthn-json](https://github.com/github/webauthn-json) library's `get()` method was used, the response can be passed directly to the [authenticate endpoint](https://stytch.com/docs/api/webauthn-authenticate). If not some fields from the [navigator.credentials.get()](https://www.w3.org/TR/webauthn-2/#sctn-getAssertion) response will need to be converted from array buffers to strings and marshalled into JSON.

        Fields:
          - public_key_credential: The response of the [navigator.credentials.create()](https://www.w3.org/TR/webauthn-2/#sctn-createCredential).
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "public_key_credential": public_key_credential,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/webauthn/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)

    def update(
        self,
        webauthn_registration_id: str,
        name: str,
    ) -> UpdateResponse:
        """Updates a Passkey or WebAuthn registration.

        Fields:
          - webauthn_registration_id: Globally unique UUID that identifies a Passkey or WebAuthn registration in the Stytch API. The `webauthn_registration_id` is used when you need to operate on a specific User's WebAuthn registration.
          - name: The `name` of the WebAuthn registration or Passkey.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "webauthn_registration_id": webauthn_registration_id,
            "name": name,
        }

        url = self.api_base.url_for("/v1/webauthn/{webauthn_registration_id}", data)
        res = self.sync_client.put(url, data, headers)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        webauthn_registration_id: str,
        name: str,
    ) -> UpdateResponse:
        """Updates a Passkey or WebAuthn registration.

        Fields:
          - webauthn_registration_id: Globally unique UUID that identifies a Passkey or WebAuthn registration in the Stytch API. The `webauthn_registration_id` is used when you need to operate on a specific User's WebAuthn registration.
          - name: The `name` of the WebAuthn registration or Passkey.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "webauthn_registration_id": webauthn_registration_id,
            "name": name,
        }

        url = self.api_base.url_for("/v1/webauthn/{webauthn_registration_id}", data)
        res = await self.async_client.put(url, data, headers)
        return UpdateResponse.from_json(res.response.status, res.json)
