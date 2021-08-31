from typing import Dict, Optional

from .base import _validate_attributes, Base

class Sessions(Base):
    def __init__(self, client):
        super().__init__(client)

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
        session_token: str,
        session_duration_minutes: Optional[int] = None,
    ):
        data = {
            "session_token": session_token,
        }
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes

        return self._post(
            "{0}/authenticate".format(self.sessions_url),
            data=data,
        )

    def revoke(
        self,
        session_id: Optional[str] = None,
        session_token: Optional[str] = None,
    ):
        data = {}
        if session_id:
            data["session_id"] = session_id
        if session_token:
            data["session_token"] = session_token

        return self._post(
            "{0}/revoke".format(self.sessions_url),
            data=data,
        )
