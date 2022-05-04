import pytest
from stytch.client import Client


class TestStytchClient:
    def test_test_env_returns_base_url(self):
        client = Client("project_id", "secret", "test", suppress_warnings=True)
        assert client.base_url == "https://test.stytch.com/v1/"

    def test_production_env_returns_prod_url(self):
        client = Client("project_id", "secret", "live", suppress_warnings=True)
        assert client.base_url == "https://api.stytch.com/v1/"

    def test_custom_env_for_development(self):
        client = Client("project_id", "secret", "https://localhost:8000/v1", suppress_warnings=True)
        assert client.base_url == "https://localhost:8000/v1/"

        client = Client("project_id", "secret", "https://localhost:8000/v1/", suppress_warnings=True)
        assert client.base_url == "https://localhost:8000/v1/"

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
