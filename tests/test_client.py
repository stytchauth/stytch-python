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
        with pytest.raises(Exception, match="Please specify test or live env"):
            Client("project_id", "secret", "invalid env").base_url

    def test_users_namespace_exists(self):
        client = Client("project_id", "secret", "development", suppress_warnings=True)
        assert client.users
        assert client.users.get
        assert client.users.update
        assert client.users.delete
        assert client.users.create

    def test_magic_links_namespace_exists(self):
        client = Client("project_id", "secret", "development", suppress_warnings=True)
        assert client.magic_links
        assert client.magic_links.send
        assert client.magic_links.send_by_email
        assert client.magic_links.authenticate

    def test_deprecated_namespaces(self):
        # Use the same client for the whole test, because each warning should only occur once per
        # client instance.
        client = Client("project_id", "secret", "development", suppress_warnings=False)

        with pytest.warns(DeprecationWarning, match="Users has been deprecated. Use users instead."):
            client.Users

        with pytest.warns(DeprecationWarning, match="MagicLinks has been deprecated. Use magic_links instead."):
            client.MagicLinks

        with pytest.warns(DeprecationWarning, match="OTP has been deprecated. Use otp instead."):
            client.OTP

        with pytest.warns(None) as warns:
            assert client.Users == client.users
            assert client.MagicLinks == client.magic_links
            assert client.OTP == client.otp

        assert len(warns) == 0
