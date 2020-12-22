import pytest
from stytch.client import Client


class TestStytchClient:
    def test_development_env_returns_base_url(self):
        client = Client("project_id", "secret", "test", suppress_warnings=True)
        assert client.base_url == "https://test.stytch.com/v1/"

    def test_production_env_returns_prod_url(self):
        client = Client("project_id", "secret", "live", suppress_warnings=True)
        assert client.base_url == "https://api.stytch.com/v1/"

    def test_no_env_raises_error(self):
        with pytest.raises(Exception):
            _ = Client("project_id", "secret", "invalid env").base_url
            assert _

    def test_Users_controller_exists(self):
        client = Client("project_id", "secret", "development", suppress_warnings=True)
        assert client.Users
        assert client.Users.get
        assert client.Users.update
        assert client.Users.delete
        assert client.Users.create

    def test_MagicLinks_controller_exists(self):
        client = Client("project_id", "secret", "development", suppress_warnings=True)
        assert client.MagicLinks
        assert client.MagicLinks.send
        assert client.MagicLinks.send_by_email
        assert client.MagicLinks.authenticate
