#!/usr/bin/env python3

from typing import Any, Dict, List, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class GetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-get)"""  # noqa

    sessions: List[StytchSession]


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-auth)"""  # noqa

    session: StytchSession
    session_jwt: str
    session_token: str
    user: Optional[User]


class RevokeResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-revoke)"""  # noqa


class JwksResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/jwks-get)"""  # noqa

    keys: List[Dict[str, Any]]
