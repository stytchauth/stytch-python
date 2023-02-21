#!/usr/bin/env python3

import warnings

from stytch.b2b.api.magic_links import MagicLinks
from stytch.b2b.api.organizations import Organizations
from stytch.b2b.api.sessions import Sessions
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Client:
    """
    Stytch B2B API Python client.

    Learn more at https://stytch.com/docs
    """

    def __init__(
        self,
        project_id: str,
        secret: str,
        environment: str,
        suppress_warnings: bool = False,
    ):
        base_url = self._env_url(environment, suppress_warnings)
        api_base = ApiBase(base_url)
        sync_client = SyncClient(project_id, secret)
        async_client = AsyncClient(project_id, secret)

        self.magic_links = MagicLinks(api_base, sync_client, async_client)
        self.organizations = Organizations(api_base, sync_client, async_client)
        self.sessions = Sessions(api_base, sync_client, async_client)

    @classmethod
    def _env_url(cls, env: str, suppress_warnings: bool = False) -> str:
        """Resolve the base URL for the Stytch API environment."""

        # Supported production environments
        if env == "test":
            if not suppress_warnings:
                warnings.warn("Test version of Stytch not intended for production use")
            return "https://test.stytch.com/v1/b2b/"
        elif env == "live":
            return "https://api.stytch.com/v1/b2b/"

        return env
