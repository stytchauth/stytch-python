#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.models import ResponseBase, User


class CreateuserResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str
    status: str
    phone_id: str
    user: User


class GetpendingusersResponse(ResponseBase):
    request_id: str
    users: None
    has_more: bool
    next_starting_after_id: str
    total: None


class GetuserResponse(ResponseBase):
    request_id: str
    user_id: str
    name: None
    emails: None
    status: str
    phone_numbers: None
    birthday: None
    webauthn_registrations: None
    created_at: None
    providers: None
    totps: None
    crypto_wallets: None
    password: None
    biometric_registrations: None
    trusted_metadata: Optional[Dict[str, Any]] = None
    untrusted_metadata: Optional[Dict[str, Any]] = None
    project_id: str


class SearchusersexternalResponse(ResponseBase):
    request_id: str
    results: None
    ResultsMetadata: None
    next_cursor: Optional[str] = None


class UpdateuserResponse(ResponseBase):
    request_id: str
    user_id: str
    emails: None
    phone_numbers: None
    crypto_wallets: None
    user: User


class DeleteuserResponse(ResponseBase):
    request_id: str
    user_id: str


class GetuserbyemailandprojectidResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class DeleteuseremailResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User


class DeleteuserphonenumberResponse(ResponseBase):
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


class DeleteuseroauthuserregistrationResponse(ResponseBase):
    request_id: str
    user_id: str
    user: User
