#!/usr/bin/env python3

import base64
import warnings
from typing import Any, Dict, Optional

import aiohttp

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.samlshield.models.saml import (
    SamlValidateRequest,
    SamlValidateRequestOptions,
    SamlValidateResponse,
)
from stytch.version import __version__


class SamlShieldSyncClient:
    """Custom sync client for SamlShield that uses public_token authentication."""
    
    def __init__(self, public_token: str, timeout: Optional[int] = None) -> None:
        # SamlShield uses the public_token as a bearer token
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": f"Stytch Python v{__version__}",
            "Authorization": f"Bearer {public_token}",
        }
        self.timeout = timeout or 600  # Default 10 minutes

    def post_form(self, url: str, data: dict, headers: dict) -> any:
        """Make a form-encoded POST request."""
        import requests
        
        # Merge the provided headers with our default headers
        merged_headers = {**self.headers, **headers}
        
        response = requests.post(
            url,
            data=data,
            headers=merged_headers,
            timeout=self.timeout,
        )
        
        try:
            resp_json = response.json()
        except Exception:
            resp_json = {}
            
        from stytch.core.http.client import ResponseWithJson
        return ResponseWithJson(response=response, json=resp_json)


class SamlShieldAsyncClient:
    """Custom async client for SamlShield that uses public_token authentication."""
    
    def __init__(self, public_token: str, timeout: Optional[int] = None, session: Optional[aiohttp.ClientSession] = None) -> None:
        # SamlShield uses the public_token as a bearer token
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded", 
            "User-Agent": f"Stytch Python v{__version__}",
            "Authorization": f"Bearer {public_token}",
        }
        self.timeout = timeout or 600  # Default 10 minutes
        self.session = session

    async def post_form(self, url: str, data: dict, headers: dict) -> any:
        """Make a form-encoded POST request."""
        # Merge the provided headers with our default headers
        merged_headers = {**self.headers, **headers}
        
        session = self.session or aiohttp.ClientSession()
        try:
            async with session.post(
                url,
                data=data,
                headers=merged_headers,
                timeout=aiohttp.ClientTimeout(total=self.timeout),
            ) as response:
                try:
                    resp_json = await response.json()
                except Exception:
                    resp_json = {}
                    
                from stytch.core.http.client import ResponseWithJson
                return ResponseWithJson(response=response, json=resp_json)
        finally:
            if self.session is None:
                await session.close()


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

    def validate(
        self,
        saml_response: str,
        method_options: Optional[SamlValidateRequestOptions] = None,
    ) -> SamlValidateResponse:
        """Validate a SAML response to check its structure and content.

        Fields:
          - saml_response: The SAML response to validate. This should be the base64 encoded 
                          SAML response from the IdP and not the raw XML.
        """
        headers: Dict[str, str] = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        if method_options is not None:
            headers = method_options.add_headers(headers)
        
        # SamlShield uses form-encoded data instead of JSON
        data: Dict[str, Any] = {
            "SAMLResponse": saml_response,
        }

        url = self.api_base.url_for("/v1/saml/validate", {})
        res = self.sync_client.post_form(url, data, headers)
        return SamlValidateResponse.from_json(res.response.status_code, res.json)

    async def validate_async(
        self,
        saml_response: str,
        method_options: Optional[SamlValidateRequestOptions] = None,
    ) -> SamlValidateResponse:
        """Validate a SAML response to check its structure and content.

        Fields:
          - saml_response: The SAML response to validate. This should be the base64 encoded 
                          SAML response from the IdP and not the raw XML.
        """
        headers: Dict[str, str] = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        if method_options is not None:
            headers = method_options.add_headers(headers)
        
        # SamlShield uses form-encoded data instead of JSON
        data: Dict[str, Any] = {
            "SAMLResponse": saml_response,
        }

        url = self.api_base.url_for("/v1/saml/validate", {})
        res = await self.async_client.post_form(url, data, headers)
        return SamlValidateResponse.from_json(res.response.status_code, res.json)
        
