# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import List, Optional

from stytch.b2b.models.discovery import DiscoveredOrganization
from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession, PrimaryRequired
from stytch.core.response_base import ResponseBase


class CreateRequestFirstPartyConnectedAppsAllowedType(str, enum.Enum):
    ALL_ALLOWED = "ALL_ALLOWED"
    RESTRICTED = "RESTRICTED"
    NOT_ALLOWED = "NOT_ALLOWED"


class CreateRequestThirdPartyConnectedAppsAllowedType(str, enum.Enum):
    ALL_ALLOWED = "ALL_ALLOWED"
    RESTRICTED = "RESTRICTED"
    NOT_ALLOWED = "NOT_ALLOWED"


class CreateResponse(ResponseBase):
    """Response type for `Organizations.create`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - intermediate_session_token: The returned Intermediate Session Token is identical to the one that was originally passed in to the request. If this value is non-empty, the member must complete an MFA step to finish logging in to the Organization. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. The token has a default expiry of 10 minutes. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member. Intermediate Session Tokens have a default expiry of 10 minutes.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
      - primary_required: Information about the primary authentication requirements of the Organization.
    """  # noqa

    member_id: str
    session_token: str
    session_jwt: str
    member: Member
    member_authenticated: bool
    intermediate_session_token: str
    member_session: Optional[MemberSession] = None
    organization: Optional[Organization] = None
    mfa_required: Optional[MfaRequired] = None
    primary_required: Optional[PrimaryRequired] = None


class ListResponse(ResponseBase):
    """Response type for `Organizations.list`.
    Fields:
      - email_address: The email address.
      - discovered_organizations: An array of `discovered_organization` objects tied to the `intermediate_session_token`, `session_token`, or `session_jwt`. See the [Discovered Organization Object](https://stytch.com/docs/b2b/api/discovered-organization-object) for complete details.

      Note that Organizations will only appear here under any of the following conditions:
      1. The end user is already a Member of the Organization.
      2. The end user is invited to the Organization.
      3. The end user can join the Organization because:

          a) The Organization allows JIT provisioning.

          b) The Organizations' allowed domains list contains the Member's email domain.

          c) The Organization has at least one other Member with a verified email address with the same domain as the end user (to prevent phishing attacks).
      - organization_id_hint: If the intermediate session token is associated with a specific Organization, that Organization ID will be returned here. The Organization ID will be null if the intermediate session token was generated by a email magic link discovery or OAuth discovery flow. If a session token or session JWT is provided, the Organization ID hint will be null.
    """  # noqa

    email_address: str
    discovered_organizations: List[DiscoveredOrganization]
    organization_id_hint: Optional[str] = None
