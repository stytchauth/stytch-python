import json
from typing import Any, Dict

import requests
import requests.auth

from stytch.client import Client


class FakeClient(Client):
    def __init__(
        self, project_id: str = "NO_PROJECT_ID", secret: str = "NO_SECRET"
    ) -> None:
        self.base_url = "https://localhost:8080/"
        self.project_id = project_id
        self.secret = secret

        self.auth = requests.auth.HTTPBasicAuth(self.project_id, self.secret)


class FakeResponse(requests.Response):
    def __init__(self, status_code: int, body: str = "{}") -> None:
        self.status_code = status_code
        self.body = body

    def json(self) -> Dict[str, Any]:
        return json.loads(self.body)
