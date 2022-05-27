from typing import Any, Dict, Optional

from .base import _validate_attributes, Base

class MagicLinks(Base):
    def __init__(self, client):
        super().__init__(client)
        self.email = Email(client)

    @property
    def magic_link_url(self):
        return self.get_url("magic_links")

    def create(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        data: Dict[str, Any] = {
            "user_id": user_id,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes
        return self._post(
            self.magic_link_url,
            data=data,
        )

    def authenticate(
        self,
        token: str,
        attributes: Optional[Dict] = None,
        options: Optional[Dict] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        code_verifier: Optional[str] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        if options:
            options = self._validate_options(options)

        data: Dict[str, Any] = {
            "token": token,
        }
        if attributes:
            data["attributes"] = attributes
        if options:
            data["options"] = options

        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if code_verifier:
            data["code_verifier"] = code_verifier

        return self._post(
            "{0}/authenticate".format(self.magic_link_url),
            data=data,
        )

class Email(Base):
    @property
    def magic_link_url(self):
        return self.get_url("magic_links")

    def send(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        code_challenge: Optional[str] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        data: Dict[str, Any] = {
            "email": email,
            "attributes": attributes,
        }
        if login_magic_link_url:
            data["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url:
            data["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes:
            data["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge:
            data["code_challenge"] = code_challenge

        return self._post(
            "{0}/email/send".format(
                self.magic_link_url,
            ),
            data=data,
        )

    def login_or_create(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False,
        code_challenge: Optional[str] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        data: Dict[str, Any] = {
           "email": email,
           "attributes": attributes,
           "create_user_as_pending": create_user_as_pending,
        }
        if login_magic_link_url:
            data["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url:
            data["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes:
            data["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge:
            data["code_challenge"] = code_challenge

        return self._post(
            "{0}/email/login_or_create".format(
                self.magic_link_url,
            ),
            data=data,
        )

    def invite(
        self,
        email: str,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        middle_name: Optional[str] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        data: Dict[str, Any] = {
            "email": email,
            "attributes": attributes,
            "name": {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
            },
        }
        if invite_magic_link_url:
            data["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes:
            data["invite_expiration_minutes"] = invite_expiration_minutes

        return self._post(
            "{0}/email/invite".format(
                self.magic_link_url,
            ),
            data=data,
        )

    def revoke_invite(
        self,
        email: str,
    ):
        return self._post(
            "{0}/email/revoke_invite".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
            },
        )
