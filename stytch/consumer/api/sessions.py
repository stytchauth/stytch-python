# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

import jwt

from stytch.consumer.models.sessions import (
    AuthenticateJWTLocalResponse,
    AuthenticateResponse,
    GetJWKSResponse,
    GetResponse,
    MigrateResponse,
    RevokeResponse,
    Session,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.shared import jwt_helpers


class Sessions:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
        jwks_client: jwt.PyJWKClient,
        project_id: str,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.jwks_client = jwks_client
        self.project_id = project_id

    def get(
        self,
        user_id: str,
    ) -> GetResponse:
        """List all active Sessions for a given `user_id`. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.

        Fields:
          - user_id: The `user_id` to get active Sessions for.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/sessions", data)
        res = self.sync_client.get(url, data, headers)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        user_id: str,
    ) -> GetResponse:
        """List all active Sessions for a given `user_id`. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.

        Fields:
          - user_id: The `user_id` to get active Sessions for.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/sessions", data)
        res = await self.async_client.get(url, data, headers)
        return GetResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticate a session token or session JWT and retrieve associated session data. If `session_duration_minutes` is included, update the lifetime of the session to be that many minutes from now. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`. This endpoint requires exactly one `session_jwt` or `session_token` as part of the request. If both are included, you will receive a `too_many_session_arguments` error.

        You may provide a JWT that needs to be refreshed and is expired according to its `exp` claim. A new JWT will be returned if both the signature and the underlying Session are still valid. See our [How to use Stytch Session JWTs](https://stytch.com/docs/guides/sessions/using-jwts) guide for more information.

        Fields:
          - session_token: The session token to authenticate.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now; minimum of 5 and a maximum of 527040 minutes (366 days). Note that a successful authentication will continue to extend the session this many minutes.
          - session_jwt: The JWT to authenticate. You may provide a JWT that has expired according to its `exp` claim and needs to be refreshed. If the signature is valid and the underlying session is still active then Stytch will return a new JWT.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/sessions/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticate a session token or session JWT and retrieve associated session data. If `session_duration_minutes` is included, update the lifetime of the session to be that many minutes from now. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`. This endpoint requires exactly one `session_jwt` or `session_token` as part of the request. If both are included, you will receive a `too_many_session_arguments` error.

        You may provide a JWT that needs to be refreshed and is expired according to its `exp` claim. A new JWT will be returned if both the signature and the underlying Session are still valid. See our [How to use Stytch Session JWTs](https://stytch.com/docs/guides/sessions/using-jwts) guide for more information.

        Fields:
          - session_token: The session token to authenticate.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now; minimum of 5 and a maximum of 527040 minutes (366 days). Note that a successful authentication will continue to extend the session this many minutes.
          - session_jwt: The JWT to authenticate. You may provide a JWT that has expired according to its `exp` claim and needs to be refreshed. If the signature is valid and the underlying session is still active then Stytch will return a new JWT.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/sessions/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)

    def revoke(
        self,
        session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> RevokeResponse:
        """Revoke a Session, immediately invalidating all of its session tokens. You can revoke a session in three ways: using its ID, or using one of its session tokens, or one of its JWTs. This endpoint requires exactly one of those to be included in the request. It will return an error if multiple are present.

        Fields:
          - session_id: The `session_id` to revoke.
          - session_token: The session token to revoke.
          - session_jwt: A JWT for the session to revoke.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}
        if session_id is not None:
            data["session_id"] = session_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/sessions/revoke", data)
        res = self.sync_client.post(url, data, headers)
        return RevokeResponse.from_json(res.response.status_code, res.json)

    async def revoke_async(
        self,
        session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> RevokeResponse:
        """Revoke a Session, immediately invalidating all of its session tokens. You can revoke a session in three ways: using its ID, or using one of its session tokens, or one of its JWTs. This endpoint requires exactly one of those to be included in the request. It will return an error if multiple are present.

        Fields:
          - session_id: The `session_id` to revoke.
          - session_token: The session token to revoke.
          - session_jwt: A JWT for the session to revoke.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}
        if session_id is not None:
            data["session_id"] = session_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/sessions/revoke", data)
        res = await self.async_client.post(url, data, headers)
        return RevokeResponse.from_json(res.response.status, res.json)

    def migrate(
        self,
        session_token: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        """Migrate a session from an external OIDC compliant endpoint. Stytch will call the external UserInfo endpoint defined in your Stytch Project settings in the [Dashboard](https://stytch.com/docs/dashboard), and then perform a lookup using the `session_token`. If the response contains a valid email address, Stytch will attempt to match that email address with an existing User and create a Stytch Session. You will need to create the user before using this endpoint.

        Fields:
          - session_token: The authorization token Stytch will pass in to the external userinfo endpoint.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "session_token": session_token,
        }
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/sessions/migrate", data)
        res = self.sync_client.post(url, data, headers)
        return MigrateResponse.from_json(res.response.status_code, res.json)

    async def migrate_async(
        self,
        session_token: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        """Migrate a session from an external OIDC compliant endpoint. Stytch will call the external UserInfo endpoint defined in your Stytch Project settings in the [Dashboard](https://stytch.com/docs/dashboard), and then perform a lookup using the `session_token`. If the response contains a valid email address, Stytch will attempt to match that email address with an existing User and create a Stytch Session. You will need to create the user before using this endpoint.

        Fields:
          - session_token: The authorization token Stytch will pass in to the external userinfo endpoint.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "session_token": session_token,
        }
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/sessions/migrate", data)
        res = await self.async_client.post(url, data, headers)
        return MigrateResponse.from_json(res.response.status, res.json)

    def get_jwks(
        self,
        project_id: str,
    ) -> GetJWKSResponse:
        """Get the JSON Web Key Set (JWKS) for a project.

        JWKS are rotated every ~6 months. Upon rotation, new JWTs will be signed using the new key, and both keys will be returned by this endpoint for a period of 1 month.

        JWTs have a set lifetime of 5 minutes, so there will be a 5 minute period where some JWTs will be signed by the old JWKS, and some JWTs will be signed by the new JWKS. The correct JWKS to use for validation is determined by matching the `kid` value of the JWT and JWKS.

        If you're using one of our [backend SDKs](https://stytch.com/docs/sdks), the JWKS rotation will be handled for you.

        If you're using your own JWT validation library, many have built-in support for JWKS rotation, and you'll just need to supply this API endpoint. If not, your application should decide which JWKS to use for validation by inspecting the `kid` value.

        See our [How to use Stytch Session JWTs](https://stytch.com/docs/guides/sessions/using-jwts) guide for more information.

        Fields:
          - project_id: The `project_id` to get the JWKS for.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.url_for("/v1/sessions/jwks/{project_id}", data)
        res = self.sync_client.get(url, data, headers)
        return GetJWKSResponse.from_json(res.response.status_code, res.json)

    async def get_jwks_async(
        self,
        project_id: str,
    ) -> GetJWKSResponse:
        """Get the JSON Web Key Set (JWKS) for a project.

        JWKS are rotated every ~6 months. Upon rotation, new JWTs will be signed using the new key, and both keys will be returned by this endpoint for a period of 1 month.

        JWTs have a set lifetime of 5 minutes, so there will be a 5 minute period where some JWTs will be signed by the old JWKS, and some JWTs will be signed by the new JWKS. The correct JWKS to use for validation is determined by matching the `kid` value of the JWT and JWKS.

        If you're using one of our [backend SDKs](https://stytch.com/docs/sdks), the JWKS rotation will be handled for you.

        If you're using your own JWT validation library, many have built-in support for JWKS rotation, and you'll just need to supply this API endpoint. If not, your application should decide which JWKS to use for validation by inspecting the `kid` value.

        See our [How to use Stytch Session JWTs](https://stytch.com/docs/guides/sessions/using-jwts) guide for more information.

        Fields:
          - project_id: The `project_id` to get the JWKS for.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.url_for("/v1/sessions/jwks/{project_id}", data)
        res = await self.async_client.get(url, data, headers)
        return GetJWKSResponse.from_json(res.response.status, res.json)

    # MANUAL(authenticate_jwt)(SERVICE_METHOD)
    # ADDIMPORT: from typing import Any, Dict, Optional
    # ADDIMPORT: import jwt
    # ADDIMPORT: import time
    # ADDIMPORT: from stytch.consumer.models.sessions import AuthenticateJWTLocalResponse
    def authenticate_jwt(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> Optional[AuthenticateJWTLocalResponse]:
        """Parse a JWT and verify the signature, preferring local verification
        over remote.

        If max_token_age_seconds is set, remote verification will be forced if the
        JWT was issued at (based on the "iat" claim) more than that many seconds ago.

        To force remote validation for all tokens, set max_token_age_seconds to
        zero or use the authenticate method instead.
        """
        # Return the local_result if available, otherwise call the Stytch API
        local_resp = self.authenticate_jwt_local(
            session_jwt=session_jwt,
            max_token_age_seconds=max_token_age_seconds,
        )
        if local_resp is not None:
            return AuthenticateJWTLocalResponse.from_json(
                status_code=200,
                json={
                    "session": local_resp,
                    "session_jwt": session_jwt,
                    "status_code": 200,
                    "request_id": "",
                },
            )
        else:
            authenticate_response = self.authenticate(
                session_custom_claims=session_custom_claims, session_jwt=session_jwt
            )
            return AuthenticateJWTLocalResponse.from_json(
                status_code=authenticate_response.status_code,
                json={
                    "session": authenticate_response.session,
                    "session_jwt": authenticate_response.session_jwt,
                    "status_code": authenticate_response.status_code,
                    "request_id": authenticate_response.request_id,
                },
            )

    async def authenticate_jwt_async(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> Optional[AuthenticateJWTLocalResponse]:
        """Parse a JWT and verify the signature, preferring local verification
        over remote.

        If max_token_age_seconds is set, remote verification will be forced if the
        JWT was issued at (based on the "iat" claim) more than that many seconds ago.

        To force remote validation for all tokens, set max_token_age_seconds to
        zero or use the authenticate method instead.
        """
        # Return the local_result if available, otherwise call the Stytch API
        local_token = self.authenticate_jwt_local(
            session_jwt=session_jwt,
            max_token_age_seconds=max_token_age_seconds,
        )
        if local_token is not None:
            return AuthenticateJWTLocalResponse.from_json(
                status_code=200,
                json={
                    "session": local_token,
                    "session_jwt": session_jwt,
                    "status_code": 200,
                    "request_id": "",
                },
            )
        else:
            authenticate_response = await self.authenticate_async(
                session_custom_claims=session_custom_claims, session_jwt=session_jwt
            )
            return AuthenticateJWTLocalResponse.from_json(
                status_code=authenticate_response.status_code,
                json={
                    "session": authenticate_response.session,
                    "session_jwt": authenticate_response.session_jwt,
                    "status_code": authenticate_response.status_code,
                    "request_id": authenticate_response.request_id,
                },
            )

    # ENDMANUAL(authenticate_jwt)

    # MANUAL(authenticate_jwt_local)(SERVICE_METHOD)
    # ADDIMPORT: from stytch.consumer.models.sessions import Session
    # ADDIMPORT: from stytch.shared import jwt_helpers
    def authenticate_jwt_local(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        leeway: int = 0,
    ) -> Optional[Session]:
        _session_claim = "https://stytch.com/session"
        generic_claims = jwt_helpers.authenticate_jwt_local(
            project_id=self.project_id,
            jwks_client=self.jwks_client,
            jwt=session_jwt,
            max_token_age_seconds=max_token_age_seconds,
            leeway=leeway,
        )
        if generic_claims is None:
            return None

        claim = generic_claims.untyped_claims[_session_claim]
        custom_claims = {
            k: v
            for k, v in generic_claims.untyped_claims.items()
            if k != _session_claim
        }

        # For JWTs that include it, prefer the inner expires_at claim.
        expires_at = claim.get("expires_at", generic_claims.reserved_claims["exp"])

        return Session(
            attributes=claim["attributes"],
            authentication_factors=claim["authentication_factors"],
            expires_at=expires_at,
            last_accessed_at=claim["last_accessed_at"],
            session_id=claim["id"],
            started_at=claim["started_at"],
            user_id=generic_claims.reserved_claims["sub"],
            custom_claims=custom_claims,
        )

    # ENDMANUAL(authenticate_jwt_local)
