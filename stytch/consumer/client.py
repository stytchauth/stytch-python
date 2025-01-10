# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!


from typing import Optional

import aiohttp
import jwt

from stytch.consumer.api.crypto_wallets import CryptoWallets
from stytch.consumer.api.fraud import Fraud
from stytch.consumer.api.idp import IDP
from stytch.consumer.api.m2m import M2M
from stytch.consumer.api.magic_links import MagicLinks
from stytch.consumer.api.oauth import OAuth
from stytch.consumer.api.otp import OTPs
from stytch.consumer.api.passwords import Passwords
from stytch.consumer.api.project import Project
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
        async_session: Optional[aiohttp.ClientSession] = None,
        fraud_environment: Optional[str] = None,
    ):
        super().__init__(
            project_id=project_id,
            secret=secret,
            environment=environment,
            suppress_warnings=suppress_warnings,
            async_session=async_session,
            fraud_environment=fraud_environment,
        )

        self.crypto_wallets = CryptoWallets(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.fraud = Fraud(
            api_base=self.fraud_api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.m2m = M2M(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
            jwks_client=self.jwks_client,
            project_id=project_id,
        )
        self.magic_links = MagicLinks(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.oauth = OAuth(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.otps = OTPs(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.passwords = Passwords(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.project = Project(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.sessions = Sessions(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
            jwks_client=self.jwks_client,
            project_id=project_id,
        )
        self.totps = TOTPs(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.users = Users(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.webauthn = WebAuthn(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.idp = IDP(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
            jwks_client=self.jwks_client,
            project_id=project_id,
        )

    def get_jwks_client(self, project_id: str) -> jwt.PyJWKClient:
        data = {"project_id": project_id}
        url = self.api_base.url_for("/v1/sessions/jwks/{project_id}", data)
        return jwt.PyJWKClient(url)
