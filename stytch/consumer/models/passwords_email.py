# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Optional

from stytch.consumer.models.sessions import Session
from stytch.consumer.models.users import User
from stytch.core.response_base import ResponseBase


class ResetStartRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"
    FR = "fr"


class ResetResponse(ResponseBase):
    """Response type for `Email.reset`.
    Fields:
      - user_id: The unique ID of the affected User.
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
      - session: If you initiate a Session, by including `session_duration_minutes` in your authenticate call, you'll receive a full Session object in the response.

      See [Session object](https://stytch.com/docs/api/session-object) for complete response fields.

    """  # noqa

    user_id: str
    session_token: str
    session_jwt: str
    user: User
    session: Optional[Session] = None


class ResetStartResponse(ResponseBase):
    """Response type for `Email.reset_start`.
    Fields:
      - user_id: The unique ID of the affected User.
      - email_id: The unique ID of a specific email address.
    """  # noqa

    user_id: str
    email_id: str
