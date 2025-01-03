# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.consumer.models.oauth import AttachResponse, AuthenticateResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class OAuth:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def attach(
        self,
        provider: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> AttachResponse:
        """Generate an OAuth Attach Token to pre-associate an OAuth flow with an existing Stytch User. Pass the returned `oauth_attach_token` to the same provider's OAuth Start endpoint to treat this OAuth flow as a login for that user instead of a signup for a new user.

        Exactly one of `user_id`, `session_token`, or `session_jwt` must be provided to identify the target Stytch User.

        This is an optional step in the OAuth flow. Stytch can often determine whether to create a new user or log in an existing one based on verified identity provider information. This endpoint is useful for cases where we can't, such as missing or unverified provider information.

        Fields:
          - provider: The OAuth provider's name.
          - user_id: The unique ID of a specific User.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "provider": provider,
        }
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/oauth/attach", data)
        res = self.sync_client.post(url, data, headers)
        return AttachResponse.from_json(res.response.status_code, res.json)

    async def attach_async(
        self,
        provider: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> AttachResponse:
        """Generate an OAuth Attach Token to pre-associate an OAuth flow with an existing Stytch User. Pass the returned `oauth_attach_token` to the same provider's OAuth Start endpoint to treat this OAuth flow as a login for that user instead of a signup for a new user.

        Exactly one of `user_id`, `session_token`, or `session_jwt` must be provided to identify the target Stytch User.

        This is an optional step in the OAuth flow. Stytch can often determine whether to create a new user or log in an existing one based on verified identity provider information. This endpoint is useful for cases where we can't, such as missing or unverified provider information.

        Fields:
          - provider: The OAuth provider's name.
          - user_id: The unique ID of a specific User.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "provider": provider,
        }
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/oauth/attach", data)
        res = await self.async_client.post(url, data, headers)
        return AttachResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        token: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticate a User given a `token`. This endpoint verifies that the user completed the OAuth flow by verifying that the token is valid and hasn't expired. To initiate a Stytch session for the user while authenticating their OAuth token, include `session_duration_minutes`; a session with the identity provider, e.g. Google or Facebook, will always be initiated upon successful authentication.

        Fields:
          - token: The OAuth `token` from the `?token=` query parameter in the URL.

              The redirect URL will look like `https://example.com/authenticate?stytch_token_type=oauth&token=rM_kw42CWBhsHLF62V75jELMbvJ87njMe3tFVj7Qupu7`

              In the redirect URL, the `stytch_token_type` will be `oauth`. See [here](/workspace-management/redirect-urls) for more detail.
          - session_token: Reuse an existing session instead of creating a new one. If you provide us with a `session_token`, then we'll update the session represented by this session token with this OAuth factor. If this `session_token` belongs to a different user than the OAuth token, the session_jwt will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: Reuse an existing session instead of creating a new one. If you provide us with a `session_jwt`, then we'll update the session represented by this JWT with this OAuth factor. If this `session_jwt` belongs to a different user than the OAuth token, the session_jwt will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
          - code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "token": token,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            data["code_verifier"] = code_verifier

        url = self.api_base.url_for("/v1/oauth/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        token: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticate a User given a `token`. This endpoint verifies that the user completed the OAuth flow by verifying that the token is valid and hasn't expired. To initiate a Stytch session for the user while authenticating their OAuth token, include `session_duration_minutes`; a session with the identity provider, e.g. Google or Facebook, will always be initiated upon successful authentication.

        Fields:
          - token: The OAuth `token` from the `?token=` query parameter in the URL.

              The redirect URL will look like `https://example.com/authenticate?stytch_token_type=oauth&token=rM_kw42CWBhsHLF62V75jELMbvJ87njMe3tFVj7Qupu7`

              In the redirect URL, the `stytch_token_type` will be `oauth`. See [here](/workspace-management/redirect-urls) for more detail.
          - session_token: Reuse an existing session instead of creating a new one. If you provide us with a `session_token`, then we'll update the session represented by this session token with this OAuth factor. If this `session_token` belongs to a different user than the OAuth token, the session_jwt will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: Reuse an existing session instead of creating a new one. If you provide us with a `session_jwt`, then we'll update the session represented by this JWT with this OAuth factor. If this `session_jwt` belongs to a different user than the OAuth token, the session_jwt will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
          - code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "token": token,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            data["code_verifier"] = code_verifier

        url = self.api_base.url_for("/v1/oauth/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)
