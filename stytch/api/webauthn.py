from typing import Dict, List, Optional

from .base import Base

class WebAuthn(Base):
    @property
    def webauthn_url(self):
        return self.get_url("webauthn")

    def register_start(
        self,
        user_id: str,
        domain: str,
        user_agent: Optional[str] = None,
        authenticator_type: Optional[str] = None,
    ):
        data = {
            "user_id": user_id,
            "domain": domain,
        }
        if user_agent:
            data["user_agent"] = user_agent
        if authenticator_type:
            data["authenticator_type"] = authenticator_type

        return self._post(
            "{0}/register/start".format(
                self.webauthn_url,
            ),
            data=data,
        )

    def register(
        self,
        user_id: str,
        public_key_credential: str,
    ):
        data = {
            "user_id": user_id,
            "public_key_credential": public_key_credential,
        }

        return self._post(
            "{0}/register".format(
                self.webauthn_url,
            ),
            data=data,
        )

    def authenticate_start(
        self,
        user_id: str,
        domain: str,
    ):
        data = {
            "user_id": user_id,
            "domain": domain,
        }

        return self._post(
            "{0}/authenticate/start".format(
                self.webauthn_url,
            ),
            data=data,
        )

    def authenticate(
        self,
        public_key_credential: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
    ):
        data = {
            "public_key_credential": public_key_credential,
        }
        if session_token:
            data["session_token"] = session_token
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes

        return self._post(
            "{0}/authenticate".format(
                self.webauthn_url,
            ),
            data=data,
        )
