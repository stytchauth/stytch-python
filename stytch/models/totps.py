#!/usr/bin/env python3

from typing import List, Optional

from stytch.core.models import (
    ResponseBase,
    StytchSession,
    TOTPInstanceWithRecoveryCodes,
    User,
)


class CreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-create)"""  # noqa

    request_id: str
    totp_id: str
    secret: str
    qr_code: str
    recovery_codes: List[str]
    user: User
    user_id: str


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-authenticate)"""  # noqa

    request_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    totp_id: str
    session_jwt: str
    user: User


class RecoveryCodesResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-get-recovery-codes)"""  # noqa

    request_id: str
    user_id: str
    totps: List[TOTPInstanceWithRecoveryCodes]


class RecoverResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-recover)"""  # noqa

    request_id: str
    totp_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
