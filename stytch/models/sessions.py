#!/usr/bin/env python3

from typing import Any, Dict, List

from stytch.core.models import ResponseBase, StytchSession


class GetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-get)"""  # noqa

    sessions: List[StytchSession]


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-auth)"""  # noqa

    session: StytchSession


class RevokeResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/session-revoke)"""  # noqa


class JwksResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/jwks-get)"""  # noqa

    keys: List[Dict[str, Any]]
