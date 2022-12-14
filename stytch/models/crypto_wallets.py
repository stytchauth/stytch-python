#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class AuthenticateStartResponse(ResponseBase):
    user_id: str
    challenge: str
    user_created: bool


class AuthenticateResponse(ResponseBase):
    user_id: str
    user: User
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
