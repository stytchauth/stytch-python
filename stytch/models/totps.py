#!/usr/bin/env python3

from typing import List, Optional

from stytch.core.models import (
    ResponseBase,
    StytchSession,
    TOTPInstanceWithRecoveryCodes,
    User,
)


class CreateResponse(ResponseBase):
    secret: str
    totp_id: str
    qr_code: str
    recovery_codes: List[str]
    user_id: str
    user: Optional[User]


class AuthenticateResponse(ResponseBase):
    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]


class RecoveryCodesResponse(ResponseBase):
    user_id: str
    totps: List[TOTPInstanceWithRecoveryCodes]


class RecoverResponse(ResponseBase):
    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
