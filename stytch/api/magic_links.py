from typing import Dict, Optional

from .base import Base

class MagicLinks(Base):
    @property
    def magic_link_url(self):
        return self.get_url("magic_links")

    def authenticate(
        self,
        token: str,
        attributes: Optional[Dict] = None,
        options: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        options = self._validate_options(options)

        data={}
        if attributes:
            data["attributes"] = attributes
        if options:
            data["options"] = options
        return self._post(
            "{0}/{1}/authenticate".format(self.magic_link_url, token),
            data=data,
        )

    def send_by_email(
        self,
        email: str,
        login_magic_link_url: str,
        signup_magic_link_url: str,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        data = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "attributes": attributes,
        }
        if login_expiration_minutes:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes:
            data["signup_expiration_minutes"] = signup_expiration_minutes

        return self._post(
            "{0}/send_by_email".format(
                self.magic_link_url,
            ),
            data=data,
        )

    def login_or_create(
        self,
        email: str,
        login_magic_link_url: str,
        signup_magic_link_url: str,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False,
    ):
        attributes = self._validate_attributes(attributes)
        data = {
           "email": email,
           "login_magic_link_url": login_magic_link_url,
           "signup_magic_link_url": signup_magic_link_url,
           "attributes": attributes,
           "create_user_as_pending": create_user_as_pending,
       }

        if login_expiration_minutes:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes:
            data["signup_expiration_minutes"] = signup_expiration_minutes

        return self._post(
            "{0}/login_or_create".format(
                self.magic_link_url,
            ),
            data=data,
        )

    def invite_by_email(
        self,
        email: str,
        invite_magic_link_url: str,
        invite_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        middle_name: Optional[str] = None,
    ):
        attributes = self._validate_attributes(attributes)
        data = {
            "email": email,
            "invite_magic_link_url": invite_magic_link_url,
            "attributes": attributes,
            "name": {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
            },
        }

        if invite_expiration_minutes:
            data["invite_expiration_minutes"] = invite_expiration_minutes

        return self._post(
            "{0}/invite_by_email".format(
                self.magic_link_url,
            ),
            data=data,
        )

    def revoke_invite_by_email(
        self,
        email: str,
    ):
        return self._post(
            "{0}/revoke_invite".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
            },
        )
