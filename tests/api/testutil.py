import json

import requests


class FakeClient:
    def __init__(self, project_id="NO_PROJECT_ID", secret="NO_SECRET"):
        self.base_url = "https://localhost:8080/"
        self.project_id = project_id
        self.secret = secret

        self.auth = requests.auth.HTTPBasicAuth(self.project_id, self.secret)


class FakeResponse:
    def __init__(self, status_code=None, body="{}"):
        self.status_code = status_code
        self.body = body

    def json(self):
        return json.loads(self.body)
