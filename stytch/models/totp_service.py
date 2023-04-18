#!/usr/bin/env python3

from typing import List, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class TotpscreateResponse(ResponseBase):
    request_id: str
    totp_id: str
    secret: str
    qr_code: str
    recovery_codes: List[str]
    user: User
    user_id: str


class TotpsauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    totp_id: str
    session_jwt: str
    user: User


class TotpsgetrecoverycodesResponse(ResponseBase):
    request_id: str
    user_id: str
    totps: None


class TotpsrecoverResponse(ResponseBase):
    request_id: str
    totp_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
