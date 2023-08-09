# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!


from typing import Optional

from stytch.consumer.api.crypto_wallets import CryptoWallets
from stytch.consumer.api.m2m import M2M
from stytch.consumer.api.magic_links import MagicLinks
from stytch.consumer.api.oauth import OAuth
from stytch.consumer.api.otp import OTPs
from stytch.consumer.api.passwords import Passwords
from stytch.consumer.api.sessions import Sessions
from stytch.consumer.api.totps import TOTPs
from stytch.consumer.api.users import Users
from stytch.consumer.api.webauthn import WebAuthn
from stytch.core.client_base import ClientBase


class Client(ClientBase):
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
        super().__init__(project_id, secret, environment, suppress_warnings)

        self.crypto_wallets = CryptoWallets(
            self.api_base, self.sync_client, self.async_client
        )
        self.m2m = M2M(
            self.api_base,
            self.sync_client,
            self.async_client,
            self.jwks_client,
            project_id,
        )
        self.magic_links = MagicLinks(
            self.api_base, self.sync_client, self.async_client
        )
        self.oauth = OAuth(self.api_base, self.sync_client, self.async_client)
        self.otps = OTPs(self.api_base, self.sync_client, self.async_client)
        self.passwords = Passwords(self.api_base, self.sync_client, self.async_client)
        self.sessions = Sessions(
            self.api_base,
            self.sync_client,
            self.async_client,
            self.jwks_client,
            project_id,
        )
        self.totps = TOTPs(self.api_base, self.sync_client, self.async_client)
        self.users = Users(self.api_base, self.sync_client, self.async_client)
        self.webauthn = WebAuthn(self.api_base, self.sync_client, self.async_client)
