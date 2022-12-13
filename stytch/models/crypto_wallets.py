#!/usr/bin/env python3

from typing import Optional

from stytch.models.common import ResponseBase, StytchSession, User


class AuthenticateStartResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    challenge: str
    user_created: bool


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
