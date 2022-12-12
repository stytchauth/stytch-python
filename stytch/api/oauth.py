from typing import TYPE_CHECKING, Any, Dict, Optional

import requests

from stytch.api.base import Base

if TYPE_CHECKING:
    from stytch.client import Client


class OAuth(Base):
    def __init__(self, client: "Client") -> None:
        super().__init__(client)

    @property
    def oauth_url(self) -> str:
        return self.get_url("oauth")

    def authenticate(
        self,
        token: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> requests.Response:

        data: Dict[str, Any] = {
            "token": token,
        }

        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims:
            data["session_custom_claims"] = session_custom_claims
        if code_verifier:
            data["code_verifier"] = code_verifier

        return self._post(
            "{0}/authenticate".format(self.oauth_url),
            data=data,
        )

    def attach(
        self,
        provider: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> requests.Response:
        """Send a /v1/oauth/attach request.

        Exactly one of user_id, session_token, or session_jwt is required.
        """

        data: Dict[str, Any] = {
            "provider": provider,
        }

        if user_id:
            data["user_id"] = user_id
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt

        return self._post(
            "{0}/attach".format(self.oauth_url),
            data=data,
        )
