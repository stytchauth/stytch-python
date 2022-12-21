#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/oauth-authenticate)

    Response fields beyond those defined in `ResponseBase`:

    - `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

    - `user`: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field detail.

    - `oauth_user_registration_id`: Globally unique UUID that identifies singluar registration of a user with an OAuth identity provider in the Stytch API.

    - `provider_subject`: The `provider_subject` field is the unique identifier used to identify the user within a given OAuth provider. Also commonly called the "sub" or "Subject field" in OAuth protocols.

    - `provider_type`: The `provider_type` field denotes the OAuth identity provider that the user has authenticated with, e.g. Google, Facebook, GitHub etc.

    - `provider_values`: The `provider_values` object lists relevant identifiers, values, and scopes for a given OAuth provider. For example this object will include a provider's `access_token` that you can use to access the provider's API for a given user.

      Note that these values will vary based on the OAuth provider in question, e.g. `id_token` is only returned by Microsoft.

    - `reset_sessions`: Indicates if all other of this user's sessions need to be reset. You should check this field if you aren't using Stytch's Session product. If you are using Stytch's Session product, we revoke the user's other sessions for you.

    - `session`: If you initiate a session, by including `session_duration_minutes` in your authenticate call, you'll receive a full session object in the response.

      See [GET sessions](https://stytch.com/docs/api/session-get) for complete response fields.

    - `session_token`: A secret token for a given Stytch session. Read more about `session_token` in our [session management guide](https://stytch.com/docs/sessions#using-sessions).

    - `session_jwt`: The JSON Web Token (JWT) for a given Stytch session. Read more about JWTs in our [session management guide](https://stytch.com/docs/sessions#using-sessions).
    """  # noqa

    user_id: str
    user: Optional[User]
    oauth_user_registration_id: str
    provider_subject: str
    provider_type: str
    provider_values: Optional[Dict[str, Any]]
    reset_sessions: bool
    session: Optional[StytchSession]
    session_jwt: str
    session_token: str


class AttachResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/oauth-overview)"""  # noqa

    oauth_attach_token: str
