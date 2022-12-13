#!/usr/bin/env python3

from typing import List, Optional


from stytch.models.common import (
    AuthenticationFactor,
    BiometricRegistration,
    CryptoWallet,
    Email,
    EmailFactor,
    Name,
    OAuthProvider,
    Operand,
    Password,
    PhoneNumber,
    ResponseBase,
    SearchQuery,
    SearchResultsMetadata,
    StytchSession,
    TOTPInstance,
    TOTPInstanceWithRecoveryCodes,
    User,
    WebAuthnRegistration,
)


class CreateResponse(ResponseBase):
    status_code: int
    request_id: str
    secret: str
    totp_id: str
    qr_code: str
    recovery_codes: List[str]
    user_id: str
    user: User


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]


class RecoveryCodesResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    totps: List[TOTPInstanceWithRecoveryCodes]


class RecoverResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
