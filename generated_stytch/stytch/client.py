from .configuration import Configuration
from .api_client import ApiClient
from .api.emails_api import EmailsApi
from .api.magic_links_api import MagicLinksApi
from .api.users_api import UsersApi

class Client:

    def __init__(self, project_id: str, secret: str):
        self.configuration = Configuration(
            username=project_id,
            password=secret,
        )
        stytch_client = ApiClient(self.configuration)

        self.Users = UsersApi(stytch_client)
        self.Emails = EmailsApi(stytch_client)
        self.MagicLinks = MagicLinksApi(stytch_client)


