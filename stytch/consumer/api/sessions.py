# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import time
from typing import Any, Dict, Optional

import jwt

from stytch.consumer.models.sessions import (
    AuthenticateResponse,
    GetJWKSResponse,
    GetResponse,
    RevokeResponse,
    Session,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


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

    def get(
        self,
        user_id: str,
    ) -> GetResponse:
        """List all active Sessions for a given `user_id`. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.

        Fields:
          - user_id: The `user_id` to get active Sessions for.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/sessions", data)
        res = self.sync_client.get(url, data)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        user_id: str,
    ) -> GetResponse:
        """List all active Sessions for a given `user_id`. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.

        Fields:
          - user_id: The `user_id` to get active Sessions for.
        """  # noqa
        data: Dict[str, Any] = {
            "user_id": user_id,
        }

        url = self.api_base.url_for("/v1/sessions", data)
        res = await self.async_client.get(url, data)
        return GetResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticate a session token and retrieve associated session data. If `session_duration_minutes` is included, update the lifetime of the session to be that many minutes from now. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`. This endpoint requires exactly one `session_jwt` or `session_token` as part of the request. If both are included you will receive a `too_many_session_arguments` error.

        Fields:
          - session_token: The session token to authenticate.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now; minimum of 5 and a maximum of 527040 minutes (366 days). Note that a successful authentication will continue to extend the session this many minutes.
          - session_jwt: The JWT to authenticate. You may provide a JWT that has expired according to its `exp` claim and needs to be refreshed. If the signature is valid and the underlying session is still active then Stytch will return a new JWT.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
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
        res = self.sync_client.post(url, data)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticate a session token and retrieve associated session data. If `session_duration_minutes` is included, update the lifetime of the session to be that many minutes from now. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`. This endpoint requires exactly one `session_jwt` or `session_token` as part of the request. If both are included you will receive a `too_many_session_arguments` error.

        Fields:
          - session_token: The session token to authenticate.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now; minimum of 5 and a maximum of 527040 minutes (366 days). Note that a successful authentication will continue to extend the session this many minutes.
          - session_jwt: The JWT to authenticate. You may provide a JWT that has expired according to its `exp` claim and needs to be refreshed. If the signature is valid and the underlying session is still active then Stytch will return a new JWT.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
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
        res = await self.async_client.post(url, data)
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
        data: Dict[str, Any] = {}
        if session_id is not None:
            data["session_id"] = session_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/sessions/revoke", data)
        res = self.sync_client.post(url, data)
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
        data: Dict[str, Any] = {}
        if session_id is not None:
            data["session_id"] = session_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/sessions/revoke", data)
        res = await self.async_client.post(url, data)
        return RevokeResponse.from_json(res.response.status, res.json)

    def get_jwks(
        self,
        project_id: str,
    ) -> GetJWKSResponse:
        """Get the JSON Web Key Set (JWKS) for a Stytch Project.

        Fields:
          - project_id: The `project_id` to get the JWKS for.
        """  # noqa
        data: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.url_for("/v1/sessions/jwks/{project_id}", data)
        res = self.sync_client.get(url, data)
        return GetJWKSResponse.from_json(res.response.status_code, res.json)

    async def get_jwks_async(
        self,
        project_id: str,
    ) -> GetJWKSResponse:
        """Get the JSON Web Key Set (JWKS) for a Stytch Project.

        Fields:
          - project_id: The `project_id` to get the JWKS for.
        """  # noqa
        data: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.url_for("/v1/sessions/jwks/{project_id}", data)
        res = await self.async_client.get(url, data)
        return GetJWKSResponse.from_json(res.response.status, res.json)

    # MANUAL(authenticate_jwt)(SERVICE_METHOD)
    # ADDIMPORT: from typing import Any, Dict, Optional
    # ADDIMPORT: import jwt
    # ADDIMPORT: import time
    def authenticate_jwt(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> Optional[Session]:
        """Parse a JWT and verify the signature, preferring local verification
        over remote.

        If max_token_age_seconds is set, remote verification will be forced if the
        JWT was issued at (based on the "iat" claim) more than that many seconds ago.

        To force remote validation for all tokens, set max_token_age_seconds to
        zero or use the authenticate method instead.
        """
        # Return the local_result if available, otherwise call the Stytch API
        return (
            self.authenticate_jwt_local(
                session_jwt=session_jwt,
                max_token_age_seconds=max_token_age_seconds,
            )
            or self.authenticate(
                session_custom_claims=session_custom_claims, session_jwt=session_jwt
            ).session
        )

    async def authenticate_jwt_async(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> Optional[Session]:
        """Parse a JWT and verify the signature, preferring local verification
        over remote.

        If max_token_age_seconds is set, remote verification will be forced if the
        JWT was issued at (based on the "iat" claim) more than that many seconds ago.

        To force remote validation for all tokens, set max_token_age_seconds to
        zero or use the authenticate method instead.
        """
        # Return the local_result if available, otherwise call the Stytch API
        return (
            self.authenticate_jwt_local(
                session_jwt=session_jwt,
                max_token_age_seconds=max_token_age_seconds,
            )
            or (
                await self.authenticate_async(
                    session_custom_claims=session_custom_claims, session_jwt=session_jwt
                )
            ).session
        )

    # ENDMANUAL(authenticate_jwt)

    # MANUAL(authenticate_jwt_local)(SERVICE_METHOD)
    # ADDIMPORT: import time
    # ADDIMPORT: from stytch.consumer.models.sessions import Session
    def authenticate_jwt_local(
        self,
        session_jwt: str,
        max_token_age_seconds: Optional[int] = None,
        leeway: int = 0,
    ) -> Optional[Session]:
        """Parse a JWT and verify the signature locally
        (without calling /authenticate in the API).

        If max_token_age_seconds is set, this will return an error if the JWT was issued
        (based on the "iat" claim) more than maxTokenAge seconds ago.

        If max_token_age_seconds is explicitly set to zero, all tokens will be
        considered too old, even if they are otherwise valid.

        The value for leeway is the maximum allowable difference in seconds when
        comparing timestamps. It defaults to zero.
        """
        project_id = self.sync_client.project_id
        jwt_audience = project_id
        jwt_issuer = "stytch.com/{}".format(project_id)
        _session_claim = "https://stytch.com/session"

        now = time.time()

        signing_key = self.jwks_client.get_signing_key_from_jwt(session_jwt)

        # NOTE: The max_token_age_seconds value is applied after decoding.
        payload = jwt.decode(
            session_jwt,
            signing_key.key,
            algorithms=["RS256"],
            options={
                "require": ["aud", "iss", "exp", "iat", "nbf"],
                "verify_signature": True,
                "verify_aud": True,
                "verify_iss": True,
                "verify_exp": True,
                "verify_iat": True,
                "verify_nbf": True,
            },
            audience=jwt_audience,
            issuer=jwt_issuer,
            leeway=leeway,
        )

        if max_token_age_seconds is not None:
            iat = payload["iat"]
            if now - iat >= max_token_age_seconds:
                # JWT was issued too long ago, don't verify
                return None

        # Unpack the session claim to match the detached session format.
        claim = payload[_session_claim]

        # For JWTs that include it, prefer the inner expires_at claim.
        expires_at = claim.get("expires_at", payload["exp"])

        # Parse custom claims by taking everything other than the reserved claims
        reserved_claims = [
            "aud",
            "exp",
            "iat",
            "iss",
            "jti",
            "nbf",
            "sub",
            _session_claim,
        ]
        custom_claims = {k: v for k, v in payload.items() if k not in reserved_claims}

        return Session(
            attributes=claim["attributes"],
            authentication_factors=claim["authentication_factors"],
            expires_at=expires_at,
            last_accessed_at=claim["last_accessed_at"],
            session_id=claim["id"],
            started_at=claim["started_at"],
            user_id=payload["sub"],
            custom_claims=custom_claims,
        )

    # ENDMANUAL(authenticate_jwt_local)