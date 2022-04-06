import requests
from unittest import mock

from testutil import FakeClient, FakeResponse

from stytch.api.magic_links import MagicLinks


class TestMagicLinks:
    def test_authenticate(self):
        client = FakeClient()
        response = FakeResponse(status_code=200)

        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            magic_links = MagicLinks(client)
            magic_links._requester_base = requests

            _ = magic_links.authenticate(
                token="DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94=",
                attributes={
                    "ip_address": "203.0.113.1",
                    "user_agent": "Toaster 3.0",
                },
                options={
                    "ip_match_required": True,
                    "user_agent_match_required": False,
                },
                session_token="mZAYn5aLEqKUlZ_Ad9U_fWr38GaAQ1oFAhT8ds245v7Q",
                session_duration_minutes=60,
            )

        mock_post.assert_called_once_with(
            "https://localhost:8080/magic_links/authenticate",
            data='{"token": "DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94=", "attributes": {"ip_address": "203.0.113.1", "user_agent": "Toaster 3.0"}, "options": {"ip_match_required": true}, "session_token": "mZAYn5aLEqKUlZ_Ad9U_fWr38GaAQ1oFAhT8ds245v7Q", "session_duration_minutes": 60}',
            auth=client.auth,
            headers=mock.ANY,
        )
