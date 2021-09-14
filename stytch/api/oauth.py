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
    ):

        data={
            "token": token,
        }
        if session_management_type:
            data["session_management_type"] = session_management_type

        return self._post(
            "{0}/authenticate".format(self.oauth_url),
            data=data,
        )
