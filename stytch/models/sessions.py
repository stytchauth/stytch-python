#!/usr/bin/env python3

from typing import Any, Dict, List

from stytch.models.common import ResponseBase, StytchSession


class GetResponse(ResponseBase):
    status_code: int
    request_id: str
    sessions: List[StytchSession]


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    session: StytchSession


class RevokeResponse(ResponseBase):
    status_code: int
    request_id: str


class JwksResponse(ResponseBase):
    status_code: int
    request_id: str
    keys: List[Dict[str, Any]]
