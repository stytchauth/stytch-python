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


class SendResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    phone_id: str


class LoginOrCreateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    phone_id: str
    user_created: bool
