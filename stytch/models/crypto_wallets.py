#!/usr/bin/env python3

from typing import Optional

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


class AuthenticateStartResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    challenge: str
    user_created: bool


class AuthenticateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
