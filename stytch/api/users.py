from typing import Dict, List, Optional

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
        email: str = None,
        phone_number: str = None,
        first_name: str = None,
        last_name: str = None,
        middle_name: str = None,
        create_user_as_pending: Optional[bool] = False,
        attributes: Dict[str, str] = {},
    ):
        data = {
            "email": email,
            "phone_number": phone_number,
            "name": {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
            },
            "create_user_as_pending": create_user_as_pending,
        }
        if attributes and self._validate_attributes(attributes):
            data.update({"attributes": attributes})
        return self._post("{0}".format(self.user_url), data)

    def get(self, user_id: str):
        return self._get("{0}/{1}".format(self.user_url, user_id))

    def get_pending(
        self,
        limit: Optional[int] = None,
        starting_after_id: Optional[str] = None
    ):
        query_params = {}
        if limit:
            query_params.update({"limit": str(limit)})
        if starting_after_id:
            query_params.update({"starting_after_id": starting_after_id})

        return self._get("{0}/{1}".format(self.user_url, "pending"), query_params)

    def delete(self, user_id: str):
        return self._delete("{0}/{1}".format(self.user_url, user_id))

    def update(
        self,
        user_id: str,
        emails: Optional[List[str]] = None,
        phone_numbers: Optional[List[str]] = None,
        first_name: Optional[str] = None,
        middle_name: Optional[str] = None,
        last_name: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = {},
    ):
        data = {}
        name = {}
        if first_name:
            name.update({"first_name": first_name})
        if middle_name:
            name.update({"middle_name": middle_name})
        if last_name:
            name.update({"last_name": last_name})
        if name:
            data.update({"name": name})

        if emails:
            ems = []
            for email in emails:
                ems.append({"email": email})
            data.update({"emails": ems})

        if phone_numbers:
            pns = []
            for phone_number in phone_numbers:
                pns.append({"phone_number": phone_number})
            data.update({"phone_numbers": pns})

        if attributes and self._validate_attributes(attributes):
            data.update({"attributes": attributes})

        return self._put("{0}/{1}".format(self.user_url, user_id), data)

    def delete_email(self, email_id: str):
        return self._delete("{0}/emails/{1}".format(self.user_url, email_id))

    def delete_phone_number(self, phone_id: str):
        return self._delete("{0}/phone_numbers/{1}".format(self.user_url, phone_id))
