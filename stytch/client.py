import warnings

import jwt

from .api.users import Users
from .api.magic_links import MagicLinks
from .api.otp import OTP
from .api.oauth import OAuth
from .api.sessions import Sessions
from .api.totps import TOTPs
from .api.webauthn import WebAuthn
from .api.crypto_wallets import CryptoWallets

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
    ):
        self.project_id = project_id
        self.secret = secret
        self.environment = environment

        self.base_url = _env_url(environment, suppress_warnings)

        jwks_url = self.base_url + 'sessions/jwks/' + self.project_id
        jwks_client = jwt.PyJWKClient(jwks_url)

        self.users = Users(self)
        self.magic_links = MagicLinks(self)
        self.oauth = OAuth(self)
        self.otps = OTP(self)
        self.sessions = Sessions(self, jwks_client)
        self.webauthn = WebAuthn(self)
        self.totps = TOTPs(self)
        self.crypto_wallets = CryptoWallets(self)

def _env_url(env: str, suppress_warnings: bool = False) -> str:
    '''Resolve the base URL for the Stytch API environment.
    '''

    # Supported production environments
    if env == "test":
        if not suppress_warnings:
            warnings.warn("Test version of Stytch not intended for production use")
        return "https://test.stytch.com/v1/"
    elif env == "live":
        return "https://api.stytch.com/v1/"

    # Internal development override. URL builders assume the base URL has a
    # trailing slash, so add one if it's missing.
    if not env.endswith('/'):
        return env + '/'
    return env
