#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class AuthenticateResponse(ResponseBase):
    user_id: str
    user: User
    method_id: str
    reset_sessions: bool
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
