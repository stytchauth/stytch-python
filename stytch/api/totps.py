from typing import Optional

from .base import Base


class TOTPs(Base):
    def __init__(self, client):
        super().__init__(client)

    @property
    def totps_url(self):
        return self.get_url("totps")

    def create(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
    ):
        data={
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
        session_duration_minutes: Optional[int] = None,
    ):
        data={
            "user_id": user_id,
            "totp_code": totp_code,
        }
        if session_token:
            data["session_token"] = session_token
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        return self._post(
            "{0}/authenticate".format(self.totps_url),
            data=data,
        )

    def recovery_codes(
        self,
        user_id: str,
    ):
        data={
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
    ):
        data={
            "user_id": user_id,
            "recovery_code": recovery_code,
        }
        return self._post(
            "{0}/recover".format(self.totps_url),
            data=data,
        )
