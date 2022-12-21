#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class SendResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/send-by-email)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

    - `email_id`: Globally unique UUID that identifies a specific email address in the Stytch API. The `email_id` is used when you need to operate on a specific user's email address, e.g. to delete the email address from the Stytch user.
    """  # noqa

    user_id: str
    email_id: str


class LoginOrCreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/log-in-or-create-user-by-email)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

    - `email_id`: Globally unique UUID that identifies a specific email address in the Stytch API. The `email_id` is used when you need to operate on a specific user's email address, e.g. to delete the email address from the Stytch user.

    - `user_created`: In `login_or_create` endpoints, this field indicates whether or not a user was freshly created or the user went through a login path.
    """  # noqa

    user_id: str
    email_id: str
    user_created: bool


class InviteResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/invite-by-email)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

    - `email_id`: Globally unique UUID that identifies a specific email address in the Stytch API. The `email_id` is used when you need to operate on a specific user's email address, e.g. to delete the email address from the Stytch user.
    """  # noqa

    user_id: str
    email_id: str


class RevokeInviteResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/revoke-pending-invite)

    There are no response fields beyond those defined in `ResponseBase`
    """  # noqa
