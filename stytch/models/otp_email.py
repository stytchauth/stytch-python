#!/usr/bin/env python3


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


class SendResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str


class LoginOrCreateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str
    user_created: bool
