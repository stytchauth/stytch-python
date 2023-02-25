#!/usr/bin/env python3


from stytch.b2b.core.models import Member
from stytch.core.models import ResponseBase


class LoginOrSignupResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

    - `member_created`: Boolean if a Member already exists with that email.

    - `member`: The Member object.
    """  # noqa

    member_id: str
    member_created: bool
    member: Member


class InviteResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member. The member_id is critical to perform operations on a Member, so be sure to preserve this value.
    - `member`: The Member object.
    """  # noqa

    member_id: str
    member: Member
