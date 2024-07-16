# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
import enum
from typing import Any, Dict, List, Optional

import pydantic

from stytch.consumer.models.attribute import Attributes
from stytch.consumer.models.users import User
from stytch.core.response_base import ResponseBase


class AuthenticationFactorDeliveryMethod(str, enum.Enum):
    EMAIL = "email"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    EMBEDDED = "embedded"
    OAUTH_GOOGLE = "oauth_google"
    OAUTH_MICROSOFT = "oauth_microsoft"
    OAUTH_APPLE = "oauth_apple"
    WEBAUTHN_REGISTRATION = "webauthn_registration"
    AUTHENTICATOR_APP = "authenticator_app"
    OAUTH_GITHUB = "oauth_github"
    RECOVERY_CODE = "recovery_code"
    OAUTH_FACEBOOK = "oauth_facebook"
    CRYPTO_WALLET = "crypto_wallet"
    OAUTH_AMAZON = "oauth_amazon"
    OAUTH_BITBUCKET = "oauth_bitbucket"
    OAUTH_COINBASE = "oauth_coinbase"
    OAUTH_DISCORD = "oauth_discord"
    OAUTH_FIGMA = "oauth_figma"
    OAUTH_GITLAB = "oauth_gitlab"
    OAUTH_INSTAGRAM = "oauth_instagram"
    OAUTH_LINKEDIN = "oauth_linkedin"
    OAUTH_SHOPIFY = "oauth_shopify"
    OAUTH_SLACK = "oauth_slack"
    OAUTH_SNAPCHAT = "oauth_snapchat"
    OAUTH_SPOTIFY = "oauth_spotify"
    OAUTH_STEAM = "oauth_steam"
    OAUTH_TIKTOK = "oauth_tiktok"
    OAUTH_TWITCH = "oauth_twitch"
    OAUTH_TWITTER = "oauth_twitter"
    KNOWLEDGE = "knowledge"
    BIOMETRIC = "biometric"
    SSO_SAML = "sso_saml"
    SSO_OIDC = "sso_oidc"
    OAUTH_SALESFORCE = "oauth_salesforce"
    OAUTH_YAHOO = "oauth_yahoo"
    OAUTH_HUBSPOT = "oauth_hubspot"
    IMPORTED_AUTH0 = "imported_auth0"
    OAUTH_EXCHANGE_SLACK = "oauth_exchange_slack"
    OAUTH_EXCHANGE_HUBSPOT = "oauth_exchange_hubspot"


class AuthenticationFactorType(str, enum.Enum):
    MAGIC_LINK = "magic_link"
    OTP = "otp"
    OAUTH = "oauth"
    WEBAUTHN = "webauthn"
    TOTP = "totp"
    CRYPTO = "crypto"
    PASSWORD = "password"
    SIGNATURE_CHALLENGE = "signature_challenge"
    SSO = "sso"
    IMPORTED = "imported"
    RECOVERY_CODES = "recovery_codes"


class AmazonOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class AppleOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class AuthenticatorAppFactor(pydantic.BaseModel):
    """
    Fields:
      - totp_id: Globally unique UUID that identifies a TOTP instance.
    """  # noqa

    totp_id: str


class BiometricFactor(pydantic.BaseModel):
    biometric_registration_id: str


class BitbucketOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class CoinbaseOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class CryptoWalletFactor(pydantic.BaseModel):
    crypto_wallet_id: str
    crypto_wallet_address: str
    crypto_wallet_type: str


class DiscordOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class EmailFactor(pydantic.BaseModel):
    """
    Fields:
      - email_id: The globally unique UUID of the Member's email.
      - email_address: The email address of the Member.
    """  # noqa

    email_id: str
    email_address: str


class EmbeddableMagicLinkFactor(pydantic.BaseModel):
    embedded_id: str


class FacebookOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class FigmaOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class GitLabOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class GithubOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class GoogleOAuthFactor(pydantic.BaseModel):
    """
    Fields:
      - id: The unique ID of an OAuth registration.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - email_id: The globally unique UUID of the Member's email.
    """  # noqa

    id: str
    provider_subject: str
    email_id: Optional[str] = None


class HubspotOAuthExchangeFactor(pydantic.BaseModel):
    email_id: str


class HubspotOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class InstagramOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class JWK(pydantic.BaseModel):
    kty: str
    use: str
    key_ops: List[str]
    alg: str
    kid: str
    x5c: List[str]
    x5tS256: str
    n: str
    e: str


class LinkedInOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class MicrosoftOAuthFactor(pydantic.BaseModel):
    """
    Fields:
      - id: The unique ID of an OAuth registration.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - email_id: The globally unique UUID of the Member's email.
    """  # noqa

    id: str
    provider_subject: str
    email_id: Optional[str] = None


class OIDCSSOFactor(pydantic.BaseModel):
    """
    Fields:
      - id: The unique ID of an SSO Registration.
      - provider_id: Globally unique UUID that identifies a specific OIDC Connection.
      - external_id: The ID of the member given by the identity provider.
    """  # noqa

    id: str
    provider_id: str
    external_id: str


class PhoneNumberFactor(pydantic.BaseModel):
    """
    Fields:
      - phone_id: The globally unique UUID of the Member's phone number.
      - phone_number: The phone number of the Member.
    """  # noqa

    phone_id: str
    phone_number: str


class RecoveryCodeFactor(pydantic.BaseModel):
    totp_recovery_code_id: str


class SAMLSSOFactor(pydantic.BaseModel):
    """
    Fields:
      - id: The unique ID of an SSO Registration.
      - provider_id: Globally unique UUID that identifies a specific SAML Connection.
      - external_id: The ID of the member given by the identity provider.
    """  # noqa

    id: str
    provider_id: str
    external_id: str


class SalesforceOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class ShopifyOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class SlackOAuthExchangeFactor(pydantic.BaseModel):
    email_id: str


class SlackOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class SnapchatOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class SpotifyOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class SteamOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class TikTokOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class TwitchOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class TwitterOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class WebAuthnFactor(pydantic.BaseModel):
    webauthn_registration_id: str
    domain: str
    user_agent: Optional[str] = None


class YahooOAuthFactor(pydantic.BaseModel):
    id: str
    provider_subject: str
    email_id: Optional[str] = None


class AuthenticationFactor(pydantic.BaseModel):
    """
    Fields:
      - type: The type of authentication factor. The possible values are: `magic_link`, `otp`,
           `oauth`, `password`, or `sso`.
      - delivery_method: The method that was used to deliver the authentication factor. The possible values depend on the `type`:

          `magic_link` – Only `email`.

          `otp` – Only `sms`.

          `oauth` – Either `oauth_google` or `oauth_microsoft`.

          `password` – Only `knowledge`.

          `sso` – Either `sso_saml` or `sso_oidc`.

      - last_authenticated_at: The timestamp when the factor was last authenticated.
      - created_at: The timestamp when the factor was initially authenticated.
      - updated_at: The timestamp when the factor was last updated.
      - email_factor: Information about the email factor, if one is present.
      - phone_number_factor: Information about the phone number factor, if one is present.
      - google_oauth_factor: Information about the Google OAuth factor, if one is present.
      - microsoft_oauth_factor: Information about the Microsoft OAuth factor, if one is present.
      - apple_oauth_factor: (no documentation yet)
      - webauthn_factor: (no documentation yet)
      - authenticator_app_factor: Information about the TOTP-backed Authenticator App factor, if one is present.
      - github_oauth_factor: (no documentation yet)
      - recovery_code_factor: (no documentation yet)
      - facebook_oauth_factor: (no documentation yet)
      - crypto_wallet_factor: (no documentation yet)
      - amazon_oauth_factor: (no documentation yet)
      - bitbucket_oauth_factor: (no documentation yet)
      - coinbase_oauth_factor: (no documentation yet)
      - discord_oauth_factor: (no documentation yet)
      - figma_oauth_factor: (no documentation yet)
      - git_lab_oauth_factor: (no documentation yet)
      - instagram_oauth_factor: (no documentation yet)
      - linked_in_oauth_factor: (no documentation yet)
      - shopify_oauth_factor: (no documentation yet)
      - slack_oauth_factor: (no documentation yet)
      - snapchat_oauth_factor: (no documentation yet)
      - spotify_oauth_factor: (no documentation yet)
      - steam_oauth_factor: (no documentation yet)
      - tik_tok_oauth_factor: (no documentation yet)
      - twitch_oauth_factor: (no documentation yet)
      - twitter_oauth_factor: (no documentation yet)
      - embeddable_magic_link_factor: (no documentation yet)
      - biometric_factor: (no documentation yet)
      - saml_sso_factor: Information about the SAML SSO factor, if one is present.
      - oidc_sso_factor: Information about the OIDC SSO factor, if one is present.
      - salesforce_oauth_factor: (no documentation yet)
      - yahoo_oauth_factor: (no documentation yet)
      - hubspot_oauth_factor: (no documentation yet)
      - slack_oauth_exchange_factor: (no documentation yet)
      - hubspot_oauth_exchange_factor: (no documentation yet)
    """  # noqa

    type: AuthenticationFactorType
    delivery_method: AuthenticationFactorDeliveryMethod
    last_authenticated_at: Optional[datetime.datetime] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    email_factor: Optional[EmailFactor] = None
    phone_number_factor: Optional[PhoneNumberFactor] = None
    google_oauth_factor: Optional[GoogleOAuthFactor] = None
    microsoft_oauth_factor: Optional[MicrosoftOAuthFactor] = None
    apple_oauth_factor: Optional[AppleOAuthFactor] = None
    webauthn_factor: Optional[WebAuthnFactor] = None
    authenticator_app_factor: Optional[AuthenticatorAppFactor] = None
    github_oauth_factor: Optional[GithubOAuthFactor] = None
    recovery_code_factor: Optional[RecoveryCodeFactor] = None
    facebook_oauth_factor: Optional[FacebookOAuthFactor] = None
    crypto_wallet_factor: Optional[CryptoWalletFactor] = None
    amazon_oauth_factor: Optional[AmazonOAuthFactor] = None
    bitbucket_oauth_factor: Optional[BitbucketOAuthFactor] = None
    coinbase_oauth_factor: Optional[CoinbaseOAuthFactor] = None
    discord_oauth_factor: Optional[DiscordOAuthFactor] = None
    figma_oauth_factor: Optional[FigmaOAuthFactor] = None
    git_lab_oauth_factor: Optional[GitLabOAuthFactor] = None
    instagram_oauth_factor: Optional[InstagramOAuthFactor] = None
    linked_in_oauth_factor: Optional[LinkedInOAuthFactor] = None
    shopify_oauth_factor: Optional[ShopifyOAuthFactor] = None
    slack_oauth_factor: Optional[SlackOAuthFactor] = None
    snapchat_oauth_factor: Optional[SnapchatOAuthFactor] = None
    spotify_oauth_factor: Optional[SpotifyOAuthFactor] = None
    steam_oauth_factor: Optional[SteamOAuthFactor] = None
    tik_tok_oauth_factor: Optional[TikTokOAuthFactor] = None
    twitch_oauth_factor: Optional[TwitchOAuthFactor] = None
    twitter_oauth_factor: Optional[TwitterOAuthFactor] = None
    embeddable_magic_link_factor: Optional[EmbeddableMagicLinkFactor] = None
    biometric_factor: Optional[BiometricFactor] = None
    saml_sso_factor: Optional[SAMLSSOFactor] = None
    oidc_sso_factor: Optional[OIDCSSOFactor] = None
    salesforce_oauth_factor: Optional[SalesforceOAuthFactor] = None
    yahoo_oauth_factor: Optional[YahooOAuthFactor] = None
    hubspot_oauth_factor: Optional[HubspotOAuthFactor] = None
    slack_oauth_exchange_factor: Optional[SlackOAuthExchangeFactor] = None
    hubspot_oauth_exchange_factor: Optional[HubspotOAuthExchangeFactor] = None


class Session(pydantic.BaseModel):
    """
    Fields:
      - session_id: A unique identifier for a specific Session.
      - user_id: The unique ID of the affected User.
      - authentication_factors: An array of different authentication factors that comprise a Session.
      - started_at: The timestamp when the Session was created. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - last_accessed_at: The timestamp when the Session was last accessed. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - expires_at: The timestamp when the Session expires. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - attributes: Provided attributes help with fraud detection.
      - custom_claims: The custom claims map for a Session. Claims can be added to a session during a Sessions authenticate call.
    """  # noqa

    session_id: str
    user_id: str
    authentication_factors: List[AuthenticationFactor]
    started_at: Optional[datetime.datetime] = None
    last_accessed_at: Optional[datetime.datetime] = None
    expires_at: Optional[datetime.datetime] = None
    attributes: Optional[Attributes] = None
    custom_claims: Optional[Dict[str, Any]] = None


class AuthenticateResponse(ResponseBase):
    """Response type for `Sessions.authenticate`.
    Fields:
      - session: If you initiate a Session, by including `session_duration_minutes` in your authenticate call, you'll receive a full Session object in the response.

      See [GET sessions](https://stytch.com/docs/api/session-get) for complete response fields.

      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    session: Session
    session_token: str
    session_jwt: str
    user: User


class GetJWKSResponse(ResponseBase):
    """Response type for `Sessions.get_jwks`.
    Fields:
      - keys: The JWK
    """  # noqa

    keys: List[JWK]


class GetResponse(ResponseBase):
    """Response type for `Sessions.get`.
    Fields:
      - sessions: An array of Session objects.
    """  # noqa

    sessions: List[Session]


class RevokeResponse(ResponseBase):
    """Response type for `Sessions.revoke`.
    Fields:
    """  # noqa

# MANUAL(AuthenticateJWTLocalResponse)(Types)
class AuthenticateJWTLocalResponse(ResponseBase):
    session: Session
    session_jwt: str
# ENDMANUAL(AuthenticateJWTLocalResponse)