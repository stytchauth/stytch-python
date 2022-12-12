#!/usr/bin/env python3

from typing import Any, Dict, List

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


class GetResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    sessions: List[StytchSession]


class AuthenticateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    session: StytchSession


class RevokeResponse(pydantic.BaseModel):
    status_code: int
    request_id: str


class JwksResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    keys: List[Dict[str, Any]]
