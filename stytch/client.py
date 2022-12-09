import warnings

import jwt

from stytch.api.crypto_wallets import CryptoWallets
from stytch.api.magic_links import MagicLinks
from stytch.api.oauth import OAuth
from stytch.api.otp import OTP
from stytch.api.passwords import Passwords
from stytch.api.sessions import Sessions
from stytch.api.totps import TOTPs
from stytch.api.users import Users
from stytch.api.webauthn import WebAuthn


class Client:
    """
    Stytch API Python client.

    Learn more at https://stytch.com/docs
    """

    def __init__(
        self,
        project_id: str,
        secret: str,
        environment: str,
        suppress_warnings: bool = False,
    ) -> None:
        self.project_id = project_id
        self.secret = secret
        self.environment = environment

        self.base_url = _env_url(environment, suppress_warnings)

        jwks_url = self.base_url + "sessions/jwks/" + self.project_id
        jwks_client = jwt.PyJWKClient(jwks_url)

        self.users = Users(self)
        self.magic_links = MagicLinks(self)
        self.oauth = OAuth(self)
        self.otps = OTP(self)
        self.sessions = Sessions(self, jwks_client)
        self.webauthn = WebAuthn(self)
        self.totps = TOTPs(self)
        self.crypto_wallets = CryptoWallets(self)
        self.passwords = Passwords(self)


def _env_url(env: str, suppress_warnings: bool = False) -> str:
    """Resolve the base URL for the Stytch API environment."""

    # Supported production environments
    if env == "test":
        if not suppress_warnings:
            warnings.warn("Test version of Stytch not intended for production use")
        return "https://test.stytch.com/v1/"
    elif env == "live":
        return "https://api.stytch.com/v1/"

    # Internal development override. URL builders assume the base URL has a
    # trailing slash, so add one if it's missing.
    if not env.endswith("/"):
        return env + "/"
    return env
