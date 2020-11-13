from stytch.client import Client

class TestStytchClient:

    def test_development_env_returns_base_url(self):
        client = Client("project_id", "secret", "development", suppress_warnings=True)
        assert client.base_url == "https://test.stytch.com/v1/"

    def test_production_env_returns_prod_url(self):
        client = Client("project_id", "secret", "production", suppress_warnings=True)
        assert client.base_url == "https://api.stytch.com/v1/"

    def test_Users_controller_exists(self):
        client = Client("project_id", "secret", "development", suppress_warnings=True)
        assert client.Users
        assert client.Users.get
        assert client.Users.update
        assert client.Users.delete
        assert client.Users.create