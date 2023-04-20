#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class WebauthnregisterstartResponse(ResponseBase):
    request_id: str
    user_id: str
    public_key_credential_creation_options: str


class WebauthnregisterResponse(ResponseBase):
    request_id: str
    user_id: str
    webauthn_registration_id: str


class WebauthnauthenticatestartResponse(ResponseBase):
    request_id: str
    user_id: str
    public_key_credential_request_options: str


class WebauthnauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    webauthn_registration_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
