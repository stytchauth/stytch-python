#!/usr/bin/env python3

import warnings
from typing import Optional

from stytch.api.crypto_wallets import CryptoWallets
from stytch.api.magic_links import MagicLinks
from stytch.api.oauth import OAuth
from stytch.api.otp import OTP
from stytch.api.passwords import Passwords
from stytch.api.sessions import Sessions
from stytch.api.totps import TOTPs
from stytch.api.users import Users
from stytch.api.webauthn import WebAuthn
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Client:
    """
    Stytch API Python client.

    Learn more at https://stytch.com/docs
    """

    def __init__(
        self,
        project_id: str,
        secret: str,
        environment: Optional[str] = None,
        suppress_warnings: bool = False,
    ):
        base_url = self._env_url(project_id, environment, suppress_warnings)
        api_base = ApiBase(base_url)
        sync_client = SyncClient(project_id, secret)
        async_client = AsyncClient(project_id, secret)

        self.users = Users(api_base, sync_client, async_client)
        self.magic_links = MagicLinks(api_base, sync_client, async_client)
        self.oauth = OAuth(api_base, sync_client, async_client)
        self.otps = OTP(api_base, sync_client, async_client)
        self.sessions = Sessions(api_base, sync_client, async_client)
        self.webauthn = WebAuthn(api_base, sync_client, async_client)
        self.totps = TOTPs(api_base, sync_client, async_client)
        self.crypto_wallets = CryptoWallets(api_base, sync_client, async_client)
        self.passwords = Passwords(api_base, sync_client, async_client)

    @classmethod
    def _env_url(
        cls, project_id: str, env: Optional[str] = None, suppress_warnings: bool = False
    ) -> str:
        """Resolve the base URL for the Stytch API environment."""
        live_api = "https://api.stytch.com/v1/"
        test_api = "https://test.stytch.com/v1/"
        test_warning = "Test version of Stytch not intended for production use"

        if env is None:
            if project_id.startswith("project-live-"):
                return live_api
            else:
                if not suppress_warnings:
                    warnings.warn(test_warning)
                return test_api

        # Supported production environments
        if env == "test":
            if not suppress_warnings:
                warnings.warn(test_warning)
            return test_api
        elif env == "live":
            return live_api

        return env
