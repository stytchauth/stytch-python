#!/usr/bin/env python3

from typing import List

from stytch.b2b.core.models import B2BStytchSession, Member
from stytch.core.models import ResponseBase


class GetResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `sessions`: An array of B2BStytchSession objects
    """  # noqa

    member_sessions: List[B2BStytchSession]


class AuthenticateResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_session`: The Session object.

    - `session_token`: A secret token for a given Stytch Session. Read more about Session_token in our Session management guide.

    - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our session management guide.

    - `member`: The Member object.
    """  # noqa

    member_session: B2BStytchSession
    session_token: str
    session_jwt: str
    member: Member


class RevokeResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    (None)
    """  # noqa
