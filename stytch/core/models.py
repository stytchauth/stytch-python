#!/usr/bin/env python3

import datetime
from typing import Any, Dict, List, Optional

import pydantic


class ResponseBase(pydantic.BaseModel):
    status_code: int
    # Optional because sessions/jwks doesn't have it currently
    request_id: Optional[str] = None

    @classmethod
    def from_json(cls, json: Dict[str, Any]):
        try:
            return cls(**json)
        except pydantic.ValidationError:
            # TODO: What if this one *also* fails?
            details = StytchErrorDetails(**json)
            raise StytchError(details) from None

    @property
    def is_informational(self) -> bool:
        return 100 <= self.status_code < 200

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    @property
    def is_redirection(self) -> bool:
        return 300 <= self.status_code < 400

    @property
    def is_client_error(self) -> bool:
        return 400 <= self.status_code < 500

    @property
    def is_server_error(self) -> bool:
        return 500 <= self.status_code < 600


class StytchErrorDetails(ResponseBase):
    error_type: str
    error_message: str
    error_url: str


class StytchError(Exception):
    def __init__(self, details: StytchErrorDetails) -> None:
        self.details = details

    def __repr__(self) -> str:
        return "StytchError {{{}}}".format(self.details)

    def __str__(self) -> str:
        return str(self.details)


class Name(pydantic.BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None


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


class StytchSession(pydantic.BaseModel):
    attributes: Optional[Dict[str, str]]
    authentication_factors: List[AuthenticationFactor]
    custom_claims: Optional[Dict[str, Any]]
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
    authenticator_type: Optional[str]
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
    name: Optional[Name]
    trusted_metadata: Optional[Dict[str, Any]]
    untrusted_metadata: Optional[Dict[str, Any]]
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    providers: List[OAuthProvider]
    webauthn_registrations: List[WebAuthnRegistration]
    biometric_registrations: List[BiometricRegistration]
    totps: List[TOTPInstance]
    crypto_wallets: List[CryptoWallet]
    password: Optional[Password]
    created_at: Optional[datetime.datetime]
    status: str


class SearchResultsMetadata(pydantic.BaseModel):
    next_cursor: Optional[str]
    total: int
