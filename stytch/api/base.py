import json
import requests

from typing import Dict, Set

from .decorator import throw_stytch_exception


class Base:
    def __init__(self, client):
        self._requester_base = requests
        self.client = client
        self.auth = requests.auth.HTTPBasicAuth(
            self.client.project_id, self.client.secret
        )

    def _validate_fields(self, accepted_fields: Set[str], fields: Set[str]) -> bool:
        if len(accepted_fields.union(fields)) > len(accepted_fields):
            raise Exception("Unknown arguments applied")

        return True

    def get_url(self, arg: str):
        return "{0}{1}".format(self.client.base_url, arg)

    @throw_stytch_exception
    def _get(self, url: str, query_params: Dict):
        return self._requester_base.get(url, auth=self.auth, params=query_params)

    @throw_stytch_exception
    def _post(self, url: str, data: Dict):
        return self._requester_base.post(url, auth=self.auth, data=json.dumps(data))

    @throw_stytch_exception
    def _put(self, url: str, data: Dict):
        return self._requester_base.put(url, auth=self.auth, data=json.dumps(data))

    @throw_stytch_exception
    def _delete(self, url: str):
        return self._requester_base.delete(url, auth=self.auth)
