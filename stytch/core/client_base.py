import abc
import warnings
from typing import Optional

import aiohttp
import jwt

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class ClientBase(abc.ABC):
    def __init__(
        self,
        project_id: str,
        secret: str,
        environment: Optional[str] = None,
        suppress_warnings: bool = False,
        async_session: Optional[aiohttp.ClientSession] = None,
        fraud_environment: Optional[str] = None,
    ):
        base_url = self._env_url(project_id, environment, suppress_warnings)
        fraud_base_url = "https://telemetry.stytch.com"
        if fraud_environment is not None:
            fraud_base_url = fraud_environment
        self.api_base = ApiBase(base_url)
        self.fraud_api_base = ApiBase(fraud_base_url)
        self.sync_client = SyncClient(project_id, secret)
        self.async_client = AsyncClient(project_id, secret, session=async_session)
        self.jwks_client = self.get_jwks_client(project_id)

    @abc.abstractmethod
    def get_jwks_client(self, project_id: str) -> jwt.PyJWKClient:
        pass

    @classmethod
    def _env_url(
        cls, project_id: str, env: Optional[str], suppress_warnings: bool = False
    ) -> str:
        """Resolve the base URL for the Stytch API environment."""
        if env is None:
            env = "live" if project_id.startswith("project-live-") else "test"

        # Supported production environments
        if env == "test":
            if not suppress_warnings:
                warnings.warn("Test version of Stytch not intended for production use")
            return "https://test.stytch.com/"
        elif env == "live":
            return "https://api.stytch.com/"

        return env
