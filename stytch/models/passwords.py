#!/usr/bin/env python3

from typing import Any, Dict, Optional


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
    user_id: str
    email_id: str


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]


class StrengthCheckResponse(ResponseBase):
    status_code: int
    request_id: str
    valid_password: bool
    score: int
    breached_password: bool
    feedback: Dict[str, Any]


class MigrateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str
    user_created: bool
