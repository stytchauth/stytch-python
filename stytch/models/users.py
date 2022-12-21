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
    """[Stytch docs](https://stytch.com/docs/api/create-user)"""  # noqa

    user_id: str
    user: User
    email_id: str
    phone_id: str
    status: str


class GetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/get-user)"""  # noqa

    user_id: str


class GetPendingResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/get-pending-users)"""  # noqa

    users: List[User]
    has_more: bool
    next_starting_after_id: str
    total: int


class SearchResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/search-users)"""  # noqa

    results: List[User]
    results_metadata: SearchResultsMetadata


class DeleteResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user)"""  # noqa

    user_id: str


class UpdateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/update-user)"""  # noqa

    user_id: str
    user: User
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    crypto_wallets: List[CryptoWallet]


class DeleteEmailResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-email)"""  # noqa

    user_id: str
    user: User


class DeletePhoneNumberResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-phone-number)"""  # noqa

    user_id: str
    user: User


class DeleteWebauthnRegistrationResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-webauthn-registration)"""  # noqa

    user_id: str
    user: User


class DeleteTotpResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-totp)"""  # noqa

    user_id: str
    user: User


class DeleteCryptoWalletResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-crypto-wallet)"""  # noqa

    user_id: str
    user: User


class DeletePasswordResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-password)"""  # noqa

    user_id: str
    user: User


class DeleteBiometricRegistrationResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-biometric-registration)"""  # noqa

    user_id: str
    user: User


class DeleteOauthUserRegistrationResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-oauth-registration)"""  # noqa

    user_id: str
    user: User
