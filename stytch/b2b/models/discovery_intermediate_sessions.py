#!/usr/bin/env python3

from typing import Optional

from stytch.b2b.core.models import B2BStytchSession, Member, Organization
from stytch.core.models import ResponseBase


class ExchangeResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: The UUID of the new Member that was created.

    - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session management guide.

    - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session management guide.

    - `member_session`: The B2BStytchSession object.

    - `member`: The [Member](https://stytch.com/docs/b2b/api/member-object) object.

    - `organization`: The [Organization](https://stytch.com/docs/b2b/api/organization-object) object.
    """  # noqa

    member_id: str
    member_session: Optional[B2BStytchSession]
    session_token: str
    session_jwt: str
    member: Member
    organization: Organization
