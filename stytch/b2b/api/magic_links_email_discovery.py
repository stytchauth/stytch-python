# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.b2b.models.magic_links_email_discovery import (
    SendRequestLocale,
    SendResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Discovery:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def send(
        self,
        email_address: str,
        discovery_redirect_url: Optional[str] = None,
        pkce_code_challenge: Optional[str] = None,
        login_template_id: Optional[str] = None,
        locale: Optional[Union[SendRequestLocale, str]] = None,
    ) -> SendResponse:
        """Send a discovery magic link to an email address.

        Fields:
          - email_address: The email address of the Member.
          - discovery_redirect_url: The URL that the end user clicks from the discovery Magic Link. This URL should be an endpoint in the backend server that
          verifies the request by querying Stytch's discovery authenticate endpoint and continues the flow. If this value is not passed, the default
          discovery redirect URL that you set in your Dashboard is used. If you have not set a default discovery redirect URL, an error is returned.
          - pkce_code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - login_template_id: Use a custom template for discovery emails. By default, it will use your default email template. The template must be from Stytch's
        built-in customizations or a custom HTML email for Magic Links - Login.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        data: Dict[str, Any] = {
            "email_address": email_address,
        }
        if discovery_redirect_url is not None:
            data["discovery_redirect_url"] = discovery_redirect_url
        if pkce_code_challenge is not None:
            data["pkce_code_challenge"] = pkce_code_challenge
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/b2b/magic_links/email/discovery/send", data)
        res = self.sync_client.post(url, data)
        return SendResponse.from_json(res.response.status_code, res.json)

    async def send_async(
        self,
        email_address: str,
        discovery_redirect_url: Optional[str] = None,
        pkce_code_challenge: Optional[str] = None,
        login_template_id: Optional[str] = None,
        locale: Optional[SendRequestLocale] = None,
    ) -> SendResponse:
        """Send a discovery magic link to an email address.

        Fields:
          - email_address: The email address of the Member.
          - discovery_redirect_url: The URL that the end user clicks from the discovery Magic Link. This URL should be an endpoint in the backend server that
          verifies the request by querying Stytch's discovery authenticate endpoint and continues the flow. If this value is not passed, the default
          discovery redirect URL that you set in your Dashboard is used. If you have not set a default discovery redirect URL, an error is returned.
          - pkce_code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - login_template_id: Use a custom template for discovery emails. By default, it will use your default email template. The template must be from Stytch's
        built-in customizations or a custom HTML email for Magic Links - Login.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        data: Dict[str, Any] = {
            "email_address": email_address,
        }
        if discovery_redirect_url is not None:
            data["discovery_redirect_url"] = discovery_redirect_url
        if pkce_code_challenge is not None:
            data["pkce_code_challenge"] = pkce_code_challenge
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/b2b/magic_links/email/discovery/send", data)
        res = await self.async_client.post(url, data)
        return SendResponse.from_json(res.response.status, res.json)
