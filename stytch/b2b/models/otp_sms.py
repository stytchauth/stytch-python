# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Optional

from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class SendRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"
    FR = "fr"
    IT = "it"
    DEDE = "de-DE"
    ZHHANS = "zh-Hans"
    CAES = "ca-ES"


class AuthenticateResponse(ResponseBase):
    """Response type for `Sms.authenticate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
    session_token: str
    session_jwt: str
    member_session: Optional[MemberSession] = None


class SendResponse(ResponseBase):
    """Response type for `Sms.send`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
