import json
import pytest
import requests
from unittest import mock

from stytch.api.users import Users


class FakeClient:
    def __init__(self):
        self.base_url = "https://localhost:8080/"
        self.project_id = "NO_PROJECT_ID"
        self.secret = "NO_SECRET"


class FakeResponse:
    def __init__(self, status_code=None, body="{}"):
        self.status_code = status_code
        self.body = body

    def json(self):
        return json.loads(self.body)


class TestUsers:
    def test_create_attributes(self):
        response = FakeResponse(
            status_code=200,
            body='{"user_id": "user-test-183e939c-e7e1-4d56-82da-8ba9c6036878"}',
        )
        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            users = Users(FakeClient())
            users._requester_base = requests
            response = users.create(
                email="test@example.net",
                attributes={
                    "ip_address": "203.0.113.1",
                    "user_agent": "Toaster 3.0",
                },
            )

        mock_post.assert_called_once_with(
            "https://localhost:8080/users",
            data='{"email": "test@example.net", "phone_number": null, "name": {"first_name": null, "middle_name": null, "last_name": null}, "create_user_as_pending": false, "attributes": {"ip_address": "203.0.113.1", "user_agent": "Toaster 3.0"}}',
            auth=users.auth,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Stytch Python v4.0.1'
            },
        )
