import requests
from unittest import mock

from testutil import FakeClient, FakeResponse

from stytch.api.users import Users
from stytch.version import __version__ as version


class TestUsers:
    def test_create_attributes(self):
        client = FakeClient()
        response = FakeResponse(
            status_code=200,
            body='{"user_id": "user-test-183e939c-e7e1-4d56-82da-8ba9c6036878"}',
        )

        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            users = Users(client)
            users._requester_base = requests
            _ = users.create(
                email="test@example.net",
                attributes={
                    "ip_address": "203.0.113.1",
                    "user_agent": "Toaster 3.0",
                },
            )

        mock_post.assert_called_once_with(
            "https://localhost:8080/users",
            data='{"email": "test@example.net", "phone_number": null, "name": {"first_name": null, "middle_name": null, "last_name": null}, "create_user_as_pending": false, "attributes": {"ip_address": "203.0.113.1", "user_agent": "Toaster 3.0"}}',
            auth=client.auth,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': f'Stytch Python v{version}'
            },
        )
