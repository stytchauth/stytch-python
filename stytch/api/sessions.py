from typing import Any, Dict, List, Optional, cast
from typing_extensions import TypedDict
import time

import jwt

from .base import _validate_attributes, Base
from .error import ClientError


class JWTInvalidError(ClientError):
    def __init__(self, message: str, cause: Exception = None):
        super().__init__("jwt_invalid", message, cause)


class JWTTooOldError(ClientError):
    def __init__(self, message: str, cause: Exception = None):
        super().__init__("jwt_too_old", message, cause)


_session_claim = "https://stytch.com/session"

SessionClaim = TypedDict(
    "SessionClaim",
    {
        "id": str,
        "started_at": str,
        "last_accessed_at": str,
        "attributes": Dict[str, str],
        "authentication_factors": List[Dict[str, Any]],
    },
)


class Sessions(Base):
    def __init__(self, client, jwks_client):
        super().__init__(client)

        self._jwks_client = jwks_client
        self._jwt_audience = client.project_id
        self._jwt_issuer = "stytch.com/" + client.project_id

    @property
    def sessions_url(self):
        return self.get_url("sessions")

    def get(
        self,
        user_id: str,
    ):
        query_params = {
            "user_id": user_id,
        }
        return self._get(self.sessions_url, query_params)

    def authenticate(
        self,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
    ):
        data: Dict[str, Any] = {}

        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes

        return self._post(
            "{0}/authenticate".format(self.sessions_url),
            data=data,
        )

    def authenticate_jwt(
        self,
        session_jwt: str,
        *,
        max_token_age_seconds: Optional[int] = None,
    ):
        """Parse a JWT and verify the signature, preferring local verification over remote.

        If max_token_age_seconds is set, remote verification will be forced if the JWT was issued
        at (based on the "iat" claim) more than that many seconds ago.

        To force remote validation for all tokens, set max_token_age_seconds to zero or use the
        authenticate method instead.
        """
        try:
            session = self.authenticate_jwt_local(
                session_jwt,
                max_token_age_seconds=max_token_age_seconds,
            )
            return {
                "session": session,
                "session_jwt": session_jwt,
            }
        except Exception as e:
            # JWT could not be verified locally. Check with the Stytch API.
            return self.authenticate(session_jwt=session_jwt).json()

    def authenticate_jwt_local(
        self,
        session_jwt: str,
        *,
        max_token_age_seconds: Optional[int] = None,
        leeway: int = 0,
    ):
        """Parse a JWT and verify the signature locally (without calling /authenticate in the API).

        If max_token_age_seconds is set, this will return an error if the JWT was issued (based on
        the "iat" claim) more than maxTokenAge seconds ago.

        If max_token_age_seconds is explicitly set to zero, all tokens will be considered too old,
        even if they are otherwise valid.

        The value for leeway is the maximum allowable difference in seconds when comparing
        timestamps. It defaults to zero.
        """
        now = time.time()

        signing_key = self._jwks_client.get_signing_key_from_jwt(session_jwt)

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
            audience=self._jwt_audience,
            issuer=self._jwt_issuer,
            leeway=leeway,
            # The max_token_age_seconds value is applied after decoding.
        )

        if max_token_age_seconds is not None:
            iat = payload["iat"]
            if now - iat >= max_token_age_seconds:
                message = "JWT was issued at {}, more than {} seconds ago".format(
                    iat, max_token_age_seconds
                )
                raise JWTTooOldError(message)

        # Unpack the session claim to match the detached session format.
        claim = cast(SessionClaim, payload[_session_claim])
        return {
            "user_id": payload["sub"],
            "expires_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime(payload["exp"])
            ),
            "session_id": claim["id"],
            "attributes": claim["attributes"],
            "authentication_factors": claim["authentication_factors"],
            "started_at": claim["started_at"],
            "last_accessed_at": claim["last_accessed_at"],
        }

    def revoke(
        self,
        session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ):
        data = {}
        if session_id:
            data["session_id"] = session_id
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt

        return self._post(
            "{0}/revoke".format(self.sessions_url),
            data=data,
        )

    def jwks(self, project_id: str):
        return self._get("{0}/jwks/{1}".format(self.sessions_url, project_id))
