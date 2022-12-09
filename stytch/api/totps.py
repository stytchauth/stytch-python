from typing import TYPE_CHECKING, Any, Dict, Optional

import requests

from stytch.api.base import Base

if TYPE_CHECKING:
    from stytch.client import Client


class TOTPs(Base):
    def __init__(self, client: "Client") -> None:
        super().__init__(client)

    @property
    def totps_url(self) -> str:
        return self.get_url("totps")

    def create(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        return self._post(
            self.totps_url,
            data=data,
        )

    def authenticate(
        self,
        user_id: str,
        totp_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "totp_code": totp_code,
        }
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims:
            data["session_custom_claims"] = session_custom_claims
        return self._post(
            "{0}/authenticate".format(self.totps_url),
            data=data,
        )

    def recovery_codes(
        self,
        user_id: str,
    ) -> requests.Response:
        data = {
            "user_id": user_id,
        }
        return self._post(
            "{0}/recovery_codes".format(self.totps_url),
            data=data,
        )

    def recover(
        self,
        user_id: str,
        recovery_code: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        data: Dict[str, Any] = {
            "user_id": user_id,
            "recovery_code": recovery_code,
        }
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims:
            data["session_custom_claims"] = session_custom_claims
        return self._post(
            "{0}/recover".format(self.totps_url),
            data=data,
        )
