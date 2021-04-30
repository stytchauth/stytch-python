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

        self.Users = Users(self)
        self.MagicLinks = MagicLinks(self)
        self.OTP = OTP(self)

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
