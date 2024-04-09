# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!


from typing import Optional

import aiohttp
import jwt

from stytch.b2b.api.discovery import Discovery
from stytch.b2b.api.magic_links import MagicLinks
from stytch.b2b.api.oauth import OAuth
from stytch.b2b.api.organizations import Organizations
from stytch.b2b.api.otp import OTPs
from stytch.b2b.api.passwords import Passwords
from stytch.b2b.api.rbac import RBAC
from stytch.b2b.api.recovery_codes import RecoveryCodes
from stytch.b2b.api.scim import SCIM
from stytch.b2b.api.sessions import Sessions
from stytch.b2b.api.sso import SSO
from stytch.b2b.api.totps import TOTPs
from stytch.consumer.api.m2m import M2M
from stytch.consumer.api.project import Project
from stytch.core.client_base import ClientBase
from stytch.shared.policy_cache import PolicyCache


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
    ):
        super().__init__(
            project_id=project_id,
            secret=secret,
            environment=environment,
            suppress_warnings=suppress_warnings,
            async_session=async_session,
        )

        policy_cache = PolicyCache(
            RBAC(
                api_base=self.api_base,
                sync_client=self.sync_client,
                async_client=self.async_client,
            )
        )

        self.discovery = Discovery(
            api_base=self.api_base,
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
        self.organizations = Organizations(
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
        self.rbac = RBAC(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.recovery_codes = RecoveryCodes(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.scim = SCIM(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.sso = SSO(
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
            policy_cache=policy_cache,
        )
        self.totps = TOTPs(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )

    def get_jwks_client(self, project_id: str) -> jwt.PyJWKClient:
        data = {"project_id": project_id}
        url = self.api_base.url_for("/v1/b2b/sessions/jwks/{project_id}", data)
        return jwt.PyJWKClient(url)
