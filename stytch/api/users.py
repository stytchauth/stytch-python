from .base import Base
import requests


class Users(Base):
    @property
    def user_url(self):
        return self.get_url('users')

    def create(self, email: str, first_name: str, last_name: str):
        data = { "email": email, "first_name": first_name, "last_name": last_name}
        return self._post("{0}".format(self.user_url), data)

    def get(self, user_id: str):
        return self._get("{0}/{1}".format(self.user_url, user_id))

    def delete(self, user_id: str):
        return self._delete("{0}/}/{1}".format(self.user_url))

    def update(self, email: str, first_name: str, last_name: str):
        data = {}
        if email:
            data.update({ "email": email })
        if first_name:
            data.update({ "first_name": first_name })
        if last_name:
            data.update({ "last_name": last_name })

        return self._put("{0}".format(self.user_url), data)