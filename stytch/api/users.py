from typing import Dict

from .base import Base


class Users(Base):
    @property
    def user_url(self):
        return self.get_url("users")

    def _validate_attributes(self, attributes: Dict[str, str]) -> bool:
        if not attributes:
            return False
        FIELDS = set(["ip_address", "user_agent"])
        if len(FIELDS.union(set(attributes.keys()))) > len(FIELDS):
            raise Exception("Unknown argument in user attributes")

        return True

    def create(
        self,
        email: str,
        first_name: str,
        last_name: str,
        attributes: Dict[str, str] = None,
    ):
        data = {"email": email, "first_name": first_name, "last_name": last_name}
        if self._validate_attributes(attributes):
            data.update(attributes)
        return self._post("{0}".format(self.user_url), data)

    def get(self, user_id: str):
        return self._get("{0}/{1}".format(self.user_url, user_id))

    def delete(self, user_id: str):
        return self._delete("{0}/{1}".format(self.user_url, user_id))

    def update(
        self, email: str, first_name: str, last_name: str, attributes: Dict[str, str]
    ):
        data = {}
        if email:
            data.update({"email": email})
        if first_name:
            data.update({"first_name": first_name})
        if last_name:
            data.update({"last_name": last_name})
        if self._validate_attributes(attributes):
            data.update({attributes: attributes})

        return self._put("{0}".format(self.user_url), data)
