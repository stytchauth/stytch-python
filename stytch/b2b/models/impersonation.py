# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Optional

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class AuthenticateResponse(ResponseBase):
    member_id: str
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    organization: Organization
    intermediate_session_token: str
    member_authenticated: bool
    member_session: Optional[MemberSession] = None
    mfa_required: Optional[MfaRequired] = None
