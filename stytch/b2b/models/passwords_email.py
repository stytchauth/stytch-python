# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Dict, Optional

import pydantic

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase
from stytch.shared.method_options import Authorization


class ResetRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class ResetStartRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class RequireResetRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class RequireResetResponse(ResponseBase):
    """Response type for `Email.require_reset`.
    Fields:
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - member_id: Globally unique UUID that identifies a specific Member.
    """  # noqa

    member: Member
    organization: Organization
    member_id: Optional[str] = None


class ResetResponse(ResponseBase):
    """Response type for `Email.reset`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member_email_id: Globally unique UUID that identifies a member's email
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - intermediate_session_token: The returned Intermediate Session Token contains a password factor associated with the Member. If this value is non-empty, the member must complete an MFA step to finish logging in to the Organization. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. Password factors are not transferable between Organizations, so the intermediate session token is not valid for use with discovery endpoints.
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
    """  # noqa

    member_id: str
    member_email_id: str
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    organization: Organization
    intermediate_session_token: str
    member_authenticated: bool
    member_session: Optional[MemberSession] = None
    mfa_required: Optional[MfaRequired] = None


class ResetStartResponse(ResponseBase):
    """Response type for `Email.reset_start`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member_email_id: Globally unique UUID that identifies a member's email
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
    """  # noqa

    member_id: str
    member_email_id: str
    member: Member
