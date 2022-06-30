from enum import Enum
from typing import Any, Dict, Optional

from .base import Base, _validate_attributes


class OAuth(Base):
    def __init__(self, client):
        super().__init__(client)

    @property
    def oauth_url(self):
        return self.get_url("oauth")

    def authenticate(
        self,
        token: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ):

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
