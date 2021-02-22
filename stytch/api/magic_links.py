from typing import Dict, Optional

from .base import Base


class MagicLinks(Base):
    @property
    def magic_link_url(self):
        return self.get_url("magic_links")

    def _validate_attributes(self, attributes: Dict[str, str]) -> Dict[str, str]:
        if not attributes:
            return attributes
        default_attributes = {"ip_address": "", "user_agent": ""}

        if attributes.get("ip_address"):
            default_attributes.update({"ip_address": attributes["ip_address"]})
        if attributes.get("user_agent"):
            default_attributes.update({"user_agent": attributes["user_agent"]})

        return default_attributes

    def _validate_match_attributes(self, attributes: Dict[str, str]) -> Dict[str, str]:
        if not attributes:
            return attributes

        default_attributes = {"ip_address_match": "", "user_agent_match": ""}
        if attributes.get("ip_address_match"):
            default_attributes.update(
                {"ip_address_match": attributes["ip_address_match"]}
            )
        if attributes.get("user_agent_match"):
            default_attributes.update(
                {"user_agent_match": attributes["user_agent_match"]}
            )

        return default_attributes

    def authenticate(self, token: str, options: Dict = None):
        options = self._validate_match_attributes(options)
        return self._post(
            "{0}/{1}/authenticate".format(self.magic_link_url, token),
            data={"options": options},
        )

    def send(
        self,
        method_id: str,
        user_id: str,
        magic_link_url: str,
        expiration_minutes: int = 10,
        attributes: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        return self._post(
            "{0}/send".format(
                self.magic_link_url,
            ),
            data={
                "method_id": method_id,
                "user_id": user_id,
                "magic_link_url": magic_link_url,
                "expiration_minutes": expiration_minutes,
                "attributes": attributes,
            },
        )

    def send_by_email(
        self,
        email: str,
        magic_link_url: str,
        expiration_minutes: int = 10,
        attributes: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        return self._post(
            "{0}/send_by_email".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
                "magic_link_url": magic_link_url,
                "expiration_minutes": expiration_minutes,
                "attributes": attributes,
            },
        )

    def login_or_create(
        self,
        email: str,
        login_magic_link_url: str,
        signup_magic_link_url: str,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        return self._post(
            "{0}/login_or_create".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
                "login_magic_link_url": login_magic_link_url,
                "signup_magic_link_url": signup_magic_link_url,
                "login_expiration_minutes": login_expiration_minutes,
                "signup_expiration_minutes": signup_expiration_minutes,
                "attributes": attributes,
            },
        )

    def invite_by_email(
        self,
        email: str,
        magic_link_url: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        return self._post(
            "{0}/invite_by_email".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
                "magic_link_url": magic_link_url,
                "expiration_minutes": expiration_minutes,
                "attributes": attributes,
            },
        )

    def revoke_invite_by_email(
        self,
        email: str,
    ):
        attributes = self._validate_attributes(attributes)
        return self._post(
            "{0}/revoke_invite".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
            },
        )
