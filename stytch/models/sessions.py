#!/usr/bin/env python3

from typing import Any, Dict, List, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class GetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-get)"""  # noqa

    sessions: List[StytchSession]


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-auth)

    NOTE: The response object should always have the user field set (ie, it will not be None), but due to backwards
    compatibility with the `sessions.authenticate_jwt` method, the AuthenticateResponse marks it as Optional. The caller
    should always check since the field is Optional, but the intention is that it will _not_ be None.
    """  # noqa

    session: StytchSession
    session_jwt: str
    session_token: str
    user: Optional[User]


class RevokeResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-revoke)"""  # noqa


class JwksResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/jwks-get)"""  # noqa

    keys: List[Dict[str, Any]]
