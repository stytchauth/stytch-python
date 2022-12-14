#!/usr/bin/env python3

from typing import List

from stytch.core.models import (
    CryptoWallet,
    Email,
    PhoneNumber,
    ResponseBase,
    SearchResultsMetadata,
    User,
)


class CreateResponse(ResponseBase):
    user_id: str
    user: User
    email_id: str
    phone_id: str
    status: str


class GetResponse(ResponseBase):
    user_id: str


class GetPendingResponse(ResponseBase):
    users: List[User]
    has_more: bool
    next_starting_after_id: str
    total: int


class SearchResponse(ResponseBase):
    results: List[User]
    results_metadata: SearchResultsMetadata


class DeleteResponse(ResponseBase):
    user_id: str


class UpdateResponse(ResponseBase):
    user_id: str
    user: User
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    crypto_wallets: List[CryptoWallet]


class DeleteEmailResponse(ResponseBase):
    user_id: str
    user: User


class DeletePhoneNumberResponse(ResponseBase):
    user_id: str
    user: User


class DeleteWebauthnRegistrationResponse(ResponseBase):
    user_id: str
    user: User


class DeleteTotpResponse(ResponseBase):
    user_id: str
    user: User


class DeleteCryptoWalletResponse(ResponseBase):
    user_id: str
    user: User


class DeletePasswordResponse(ResponseBase):
    user_id: str
    user: User


class DeleteBiometricRegistrationResponse(ResponseBase):
    user_id: str
    user: User


class DeleteOauthUserRegistrationResponse(ResponseBase):
    user_id: str
    user: User
