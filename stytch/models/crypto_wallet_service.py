#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class CryptowalletsauthenticatestartResponse(ResponseBase):
    request_id: str
    user_id: str
    challenge: str
    user_created: bool


class CryptowalletsauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
