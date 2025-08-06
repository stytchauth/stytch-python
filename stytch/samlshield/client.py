#!/usr/bin/env python3

from typing import Any, Dict, Optional

import aiohttp
import requests

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, ResponseWithJson, SyncClient
from stytch.samlshield.api.saml import Saml
from stytch.version import __version__


class SamlShieldSyncClient(SyncClient):
    """Custom sync client for SamlShield that uses public_token authentication."""

    def __init__(self, public_token: str, timeout: Optional[int] = None) -> None:
        # Initialize with dummy values since we'll override auth
        super().__init__("", "")
        # Override headers for Bearer auth
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": f"Stytch Python v{__version__}",
            "Authorization": f"Bearer {public_token}",
        }
        # Keep auth but override with Bearer in headers
        self.timeout = timeout or 600

    def post_form(
        self,
        url: str,
        form: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson[requests.Response]:
        """Override to use custom timeout and merge headers properly."""
        final_headers = self.headers.copy()
        final_headers.update(headers or {})

        response = requests.post(
            url,
            data=form,
            headers=final_headers,
            timeout=self.timeout,
        )

        return self._response_from_request(response)


class SamlShieldAsyncClient(AsyncClient):
    """Custom async client for SamlShield that uses public_token authentication."""

    def __init__(
        self,
        public_token: str,
        timeout: Optional[int] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        # Initialize with dummy values since we'll override auth
        super().__init__("", "", session)
        # Override headers for Bearer auth
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": f"Stytch Python v{__version__}",
            "Authorization": f"Bearer {public_token}",
        }
        # Keep auth but override with Bearer in headers
        self.timeout = timeout or 600


class SamlShieldClient:
    """
    SamlShield API Python client.

    SamlShield is a SAML response validation service that helps identify
    potential security issues in SAML authentication flows.

    Learn more at https://samlshield.com/
    """

    def __init__(
        self,
        public_token: str,
        timeout: Optional[int] = None,
        async_session: Optional[aiohttp.ClientSession] = None,
        custom_base_url: Optional[str] = None,
    ):
        """
        Initialize the SamlShield client.

        Args:
            public_token: Your SamlShield public token for authentication
            timeout: Request timeout in seconds (default: 600)
            async_session: Optional aiohttp session for async requests
            custom_base_url: Optional custom base URL (default: https://api.samlshield.com/)
        """
        if not public_token:
            raise ValueError('Missing "public_token"')

        # Validate custom_base_url uses HTTPS
        if custom_base_url and not custom_base_url.startswith("https://"):
            raise ValueError("custom_base_url must use HTTPS scheme")

        base_url = custom_base_url or "https://api.samlshield.com/"
        if not base_url.endswith("/"):
            base_url += "/"

        self.api_base = ApiBase(base_url)
        self.sync_client = SamlShieldSyncClient(public_token, timeout)
        self.async_client = SamlShieldAsyncClient(public_token, timeout, async_session)

        self.saml = Saml(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
