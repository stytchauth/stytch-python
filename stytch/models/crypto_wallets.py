#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class AuthenticateStartResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/crypto-wallet-authenticate-start)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: The user ID belonging to the user you associated with the request. If you did not supply a `user_id`, this will be a newly created user.

    - `challenge`: A `challenge` the user must sign as part of a call to `authenticate`

    - `user_created`: Whether or not a new user was created as part of this request
    """  # noqa

    user_id: str
    challenge: str
    user_created: bool


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/crypto-wallet-authenticate)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: The `user_id` of the authenticated user

    - `user`: The authenticated user

    - `session_jwt`: May be an empty string

    - `session_token`: May be an empty string

    - `session`: An optional `StytchSession`
    """  # noqa

    user_id: str
    user: User
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
