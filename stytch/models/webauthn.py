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


class RegisterStartResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    public_key_credential_creation_options: str


class RegisterResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    webauthn_registration_id: str


class AuthenticateStartResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    public_key_credential_request_options: str


class AuthenticateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
    webauthn_registration_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
