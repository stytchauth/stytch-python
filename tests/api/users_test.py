import requests
import unittest
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
                "Content-Type": "application/json",
                "User-Agent": f"Stytch Python v{version}",
            },
        )


class TestSearchUsers(unittest.TestCase):
    def test_search_no_params(self):
        client = FakeClient()
        response = FakeResponse(
            status_code=200,
            body="{}",
        )

        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            users = Users(client)
            users._requester_base = requests
            _ = users.search()

        mock_post.assert_called_once_with(
            "https://localhost:8080/users/search",
            data="{}",
            auth=client.auth,
            headers={
                "Content-Type": "application/json",
                "User-Agent": f"Stytch Python v{version}",
            },
        )

    def test_search_with_params(self):
        client = FakeClient()
        response = FakeResponse(
            status_code=200,
            body='{"user_id": "user-test-183e939c-e7e1-4d56-82da-8ba9c6036878"}',
        )

        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            users = Users(client)
            users._requester_base = requests
            _ = users.search(
                limit=50,
                cursor="abc123",
                query={
                    "operator": "AND",
                    "operands": [{"filter_name": "test_filter", "filter_value": 1}],
                },
            )

        mock_post.assert_called_once_with(
            "https://localhost:8080/users/search",
            data='{"limit": 50, "cursor": "abc123", "query": {"operator": "AND", "operands": [{"filter_name": "test_filter", "filter_value": 1}]}}',
            auth=client.auth,
            headers={
                "Content-Type": "application/json",
                "User-Agent": f"Stytch Python v{version}",
            },
        )

    @mock.patch("requests.post")
    def test_search_all(self, mock_post):
        client = FakeClient()
        response_1 = FakeResponse(
            status_code=200,
            body='{"results_metadata": {"next_cursor": "A"}}',
        )

        response_2 = FakeResponse(
            status_code=200,
            body='{"results_metadata": {"next_cursor": null}}',
        )

        users = Users(client)
        users._requester_base = requests

        search_generator = users.search_all()

        mock_post.return_value = response_1
        page = next(search_generator)
        assert page == response_1
        mock_post.assert_called_with(
            "https://localhost:8080/users/search",
            data="{}",
            auth=client.auth,
            headers={
                "Content-Type": "application/json",
                "User-Agent": f"Stytch Python v{version}",
            },
        )

        mock_post.return_value = response_2
        page = next(search_generator)
        assert page == response_2
        mock_post.assert_called_with(
            "https://localhost:8080/users/search",
            data='{"cursor": "A"}',
            auth=client.auth,
            headers={
                "Content-Type": "application/json",
                "User-Agent": f"Stytch Python v{version}",
            },
        )

        with self.assertRaises(StopIteration):
            next(search_generator)
