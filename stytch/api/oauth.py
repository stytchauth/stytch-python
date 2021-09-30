from typing import Dict, Optional
from enum import Enum

from .base import _validate_attributes, Base

class SessionManagementType(Enum):
    IDP = "idp"
    STYTCH = "stytch"
    NONE = "none"

class OAuth(Base):
    def __init__(self, client):
        super().__init__(client)

    @property
    def oauth_url(self):
        return self.get_url("oauth")

    def authenticate(
        self,
        token: str,
        session_management_type: Optional[SessionManagementType] = None,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
    ):

        data={
            "token": token,
        }
        if session_management_type:
            data["session_management_type"] = session_management_type
        if session_token:
            data["session_token"] = session_token
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes

        return self._post(
            "{0}/authenticate".format(self.oauth_url),
            data=data,
        )
