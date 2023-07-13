# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Optional

import pydantic

from stytch.consumer.models.sessions import Session
from stytch.consumer.models.users import User
from stytch.core.response_base import ResponseBase


class Options(pydantic.BaseModel):
    """
    Fields:
      - ip_match_required: Require that the IP address the Magic Link was requested from matches the IP address it's clicked from.
      - user_agent_match_required: Require that the user agent the Magic Link was requested from matches the user agent it's clicked from.
    """  # noqa

    ip_match_required: bool
    user_agent_match_required: bool


class AuthenticateResponse(ResponseBase):
    """Response type for `MagicLinks.authenticate`.
    Fields:
      - user_id: The unique ID of the affected User.
      - method_id: The `email_id` or `phone_id` involved in the given authentication.
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
      - reset_sessions: Indicates if all other of the User's Sessions need to be reset. You should check this field if you aren't using Stytch's Session product. If you are using Stytch's Session product, we revoke the User's other sessions for you.
      - session: If you initiate a Session, by including `session_duration_minutes` in your authenticate call, you'll receive a full Session object in the response.

      See [GET sessions](https://stytch.com/docs/api/session-get) for complete response fields.

    """  # noqa

    user_id: str
    method_id: str
    session_token: str
    session_jwt: str
    user: User
    reset_sessions: bool
    session: Optional[Session] = None


class CreateResponse(ResponseBase):
    """Response type for `MagicLinks.create`.
    Fields:
      - user_id: The unique ID of the affected User.
      - token: The Magic Link `token` that you'll include in your contact method of choice, e.g. email or SMS.
    """  # noqa

    user_id: str
    token: str
