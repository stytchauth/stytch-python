#!/usr/bin/env python3

from typing import List

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
    user_id: str
    user: User
    email_id: str
    phone_id: str
    status: str


class GetResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str


class GetPendingResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    users: List[User]
    has_more: bool
    next_starting_after_id: str
    total: int


class SearchResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    results: List[User]
    results_metadata: SearchResultsMetadata


class DeleteResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str


class UpdateResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    crypto_wallets: List[CryptoWallet]


class DeleteEmailResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeletePhoneNumberResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteWebauthnRegistrationResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteTotpResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteCryptoWalletResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeletePasswordResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteBiometricRegistrationResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteOauthUserRegistrationResponse(pydantic.BaseModel):
    status_code: int
    request_id: str
    user_id: str
    user: User
