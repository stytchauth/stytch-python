#!/usr/bin/env python3

from typing import Optional

from stytch.b2b.core.models import B2BStytchSession, Member, Organization
from stytch.core.models import ResponseBase


class ResetResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_session`: The B2BStytchSession object.

    - `member`: The Member object.

    - `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

    - `organization`: The Organization object.
    """  # noqa

    member: Member
    member_id: str
    organization: Organization
    member_session: Optional[B2BStytchSession]
