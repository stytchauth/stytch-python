# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.b2b.api.oauth_discovery import Discovery
from stytch.b2b.models.oauth import AuthenticateRequestLocale, AuthenticateResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class OAuth:
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

    def authenticate(
        self,
        oauth_token: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        pkce_code_verifier: Optional[str] = None,
        locale: Optional[Union[AuthenticateRequestLocale, str]] = None,
        intermediate_session_token: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticate a Member given a `token`. This endpoint verifies that the member completed the OAuth flow by verifying that the token is valid and hasn't expired.  Provide the `session_duration_minutes` parameter to set the lifetime of the session. If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration.

        If the Member is required to complete MFA to log in to the Organization, the returned value of `member_authenticated` will be `false`, and an `intermediate_session_token` will be returned.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `intermediate_session_token` can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to join a different Organization or create a new one.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        If a valid `session_token` or `session_jwt` is passed in, the Member will not be required to complete an MFA step.

        If the Member is logging in via an OAuth provider that does not fully verify the email, the returned value of `member_authenticated` will be `false`, and an `intermediate_session_token` will be returned.
        The `primary_required` field details the authentication flow the Member must perform in order to [complete a step-up authentication](https://stytch.com/docs/b2b/guides/oauth/auth-flows) into the organization. The `intermediate_session_token` must be passed into that authentication flow.

        We’re actively accepting requests for new OAuth providers! Please [email us](mailto:support@stytch.com) or [post in our community](https://stytch.com/docs/b2b/resources) if you are looking for an OAuth provider that is not currently supported.

        Fields:
          - oauth_token: The token to authenticate.
          - session_token: A secret token for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - pkce_code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
          - locale: If the Member needs to complete an MFA step, and the Member has a phone number, this endpoint will pre-emptively send a one-time passcode (OTP) to the Member's phone number. The locale argument will be used to determine which language to use when sending the passcode.

        Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - intermediate_session_token: Adds this primary authentication factor to the intermediate session token. If the resulting set of factors satisfies the organization's primary authentication requirements and MFA requirements, the intermediate session token will be consumed and converted to a member session. If not, the same intermediate session token will be returned.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "oauth_token": oauth_token,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if pkce_code_verifier is not None:
            data["pkce_code_verifier"] = pkce_code_verifier
        if locale is not None:
            data["locale"] = locale
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token

        url = self.api_base.url_for("/v1/b2b/oauth/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        oauth_token: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        pkce_code_verifier: Optional[str] = None,
        locale: Optional[AuthenticateRequestLocale] = None,
        intermediate_session_token: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticate a Member given a `token`. This endpoint verifies that the member completed the OAuth flow by verifying that the token is valid and hasn't expired.  Provide the `session_duration_minutes` parameter to set the lifetime of the session. If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration.

        If the Member is required to complete MFA to log in to the Organization, the returned value of `member_authenticated` will be `false`, and an `intermediate_session_token` will be returned.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `intermediate_session_token` can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to join a different Organization or create a new one.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        If a valid `session_token` or `session_jwt` is passed in, the Member will not be required to complete an MFA step.

        If the Member is logging in via an OAuth provider that does not fully verify the email, the returned value of `member_authenticated` will be `false`, and an `intermediate_session_token` will be returned.
        The `primary_required` field details the authentication flow the Member must perform in order to [complete a step-up authentication](https://stytch.com/docs/b2b/guides/oauth/auth-flows) into the organization. The `intermediate_session_token` must be passed into that authentication flow.

        We’re actively accepting requests for new OAuth providers! Please [email us](mailto:support@stytch.com) or [post in our community](https://stytch.com/docs/b2b/resources) if you are looking for an OAuth provider that is not currently supported.

        Fields:
          - oauth_token: The token to authenticate.
          - session_token: A secret token for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - pkce_code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
          - locale: If the Member needs to complete an MFA step, and the Member has a phone number, this endpoint will pre-emptively send a one-time passcode (OTP) to the Member's phone number. The locale argument will be used to determine which language to use when sending the passcode.

        Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - intermediate_session_token: Adds this primary authentication factor to the intermediate session token. If the resulting set of factors satisfies the organization's primary authentication requirements and MFA requirements, the intermediate session token will be consumed and converted to a member session. If not, the same intermediate session token will be returned.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "oauth_token": oauth_token,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if pkce_code_verifier is not None:
            data["pkce_code_verifier"] = pkce_code_verifier
        if locale is not None:
            data["locale"] = locale
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token

        url = self.api_base.url_for("/v1/b2b/oauth/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)
