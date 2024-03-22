# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Optional

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession, PrimaryRequired
from stytch.core.response_base import ResponseBase


class ExchangeRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class ExchangeResponse(ResponseBase):
    """Response type for `IntermediateSessions.exchange`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - intermediate_session_token: The returned Intermediate Session Token is identical to the one that was originally passed in to the request.
          The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp),
          or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete the MFA flow and log in to the Organization.
          It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a different existing Organization,
          or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
      - primary_required: (no documentation yet)
    """  # noqa

    member_id: str
    session_token: str
    session_jwt: str
    member: Member
    organization: Organization
    member_authenticated: bool
    intermediate_session_token: str
    member_session: Optional[MemberSession] = None
    mfa_required: Optional[MfaRequired] = None
    primary_required: Optional[PrimaryRequired] = None
