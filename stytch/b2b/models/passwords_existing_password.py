#!/usr/bin/env python3

from typing import Optional

from stytch.b2b.core.models import B2BStytchSession, Member, Organization
from stytch.core.models import ResponseBase


class ResetResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_session`: The B2BStytchSession object.

    - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session management guide.

    - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

    - `organization_id`: Globally unique UUID that identifies a specific Organization in the Stytch API. The organization_id is critical to perform operations on an Organization so be sure to preserve this value.

    - `member`: The Member object.

    - `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

    - `organization`: The Organization object.
    """  # noqa

    member: Member
    member_id: str
    organization_id: str
    organization: Organization
    session_token: str
    session_jwt: str
    member_session: Optional[B2BStytchSession]
