#!/usr/bin/env python3

import pydantic

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
    SearchQuery,
    SearchResultsMetadata,
    StytchSession,
    TOTPInstance,
    TOTPInstanceWithRecoveryCodes,
    User,
    WebAuthnRegistration,
)


class CreateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    secret: str
    totp_id: str
    qr_code: str
    recovery_codes: List[str]
    user_id: str
    user: User


class AuthenticateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]


class RecoveryCodesResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    totps: List[TOTPInstanceWithRecoveryCodes]


class RecoverResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
    totp_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
