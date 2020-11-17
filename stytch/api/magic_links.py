from typing import Dict, Optional

from .base import Base


class MagicLinks(Base):
    @property
    def magic_link_url(self):
        return self.get_url("magic_links")

    def _validate_attributes(self, attributes: Dict[str, str]) -> bool:
        if not attributes:
            return True
        return self._validate_fields(
            set(["ip_address", "user_agent"]), set(attributes.keys())
        )

    def _validate_match_attributes(self, attributes: Dict[str, str]) -> bool:
        if not attributes:
            return True
        return self._validate_fields(
            set(["ip_address_match", "user_agent_match"]), set(attributes.keys())
        )

    def authenticate(self, token: str, options: Dict = None):
        if not self._validate_match_attributes(options):
            raise Exception("invalid arguments")
        return self._post(
            "{0}/{1}/authenticate".format(self.magic_link_url, token),
            data={"options": options},
        )

    def send(
        self,
        method_id: str,
        user_id: str,
        magic_link_url: str,
        expiration_minutes: float = 10.0,
        template_id: str = None,
        attributes: Dict = {},
    ):
        if not self._validate_attributes(attributes):
            raise Exception("invalid arguments")
        return self._post(
            "{0}/send".format(
                self.magic_link_url,
            ),
            data={
                "method_id": method_id,
                "user_id": user_id,
                "magic_link_url": magic_link_url,
                "expiration_minutes": expiration_minutes,
                "template_id": template_id,
                "attributes": attributes,
            },
        )

    def send_by_email(
        self,
        email: str,
        magic_link_url: str,
        expiration_minutes: float = 10.0,
        template_id: Optional[str] = None,
        attributes: Dict = {},
    ):
        if not self._validate_attributes(attributes):
            raise Exception("invalid arguments")
        return self._post(
            "{0}/send_by_email".format(
                self.magic_link_url,
            ),
            data={
                "email": email,
                "magic_link_url": magic_link_url,
                "expiration_minutes": expiration_minutes,
                "template_id": template_id,
                "attributes": attributes,
            },
        )
