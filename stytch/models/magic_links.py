#!/usr/bin/env python3

from typing import Optional

from stytch.models.common import ResponseBase, StytchSession, User


class CreateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    method_id: str
    reset_sessions: bool
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
