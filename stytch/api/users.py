from typing import Dict, Optional

from .base import Base


class Users(Base):
    @property
    def user_url(self):
        return self.get_url("users")

    def _validate_attributes(self, attributes: Dict[str, str]) -> bool:
        if not attributes:
            return True
        return self._validate_fields(
            set(["ip_address", "user_agent"]), set(attributes.keys())
        )

    def create(
        self,
        email: str,
        first_name: str = None,
        last_name: str = None,
        middle_name: str = None,
        attributes: Dict[str, str] = {},
    ):
        data = {
            "email": email,
            "name": {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
            },
        }
        if attributes and self._validate_attributes(attributes):
            data.update(attributes)
        return self._post("{0}".format(self.user_url), data)

    def get(self, user_id: str):
        return self._get("{0}/{1}".format(self.user_url, user_id))

    def get_invited_users(
        self,
        limit: Optional[int] = None,
        starting_after_id: Optional[str] = None
    ):
        query_params = {}
        if limit:
            query_params.update({"limit": str(limit)})
        if starting_after_id:
            query_params.update({"starting_after_id": starting_after_id})

        return self._get("{0}/{1}".format(self.user_url, "invites"), query_params)

    def delete(self, user_id: str):
        return self._delete("{0}/{1}".format(self.user_url, user_id))

    def update(
        self,
        user_id: str,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        middle_name: Optional[str] = None,
        last_name: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = {},
    ):
        data = {}
        name = {}
        if email:
            data.update({"email": email})
        if first_name:
            name.update({"first_name": first_name})
        if middle_name:
            name.update({"middle_name": middle_name})
        if last_name:
            name.update({"last_name": last_name})
        if name:
            data.update({"name": name})
        if attributes and self._validate_attributes(attributes):
            data.update({"attributes": attributes})

        return self._put("{0}/{1}".format(self.user_url, user_id), data)

    def delete_email(self, user_id: str, email: str):
        return self._delete("{0}/{1}/emails/{2}".format(self.user_url, user_id, email))
