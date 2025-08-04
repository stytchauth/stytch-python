from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.samlshield.models.saml import (
    SamlValidateRequestOptions,
    SamlValidateResponse,
)


class Saml:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

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
        headers: Dict[str, str] = {"Content-Type": "application/x-www-form-urlencoded"}
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
        headers: Dict[str, str] = {"Content-Type": "application/x-www-form-urlencoded"}
        if method_options is not None:
            headers = method_options.add_headers(headers)

        # SamlShield uses form-encoded data instead of JSON
        data: Dict[str, Any] = {
            "SAMLResponse": saml_response,
        }

        url = self.api_base.url_for("/v1/saml/validate", {})
        res = await self.async_client.post_form(url, data, headers)
        return SamlValidateResponse.from_json(res.response.status, res.json)
