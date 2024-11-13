# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.passwords_discovery_email import (
    ResetResponse,
    ResetStartResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Email:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def reset_start(
        self,
        email_address: str,
        reset_password_redirect_url: Optional[str] = None,
        discovery_redirect_url: Optional[str] = None,
        reset_password_template_id: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        pkce_code_challenge: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> ResetStartResponse:
        """Initiates a password reset for the email address provided, when cross-org passwords are enabled. This will trigger an email to be sent to the address, containing a magic link that will allow them to set a new password and authenticate.

        This endpoint adapts to your Project's password strength configuration.
        If you're using [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy), the default, your passwords are considered valid
        if the strength score is >= 3. If you're using [LUDS](https://stytch.com/docs/guides/passwords/strength-policy), your passwords are
        considered valid if they meet the requirements that you've set with Stytch.
        You may update your password strength configuration in the [stytch dashboard](https://stytch.com/dashboard/password-strength-config).

        Fields:
          - email_address: The email address of the Member to start the email reset process for.
          - reset_password_redirect_url: The URL that the Member clicks from the reset password link. This URL should be an endpoint in the backend server that verifies the request by querying
          Stytch's authenticate endpoint and finishes the reset password flow. If this value is not passed, the default `reset_password_redirect_url` that you set in your Dashboard is used.
          If you have not set a default `reset_password_redirect_url`, an error is returned.
          - discovery_redirect_url: The URL that the end user clicks from the discovery Magic Link. This URL should be an endpoint in the backend server that
          verifies the request by querying Stytch's discovery authenticate endpoint and continues the flow. If this value is not passed, the default
          discovery redirect URL that you set in your Dashboard is used. If you have not set a default discovery redirect URL, an error is returned.
          - reset_password_template_id: Use a custom template for reset password emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic Links - Reset Password.
          - reset_password_expiration_minutes: Sets a time limit after which the email link to reset the member's password will no longer be valid.
          - pkce_code_challenge: (no documentation yet)
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email_address": email_address,
        }
        if reset_password_redirect_url is not None:
            data["reset_password_redirect_url"] = reset_password_redirect_url
        if discovery_redirect_url is not None:
            data["discovery_redirect_url"] = discovery_redirect_url
        if reset_password_template_id is not None:
            data["reset_password_template_id"] = reset_password_template_id
        if reset_password_expiration_minutes is not None:
            data[
                "reset_password_expiration_minutes"
            ] = reset_password_expiration_minutes
        if pkce_code_challenge is not None:
            data["pkce_code_challenge"] = pkce_code_challenge
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for(
            "/v1/b2b/passwords/discovery/email/reset/start", data
        )
        res = self.sync_client.post(url, data, headers)
        return ResetStartResponse.from_json(res.response.status_code, res.json)

    async def reset_start_async(
        self,
        email_address: str,
        reset_password_redirect_url: Optional[str] = None,
        discovery_redirect_url: Optional[str] = None,
        reset_password_template_id: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        pkce_code_challenge: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> ResetStartResponse:
        """Initiates a password reset for the email address provided, when cross-org passwords are enabled. This will trigger an email to be sent to the address, containing a magic link that will allow them to set a new password and authenticate.

        This endpoint adapts to your Project's password strength configuration.
        If you're using [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy), the default, your passwords are considered valid
        if the strength score is >= 3. If you're using [LUDS](https://stytch.com/docs/guides/passwords/strength-policy), your passwords are
        considered valid if they meet the requirements that you've set with Stytch.
        You may update your password strength configuration in the [stytch dashboard](https://stytch.com/dashboard/password-strength-config).

        Fields:
          - email_address: The email address of the Member to start the email reset process for.
          - reset_password_redirect_url: The URL that the Member clicks from the reset password link. This URL should be an endpoint in the backend server that verifies the request by querying
          Stytch's authenticate endpoint and finishes the reset password flow. If this value is not passed, the default `reset_password_redirect_url` that you set in your Dashboard is used.
          If you have not set a default `reset_password_redirect_url`, an error is returned.
          - discovery_redirect_url: The URL that the end user clicks from the discovery Magic Link. This URL should be an endpoint in the backend server that
          verifies the request by querying Stytch's discovery authenticate endpoint and continues the flow. If this value is not passed, the default
          discovery redirect URL that you set in your Dashboard is used. If you have not set a default discovery redirect URL, an error is returned.
          - reset_password_template_id: Use a custom template for reset password emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic Links - Reset Password.
          - reset_password_expiration_minutes: Sets a time limit after which the email link to reset the member's password will no longer be valid.
          - pkce_code_challenge: (no documentation yet)
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email_address": email_address,
        }
        if reset_password_redirect_url is not None:
            data["reset_password_redirect_url"] = reset_password_redirect_url
        if discovery_redirect_url is not None:
            data["discovery_redirect_url"] = discovery_redirect_url
        if reset_password_template_id is not None:
            data["reset_password_template_id"] = reset_password_template_id
        if reset_password_expiration_minutes is not None:
            data[
                "reset_password_expiration_minutes"
            ] = reset_password_expiration_minutes
        if pkce_code_challenge is not None:
            data["pkce_code_challenge"] = pkce_code_challenge
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for(
            "/v1/b2b/passwords/discovery/email/reset/start", data
        )
        res = await self.async_client.post(url, data, headers)
        return ResetStartResponse.from_json(res.response.status, res.json)

    def reset(
        self,
        password_reset_token: str,
        password: str,
        pkce_code_verifier: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the password associated with an email and start an intermediate session. This endpoint checks that the password reset token is valid, hasn’t expired, or already been used.

        The provided password needs to meet the project's password strength requirements, which can be checked in advance with the password strength endpoint. If the token and password are accepted, the password is securely stored for future authentication and the user is authenticated.

        Resetting a password will start an intermediate session and return a list of discovered organizations the session can be exchanged into.

        Fields:
          - password_reset_token: The password reset token to authenticate.
          - password: The password to authenticate, reset, or set for the first time. Any UTF8 character is allowed, e.g. spaces, emojis, non-English characers, etc.
          - pkce_code_verifier: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "password_reset_token": password_reset_token,
            "password": password,
        }
        if pkce_code_verifier is not None:
            data["pkce_code_verifier"] = pkce_code_verifier

        url = self.api_base.url_for("/v1/b2b/passwords/discovery/email/reset", data)
        res = self.sync_client.post(url, data, headers)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        password_reset_token: str,
        password: str,
        pkce_code_verifier: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the password associated with an email and start an intermediate session. This endpoint checks that the password reset token is valid, hasn’t expired, or already been used.

        The provided password needs to meet the project's password strength requirements, which can be checked in advance with the password strength endpoint. If the token and password are accepted, the password is securely stored for future authentication and the user is authenticated.

        Resetting a password will start an intermediate session and return a list of discovered organizations the session can be exchanged into.

        Fields:
          - password_reset_token: The password reset token to authenticate.
          - password: The password to authenticate, reset, or set for the first time. Any UTF8 character is allowed, e.g. spaces, emojis, non-English characers, etc.
          - pkce_code_verifier: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "password_reset_token": password_reset_token,
            "password": password,
        }
        if pkce_code_verifier is not None:
            data["pkce_code_verifier"] = pkce_code_verifier

        url = self.api_base.url_for("/v1/b2b/passwords/discovery/email/reset", data)
        res = await self.async_client.post(url, data, headers)
        return ResetResponse.from_json(res.response.status, res.json)
