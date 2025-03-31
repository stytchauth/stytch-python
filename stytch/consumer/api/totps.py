# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.consumer.models.totps import (
    AuthenticateResponse,
    CreateResponse,
    RecoverResponse,
    RecoveryCodesResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class TOTPs:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def create(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ) -> CreateResponse:
        """Create a new TOTP instance for a user. The user can use the authenticator application of their choice to scan the QR code or enter the secret.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
          - expiration_minutes: The expiration for the TOTP instance. If the newly created TOTP is not authenticated within this time frame the TOTP will be unusable. Defaults to 1440 (1 day) with a minimum of 5 and a maximum of 1440.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes

        url = self.api_base.url_for("/v1/totps", data)
        res = self.sync_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ) -> CreateResponse:
        """Create a new TOTP instance for a user. The user can use the authenticator application of their choice to scan the QR code or enter the secret.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
          - expiration_minutes: The expiration for the TOTP instance. If the newly created TOTP is not authenticated within this time frame the TOTP will be unusable. Defaults to 1440 (1 day) with a minimum of 5 and a maximum of 1440.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes

        url = self.api_base.url_for("/v1/totps", data)
        res = await self.async_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticate a TOTP code entered by a user.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
          - totp_code: The TOTP code to authenticate. The TOTP code should consist of 6 digits.
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
            "totp_code": totp_code,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/totps/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticate a TOTP code entered by a user.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
          - totp_code: The TOTP code to authenticate. The TOTP code should consist of 6 digits.
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
            "totp_code": totp_code,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/totps/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)

    def recovery_codes(
        self,
        user_id: str,
    ) -> RecoveryCodesResponse:
        """Retrieve the recovery codes for a TOTP instance tied to a User.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/totps/recovery_codes", data)
        res = self.sync_client.post(url, data, headers)
        return RecoveryCodesResponse.from_json(res.response.status_code, res.json)

    async def recovery_codes_async(
        self,
        user_id: str,
    ) -> RecoveryCodesResponse:
        """Retrieve the recovery codes for a TOTP instance tied to a User.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/totps/recovery_codes", data)
        res = await self.async_client.post(url, data, headers)
        return RecoveryCodesResponse.from_json(res.response.status, res.json)

    def recover(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> RecoverResponse:
        """Authenticate a recovery code for a TOTP instance.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
          - recovery_code: The recovery code to authenticate.
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
            "recovery_code": recovery_code,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/totps/recover", data)
        res = self.sync_client.post(url, data, headers)
        return RecoverResponse.from_json(res.response.status_code, res.json)

    async def recover_async(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> RecoverResponse:
        """Authenticate a recovery code for a TOTP instance.

        Fields:
          - user_id: The `user_id` of an active user the TOTP registration should be tied to. You may use an external_id here if one is set for the user.
          - recovery_code: The recovery code to authenticate.
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
            "recovery_code": recovery_code,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/totps/recover", data)
        res = await self.async_client.post(url, data, headers)
        return RecoverResponse.from_json(res.response.status, res.json)
