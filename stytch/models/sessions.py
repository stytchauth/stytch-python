#!/usr/bin/env python3

from typing import Any, Dict, List

from stytch.core.models import ResponseBase, StytchSession


class GetResponse(ResponseBase):
    sessions: List[StytchSession]


class AuthenticateResponse(ResponseBase):
    session: StytchSession


class RevokeResponse(ResponseBase):
    pass


class JwksResponse(ResponseBase):
    keys: List[Dict[str, Any]]
