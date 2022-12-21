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

    secret: str
    totp_id: str
    qr_code: str
    recovery_codes: List[str]
    user_id: str
    user: Optional[User]


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-authenticate)"""  # noqa

    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]


class RecoveryCodesResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-get-recovery-codes)"""  # noqa

    user_id: str
    totps: List[TOTPInstanceWithRecoveryCodes]


class RecoverResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/totp-recover)"""  # noqa

    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
