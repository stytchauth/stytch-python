#!/usr/bin/env python3

from typing import List

from stytch.models.common import (
    CryptoWallet,
    Email,
    PhoneNumber,
    ResponseBase,
    SearchResultsMetadata,
    User,
)


class CreateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    email_id: str
    phone_id: str
    status: str


class GetResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str


class GetPendingResponse(ResponseBase):
    status_code: int
    request_id: str
    users: List[User]
    has_more: bool
    next_starting_after_id: str
    total: int


class SearchResponse(ResponseBase):
    status_code: int
    request_id: str
    results: List[User]
    results_metadata: SearchResultsMetadata


class DeleteResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str


class UpdateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    crypto_wallets: List[CryptoWallet]


class DeleteEmailResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeletePhoneNumberResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteWebauthnRegistrationResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteTotpResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteCryptoWalletResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeletePasswordResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteBiometricRegistrationResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User


class DeleteOauthUserRegistrationResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    user: User
