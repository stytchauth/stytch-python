#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class CreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/create-magic-link)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

    - `token`: The magic link token that you'll include in your contact method of choice, e.g. email or SMS. Check out our [Embeddable magic link guide](https://stytch.com/docs/api/magic-links#embeddable-magic-links_embeddable-overview) for more detail on where to include the token.
    """  # noqa

    status_code: int
    request_id: str
    user_id: str


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/authenticate-magic-link)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

    - `user`: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field detail.

    - `reset_sessions`: Indicates if all other of this user's sessions need to be reset. You should check this field if you aren't using Stytch's Session product. If you are using Stytch's Session product, we revoke the user's other sessions for you.

    - `session_jwt`: The JSON Web Token (JWT) for a given Stytch session. Read more about JWTs in our [session management guide](https://stytch.com/docs/sessions#using-sessions).

    - `session_token`: A secret token for a given Stytch session. Read more about `session_token` in our [session management guide](https://stytch.com/docs/sessions#using-sessions).

    - `session`: If you initiate a session, by including `session_duration_minutes` in your authenticate call, you'll receive a full session object in the response.
      See [GET sessions](https://stytch.com/docs/api/session-get) for complete response fields.
    """  # noqa

    status_code: int
    request_id: str
    user_id: str
    user: User
    method_id: str
    reset_sessions: bool
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
