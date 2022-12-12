#!/usr/bin/env python3

import datetime
from typing import Any, Dict, List, Optional

import pydantic


class Name(pydantic.BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]


class Operand(pydantic.BaseModel):
    filter_name: str
    filter_value: Any


class SearchQuery(pydantic.BaseModel):
    operator: str
    operands: List[Operand]


class EmailFactor(pydantic.BaseModel):
    email_address: str
    email_id: str


class AuthenticationFactor(pydantic.BaseModel):
    delivery_method: str
    email_factor: EmailFactor
    last_authenticated_at: datetime.datetime
    type: str


# TODO: Ensure that pydantic can handle extra keys
class StytchSession(pydantic.BaseModel):
    attributes: Dict[str, str]
    authentication_factors: List[AuthenticationFactor]
    custom_claims: Dict[str, Any]
    expires_at: datetime.datetime
    last_accessed_at: datetime.datetime
    session_id: str
    started_at: datetime.datetime
    user_id: str


class TOTPInstance(pydantic.BaseModel):
    totp_id: str
    verified: bool


class TOTPInstanceWithRecoveryCodes(TOTPInstance):
    recovery_codes: List[str]


class Email(pydantic.BaseModel):
    email_id: str
    email: str
    verified: bool


class PhoneNumber(pydantic.BaseModel):
    phone_id: str
    phone_number: str
    verified: bool


class OAuthProvider(pydantic.BaseModel):
    oauth_user_registration_id: str
    provider_subject: str
    provider_type: str
    profile_picture_url: str
    locale: str


class WebAuthnRegistration(pydantic.BaseModel):
    webauthn_registration_id: str
    domain: str
    user_agent: str
    authenticator_type: str
    verified: bool


class BiometricRegistration(pydantic.BaseModel):
    biometric_registration_id: str
    verified: bool


class CryptoWallet(pydantic.BaseModel):
    crypto_wallet_id: str
    crypto_wallet_address: str
    crypto_wallet_type: str
    verified: bool


class Password(pydantic.BaseModel):
    password_id: str
    requires_reset: bool


class User(pydantic.BaseModel):
    name: Name
    trusted_metadata: Dict[str, Any]
    untrusted_metadata: Dict[str, Any]
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    providers: List[OAuthProvider]
    webauthn_registrations: List[WebAuthnRegistration]
    biometric_registrations: List[BiometricRegistration]
    totps: List[TOTPInstance]
    crypto_wallets: List[CryptoWallet]
    password: Optional[Password]
    created_at: datetime.datetime
    status: str


class SearchResultsMetadata(pydantic.BaseModel):
    next_cursor: str
    total: int
