import json
import requests

from typing import Dict


class Base:
    def __init__(self, client):
        self._requester_base = requests
        self.client = client
        self.auth = requests.auth.HTTPBasicAuth(self.client.project_id, self.client.secret)
    
    def get_url(self, arg: str):
        return "{0}{1}".format(self.client.base_url, arg)

    def _get(self, url: str):
        return self._requester_base.get(url, auth=self.auth)

    def _post(self, url: str, data: Dict):
        print(url)
        return self._requester_base.post(url, auth=self.auth, data=json.dumps(data))

    def _put(self, url: str, data: Dict):
        return self._requester_base.put(url, auth=self.auth, data=json.dumps(data))

    def _delete(self, url: str):
        return self._requester_base.delete(url, auth=self.auth)