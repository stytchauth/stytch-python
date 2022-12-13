#!/usr/bin/env python3

from typing import Any, Dict, List


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


class GetResponse(ResponseBase):
    status_code: int
    request_id: str
    sessions: List[StytchSession]


class AuthenticateResponse(ResponseBase):
    status_code: int
    request_id: str
    session: StytchSession


class RevokeResponse(ResponseBase):
    status_code: int
    request_id: str


class JwksResponse(ResponseBase):
    status_code: int
    request_id: str
    keys: List[Dict[str, Any]]
