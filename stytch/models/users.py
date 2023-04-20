#!/usr/bin/env python3

from typing import Any, Dict, List, Optional

from stytch.core.models import ResponseBase, TOTPInstance, User


class CreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/create-user)"""  # noqa

    request_id: str
    user_id: str
    email_id: str
    status: str
    phone_id: str
    user: User


class GetpendingusersResponse(ResponseBase):
    request_id: str
    users: TODO
    has_more: bool
    next_starting_after_id: str
    total: TODO


class GetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/get-user)"""  # noqa

    request_id: str
    user_id: str
    name: TODO
    emails: TODO
    status: str
    phone_numbers: TODO
    birthday: TODO
    webauthn_registrations: TODO
    created_at: TODO
    providers: TODO
    totps: List[TOTPInstance]
    crypto_wallets: TODO
    password: TODO
    biometric_registrations: TODO
    trusted_metadata: Optional[Dict[str, Any]] = None
    untrusted_metadata: Optional[Dict[str, Any]] = None
    project_id: str


class SearchusersexternalResponse(ResponseBase):
    request_id: str
    results: TODO
    results_metadata: ResultsMetadata


class UpdateuserResponse(ResponseBase):
    request_id: str
    user_id: str
    emails: TODO
    phone_numbers: TODO
    crypto_wallets: TODO
    user: User


class DeleteuserResponse(ResponseBase):
    request_id: str
    user_id: str


class GetbyemailandprojectidResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class DeleteEmailResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-email)"""  # noqa

    request_id: str
    user_id: str
    user: User


class DeletePhoneNumberResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-phone-number)"""  # noqa

    request_id: str
    user_id: str
    user: User


class DeleteuserwebauthnregistrationResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User


class DeleteuserbiometricregistrationResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User


class DeleteusertotpResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User


class DeleteusercryptowalletResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User


class DeleteuserpasswordResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User


class DeleteOauthUserRegistrationResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/delete-user-oauth-registration)"""  # noqa

    request_id: str
    user_id: str
    user: User
