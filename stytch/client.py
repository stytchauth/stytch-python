from collections import defaultdict
import warnings

from .api.users import Users
from .api.magic_links import MagicLinks
from .api.otp import OTP

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
        self.suppress_warnings = suppress_warnings

        self.users = Users(self)
        self.magic_links = MagicLinks(self)
        self.otp = OTP(self)

        self._warned = defaultdict(bool)

    @property
    def Users(self):
        if not self._warned['Users']:
            warnings.warn(
                'Users has been deprecated. Use users instead.',
                DeprecationWarning,
            )
            self._warned['Users'] = True
        return self.users

    @property
    def MagicLinks(self):
        if not self._warned['MagicLinks']:
            warnings.warn(
                'MagicLinks has been deprecated. Use magic_links instead.',
                DeprecationWarning,
            )
            self._warned['MagicLinks'] = True
        return self.magic_links

    @property
    def OTP(self):
        if not self._warned['OTP']:
            warnings.warn(
                'OTP has been deprecated. Use otp instead.',
                DeprecationWarning,
            )
            self._warned['OTP'] = True
        return self.otp

    @property
    def base_url(self):
        if self.environment == "test":
            base_url = "https://test.stytch.com/v1/"
            if not self.suppress_warnings:
                warnings.warn("Test version of Stytch not intended for production use")
        elif self.environment == "live":
            base_url = "https://api.stytch.com/v1/"
        else:
            raise Exception("Invalid or missing env. Please specify test or live env")

        return base_url
