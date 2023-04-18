#!/usr/bin/env python3


from stytch.b2b.core.models import Member, Organization
from stytch.core.models import ResponseBase


class LoginOrSignupResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

    - `member_created`: A flag indicating `true` if a new Member object was created and `false` if the Member object already existed.

    - `member`: The Member object.

    - `organization`: The Organization object.
    """  # noqa

    member_id: str
    member_created: bool
    member: Member
    organization: Organization


class InviteResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member. The member_id is critical to perform operations on a Member, so be sure to preserve this value.
    - `member`: The Member object.
    - `organization`: The Organization object.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
