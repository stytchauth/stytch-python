#!/usr/bin/env python3

from typing import Optional


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
    status_code: int
    request_id: str
    user_id: str
    email_id: str


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    status_code: int
    request_id: str
    user_id: str
    user: User
    method_id: str
    reset_sessions: bool
    session_jwt: str
    session_token: str
    session: Optional[str]
