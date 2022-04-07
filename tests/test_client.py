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

    def test_users_controller_exists(self):
        client = Client("project_id", "secret", "test", suppress_warnings=True)
        assert client.users
        assert client.users.get
        assert client.users.update
        assert client.users.delete
        assert client.users.create

    def test_magic_links_controller_exists(self):
        client = Client("project_id", "secret", "test", suppress_warnings=True)
        assert client.magic_links
        assert client.magic_links.email.send
        assert client.magic_links.authenticate
