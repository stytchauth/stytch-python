# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from stytch.b2b.api.magic_links_email_discovery import Discovery
from stytch.b2b.models.magic_links_email import (
    InviteRequestLocale,
    InviteRequestOptions,
    InviteResponse,
    LoginOrSignupRequestLocale,
    LoginOrSignupResponse,
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
        self.discovery = Discovery(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )

    def login_or_signup(
        self,
        organization_id: str,
        email_address: str,
        login_redirect_url: Optional[str] = None,
        signup_redirect_url: Optional[str] = None,
        pkce_code_challenge: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
        locale: Optional[Union[LoginOrSignupRequestLocale, str]] = None,
    ) -> LoginOrSignupResponse:
        """Send either a login or signup magic link to a Member. A new, pending, or invited Member will receive a signup Email Magic Link. Members will have a `pending` status until they successfully authenticate. An active Member will receive a login Email Magic Link.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - login_redirect_url: The URL that the Member clicks from the login Email Magic Link. This URL should be an endpoint in the backend server that
          verifies the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default login
          redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.
          - signup_redirect_url: The URL the Member clicks from the signup Email Magic Link. This URL should be an endpoint in the backend server that verifies
          the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default sign-up redirect URL
          that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - pkce_code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be from Stytch's
        built-in customizations or a custom HTML email for Magic Links - Login.
          - signup_template_id: Use a custom template for signup emails. By default, it will use your default email template. The template must be from Stytch's
        built-in customizations or a custom HTML email for Magic Links - Signup.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
        }
        if login_redirect_url is not None:
            data["login_redirect_url"] = login_redirect_url
        if signup_redirect_url is not None:
            data["signup_redirect_url"] = signup_redirect_url
        if pkce_code_challenge is not None:
            data["pkce_code_challenge"] = pkce_code_challenge
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/b2b/magic_links/email/login_or_signup", data)
        res = self.sync_client.post(url, data, headers)
        return LoginOrSignupResponse.from_json(res.response.status_code, res.json)

    async def login_or_signup_async(
        self,
        organization_id: str,
        email_address: str,
        login_redirect_url: Optional[str] = None,
        signup_redirect_url: Optional[str] = None,
        pkce_code_challenge: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
        locale: Optional[LoginOrSignupRequestLocale] = None,
    ) -> LoginOrSignupResponse:
        """Send either a login or signup magic link to a Member. A new, pending, or invited Member will receive a signup Email Magic Link. Members will have a `pending` status until they successfully authenticate. An active Member will receive a login Email Magic Link.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - login_redirect_url: The URL that the Member clicks from the login Email Magic Link. This URL should be an endpoint in the backend server that
          verifies the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default login
          redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.
          - signup_redirect_url: The URL the Member clicks from the signup Email Magic Link. This URL should be an endpoint in the backend server that verifies
          the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default sign-up redirect URL
          that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - pkce_code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be from Stytch's
        built-in customizations or a custom HTML email for Magic Links - Login.
          - signup_template_id: Use a custom template for signup emails. By default, it will use your default email template. The template must be from Stytch's
        built-in customizations or a custom HTML email for Magic Links - Signup.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
        }
        if login_redirect_url is not None:
            data["login_redirect_url"] = login_redirect_url
        if signup_redirect_url is not None:
            data["signup_redirect_url"] = signup_redirect_url
        if pkce_code_challenge is not None:
            data["pkce_code_challenge"] = pkce_code_challenge
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/b2b/magic_links/email/login_or_signup", data)
        res = await self.async_client.post(url, data, headers)
        return LoginOrSignupResponse.from_json(res.response.status, res.json)

    def invite(
        self,
        organization_id: str,
        email_address: str,
        invite_redirect_url: Optional[str] = None,
        invited_by_member_id: Optional[str] = None,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        invite_template_id: Optional[str] = None,
        locale: Optional[Union[InviteRequestLocale, str]] = None,
        roles: Optional[List[str]] = None,
        method_options: Optional[InviteRequestOptions] = None,
    ) -> InviteResponse:
        """Send an invite email to a new Member to join an Organization. The Member will be created with an `invited` status until they successfully authenticate. Sending invites to `pending` Members will update their status to `invited`. Sending invites to already `active` Members will return an error. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - invite_redirect_url: The URL that the Member clicks from the invite Email Magic Link. This URL should be an endpoint in the backend server that verifies
          the request by querying Stytch's authenticate endpoint and finishes the invite flow. If this value is not passed, the default `invite_redirect_url`
          that you set in your Dashboard is used. If you have not set a default `invite_redirect_url`, an error is returned.
          - invited_by_member_id: The `member_id` of the Member who sends the invite.
          - name: The name of the Member.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - invite_template_id: Use a custom template for invite emails. By default, it will use your default email template. The template must be a template
          using our built-in customizations or a custom HTML email for Magic Links - Invite.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - roles: Roles to explicitly assign to this Member. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment)
           for more information about role assignment.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
        }
        if invite_redirect_url is not None:
            data["invite_redirect_url"] = invite_redirect_url
        if invited_by_member_id is not None:
            data["invited_by_member_id"] = invited_by_member_id
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if invite_template_id is not None:
            data["invite_template_id"] = invite_template_id
        if locale is not None:
            data["locale"] = locale
        if roles is not None:
            data["roles"] = roles

        url = self.api_base.url_for("/v1/b2b/magic_links/email/invite", data)
        res = self.sync_client.post(url, data, headers)
        return InviteResponse.from_json(res.response.status_code, res.json)

    async def invite_async(
        self,
        organization_id: str,
        email_address: str,
        invite_redirect_url: Optional[str] = None,
        invited_by_member_id: Optional[str] = None,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        invite_template_id: Optional[str] = None,
        locale: Optional[InviteRequestLocale] = None,
        roles: Optional[List[str]] = None,
        method_options: Optional[InviteRequestOptions] = None,
    ) -> InviteResponse:
        """Send an invite email to a new Member to join an Organization. The Member will be created with an `invited` status until they successfully authenticate. Sending invites to `pending` Members will update their status to `invited`. Sending invites to already `active` Members will return an error. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - invite_redirect_url: The URL that the Member clicks from the invite Email Magic Link. This URL should be an endpoint in the backend server that verifies
          the request by querying Stytch's authenticate endpoint and finishes the invite flow. If this value is not passed, the default `invite_redirect_url`
          that you set in your Dashboard is used. If you have not set a default `invite_redirect_url`, an error is returned.
          - invited_by_member_id: The `member_id` of the Member who sends the invite.
          - name: The name of the Member.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - invite_template_id: Use a custom template for invite emails. By default, it will use your default email template. The template must be a template
          using our built-in customizations or a custom HTML email for Magic Links - Invite.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - roles: Roles to explicitly assign to this Member. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment)
           for more information about role assignment.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
        }
        if invite_redirect_url is not None:
            data["invite_redirect_url"] = invite_redirect_url
        if invited_by_member_id is not None:
            data["invited_by_member_id"] = invited_by_member_id
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if invite_template_id is not None:
            data["invite_template_id"] = invite_template_id
        if locale is not None:
            data["locale"] = locale
        if roles is not None:
            data["roles"] = roles

        url = self.api_base.url_for("/v1/b2b/magic_links/email/invite", data)
        res = await self.async_client.post(url, data, headers)
        return InviteResponse.from_json(res.response.status, res.json)
