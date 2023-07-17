import warnings
from typing import Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class ClientBase:
    def __init__(
        self,
        project_id: str,
        secret: str,
        environment: Optional[str] = None,
        suppress_warnings: bool = False,
    ):
        base_url = self._env_url(project_id, environment, suppress_warnings)
        self.api_base = ApiBase(base_url)
        self.sync_client = SyncClient(project_id, secret)
        self.async_client = AsyncClient(project_id, secret)

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
