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

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.consumer.models.sessions import JWK, AuthenticationFactor
from stytch.core.response_base import ResponseBase


class ExchangeRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class AuthorizationCheck(pydantic.BaseModel):
    """
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - resource_id: A unique identifier of the RBAC Resource, provided by the developer and intended to be human-readable.

      A `resource_id` is not allowed to start with `stytch`, which is a special prefix used for Stytch default Resources with reserved  `resource_id`s. These include:

      * `stytch.organization`
      * `stytch.member`
      * `stytch.sso`
      * `stytch.self`

      Check out the [guide on Stytch default Resources](https://stytch.com/docs/b2b/guides/rbac/stytch-defaults) for a more detailed explanation.


      - action: An action to take on a Resource.
    """  # noqa

    organization_id: str
    resource_id: str
    action: str


class AuthorizationVerdict(pydantic.BaseModel):
    authorized: bool
    granting_roles: List[str]


class MemberSession(pydantic.BaseModel):
    """
    Fields:
      - member_session_id: Globally unique UUID that identifies a specific Session.
      - member_id: Globally unique UUID that identifies a specific Member.
      - started_at: The timestamp when the Session was created. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - last_accessed_at: The timestamp when the Session was last accessed. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - expires_at: The timestamp when the Session expires. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - authentication_factors: An array of different authentication factors that comprise a Session.
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - roles: (no documentation yet)
      - custom_claims: The custom claims map for a Session. Claims can be added to a session during a Sessions authenticate call.
    """  # noqa

    member_session_id: str
    member_id: str
    started_at: datetime.datetime
    last_accessed_at: datetime.datetime
    expires_at: datetime.datetime
    authentication_factors: List[AuthenticationFactor]
    organization_id: str
    roles: List[str]
    custom_claims: Optional[Dict[str, Any]] = None


class PrimaryRequired(pydantic.BaseModel):
    """
    Fields:
      - allowed_auth_methods: If non-empty, indicates that the Organization restricts the authentication methods it allows for login (such as `sso` or `password`), and the end user must complete one of those authentication methods to log in. If empty, indicates that the Organization does not restrict the authentication method it allows for login, but the end user does not have any transferrable primary factors. Only email magic link and OAuth factors can be transferred between Organizations.
    """  # noqa

    allowed_auth_methods: List[str]


class AuthenticateResponse(ResponseBase):
    """Response type for `Sessions.authenticate`.
    Fields:
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - verdict: If an `authorization_check` is provided in the request and the check succeeds, this field will return
      the complete list of Roles that gave the Member permission to perform the specified action on the specified Resource.
    """  # noqa

    member_session: MemberSession
    session_token: str
    session_jwt: str
    member: Member
    organization: Organization
    verdict: Optional[AuthorizationVerdict] = None


class ExchangeResponse(ResponseBase):
    """Response type for `Sessions.exchange`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - intermediate_session_token: The returned Intermediate Session Token contains any Email Magic Link or OAuth factors from the original member session that are valid for the target Organization. If this value is non-empty, the member must complete an MFA step to finish logging in to the Organization. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
      - primary_required: (no documentation yet)
    """  # noqa

    member_id: str
    member_session: MemberSession
    session_token: str
    session_jwt: str
    member: Member
    organization: Organization
    member_authenticated: bool
    intermediate_session_token: str
    mfa_required: Optional[MfaRequired] = None
    primary_required: Optional[PrimaryRequired] = None


class GetJWKSResponse(ResponseBase):
    """Response type for `Sessions.get_jwks`.
    Fields:
      - keys: The JWK
    """  # noqa

    keys: List[JWK]


class GetResponse(ResponseBase):
    """Response type for `Sessions.get`.
    Fields:
      - member_sessions: An array of [Session objects](https://stytch.com/docs/b2b/api/session-object).
    """  # noqa

    member_sessions: List[MemberSession]


class RevokeResponse(ResponseBase):
    """Response type for `Sessions.revoke`.
    Fields:
    """  # noqa


# MANUAL(LocalJWTResponse)(Types)
class LocalJWTResponse(pydantic.BaseModel):
    member_session: MemberSession
    roles_claim: Optional[List[str]]


# ENDMANUAL(LocalJWTResponse)
