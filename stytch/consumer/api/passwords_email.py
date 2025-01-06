# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.consumer.models.attribute import Attributes
from stytch.consumer.models.magic_links import Options
from stytch.consumer.models.passwords_email import (
    ResetResponse,
    ResetStartRequestLocale,
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
        email: str,
        reset_password_redirect_url: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        attributes: Optional[Union[Attributes, Dict[str, Any]]] = None,
        login_redirect_url: Optional[str] = None,
        locale: Optional[Union[ResetStartRequestLocale, str]] = None,
        reset_password_template_id: Optional[str] = None,
    ) -> ResetStartResponse:
        """Initiates a password reset for the email address provided. This will trigger an email to be sent to the address, containing a magic link that will allow them to set a new password and authenticate.

        Fields:
          - email: The email of the User that requested the password reset.
          - reset_password_redirect_url: The url that the user clicks from the password reset email to finish the reset password flow.
          This should be a url that your app receives and parses before showing your app's reset password page.
          After the user submits a new password to your app, it should send an API request to complete the password reset process.
          If this value is not passed, the default reset password redirect URL that you set in your Dashboard is used.
          If you have not set a default reset password redirect URL, an error is returned.
          - reset_password_expiration_minutes: Set the expiration for the password reset, in minutes. By default, it expires in 30 minutes.
          The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - attributes: Provided attributes help with fraud detection.
          - login_redirect_url: The URL Stytch redirects to after the OAuth flow is completed for a user that already exists. This URL should be a route in your application which will run `oauth.authenticate` (see below) and finish the login.

          The URL must be configured as a Login URL in the [Redirect URL page](https://stytch.com/docs/dashboard/redirect-urls). If the field is not specified, the default Login URL will be used.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - reset_password_template_id: Use a custom template for password reset emails. By default, it will use your default email template.
          The template must be a template using our built-in customizations or a custom HTML email for Passwords - Password reset.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if reset_password_redirect_url is not None:
            data["reset_password_redirect_url"] = reset_password_redirect_url
        if reset_password_expiration_minutes is not None:
            data["reset_password_expiration_minutes"] = (
                reset_password_expiration_minutes
            )
        if code_challenge is not None:
            data["code_challenge"] = code_challenge
        if attributes is not None:
            data["attributes"] = (
                attributes if isinstance(attributes, dict) else attributes.dict()
            )
        if login_redirect_url is not None:
            data["login_redirect_url"] = login_redirect_url
        if locale is not None:
            data["locale"] = locale
        if reset_password_template_id is not None:
            data["reset_password_template_id"] = reset_password_template_id

        url = self.api_base.url_for("/v1/passwords/email/reset/start", data)
        res = self.sync_client.post(url, data, headers)
        return ResetStartResponse.from_json(res.response.status_code, res.json)

    async def reset_start_async(
        self,
        email: str,
        reset_password_redirect_url: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        login_redirect_url: Optional[str] = None,
        locale: Optional[ResetStartRequestLocale] = None,
        reset_password_template_id: Optional[str] = None,
    ) -> ResetStartResponse:
        """Initiates a password reset for the email address provided. This will trigger an email to be sent to the address, containing a magic link that will allow them to set a new password and authenticate.

        Fields:
          - email: The email of the User that requested the password reset.
          - reset_password_redirect_url: The url that the user clicks from the password reset email to finish the reset password flow.
          This should be a url that your app receives and parses before showing your app's reset password page.
          After the user submits a new password to your app, it should send an API request to complete the password reset process.
          If this value is not passed, the default reset password redirect URL that you set in your Dashboard is used.
          If you have not set a default reset password redirect URL, an error is returned.
          - reset_password_expiration_minutes: Set the expiration for the password reset, in minutes. By default, it expires in 30 minutes.
          The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - attributes: Provided attributes help with fraud detection.
          - login_redirect_url: The URL Stytch redirects to after the OAuth flow is completed for a user that already exists. This URL should be a route in your application which will run `oauth.authenticate` (see below) and finish the login.

          The URL must be configured as a Login URL in the [Redirect URL page](https://stytch.com/docs/dashboard/redirect-urls). If the field is not specified, the default Login URL will be used.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - reset_password_template_id: Use a custom template for password reset emails. By default, it will use your default email template.
          The template must be a template using our built-in customizations or a custom HTML email for Passwords - Password reset.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if reset_password_redirect_url is not None:
            data["reset_password_redirect_url"] = reset_password_redirect_url
        if reset_password_expiration_minutes is not None:
            data["reset_password_expiration_minutes"] = (
                reset_password_expiration_minutes
            )
        if code_challenge is not None:
            data["code_challenge"] = code_challenge
        if attributes is not None:
            data["attributes"] = (
                attributes if isinstance(attributes, dict) else attributes.dict()
            )
        if login_redirect_url is not None:
            data["login_redirect_url"] = login_redirect_url
        if locale is not None:
            data["locale"] = locale
        if reset_password_template_id is not None:
            data["reset_password_template_id"] = reset_password_template_id

        url = self.api_base.url_for("/v1/passwords/email/reset/start", data)
        res = await self.async_client.post(url, data, headers)
        return ResetStartResponse.from_json(res.response.status, res.json)

    def reset(
        self,
        token: str,
        password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        code_verifier: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        attributes: Optional[Union[Attributes, Dict[str, Any]]] = None,
        options: Optional[Union[Options, Dict[str, Any]]] = None,
    ) -> ResetResponse:
        """Reset the user’s password and authenticate them. This endpoint checks that the magic link `token` is valid, hasn’t expired, or already been used – and can optionally require additional security settings, such as the IP address and user agent matching the initial reset request.

        The provided password needs to meet our password strength requirements, which can be checked in advance with the password strength endpoint. If the token and password are accepted, the password is securely stored for future authentication and the user is authenticated.

        Note that a successful password reset by email will revoke all active sessions for the `user_id`.

        Fields:
          - token: The Passwords `token` from the `?token=` query parameter in the URL.

              In the redirect URL, the `stytch_token_type` will be `login` or `reset_password`.

              See examples and read more about redirect URLs [here](https://stytch.com/docs/workspace-management/redirect-urls).
          - password: The password for the user. Any UTF8 character is allowed, e.g. spaces, emojis, non-English characers, etc.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
          - attributes: Provided attributes help with fraud detection.
          - options: Specify optional security settings.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "token": token,
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if code_verifier is not None:
            data["code_verifier"] = code_verifier
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if attributes is not None:
            data["attributes"] = (
                attributes if isinstance(attributes, dict) else attributes.dict()
            )
        if options is not None:
            data["options"] = options if isinstance(options, dict) else options.dict()

        url = self.api_base.url_for("/v1/passwords/email/reset", data)
        res = self.sync_client.post(url, data, headers)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        token: str,
        password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        code_verifier: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        attributes: Optional[Attributes] = None,
        options: Optional[Options] = None,
    ) -> ResetResponse:
        """Reset the user’s password and authenticate them. This endpoint checks that the magic link `token` is valid, hasn’t expired, or already been used – and can optionally require additional security settings, such as the IP address and user agent matching the initial reset request.

        The provided password needs to meet our password strength requirements, which can be checked in advance with the password strength endpoint. If the token and password are accepted, the password is securely stored for future authentication and the user is authenticated.

        Note that a successful password reset by email will revoke all active sessions for the `user_id`.

        Fields:
          - token: The Passwords `token` from the `?token=` query parameter in the URL.

              In the redirect URL, the `stytch_token_type` will be `login` or `reset_password`.

              See examples and read more about redirect URLs [here](https://stytch.com/docs/workspace-management/redirect-urls).
          - password: The password for the user. Any UTF8 character is allowed, e.g. spaces, emojis, non-English characers, etc.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
          - attributes: Provided attributes help with fraud detection.
          - options: Specify optional security settings.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "token": token,
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if code_verifier is not None:
            data["code_verifier"] = code_verifier
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if attributes is not None:
            data["attributes"] = (
                attributes if isinstance(attributes, dict) else attributes.dict()
            )
        if options is not None:
            data["options"] = options if isinstance(options, dict) else options.dict()

        url = self.api_base.url_for("/v1/passwords/email/reset", data)
        res = await self.async_client.post(url, data, headers)
        return ResetResponse.from_json(res.response.status, res.json)
