#!/usr/bin/env python3

from typing import Optional

from stytch.b2b.core.models import B2BStytchSession, Member
from stytch.core.models import ResponseBase


class AuthenticateResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

    - `method_id`: The email_id or phone_id involved in the given authentication.

    - `reset_sessions`: Indicates if all Sessions linked to the Member need to be reset. You should check this field if you aren't using Stytch's Session product. If you are using Stytch's Session product, we revoke the Member’s other Sessions for you.

    - `organization_id`: Globally unique UUID that identifies a specific Organization in the Stytch API. The organization_id is critical to perform operations on an Organization so be sure to preserve this value.

    - `member`: The Member object.

    - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session management guide.

    - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session management guide.

    - `member_session`: The B2BStytchSession object.
    """  # noqa

    member_id: str
    method_id: str
    reset_sessions: bool
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    member_session: Optional[B2BStytchSession]
