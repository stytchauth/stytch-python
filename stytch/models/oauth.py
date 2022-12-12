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


class AuthenticateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
    oauth_user_registration_id: str
    provider_subject: str
    provider_type: str
    provider_values: Dict[str, Any]
    reset_sessions: bool
    session: Optional[StytchSession]
    session_jwt: str
    session_token: str
