#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class BiometricsregisterstartResponse(ResponseBase):
    request_id: str
    user_id: str
    biometric_registration_id: str
    challenge: str


class BiometricsregisterResponse(ResponseBase):
    request_id: str
    user_id: str
    biometric_registration_id: str
    user: User
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str


class BiometricsauthenticatestartResponse(ResponseBase):
    request_id: str
    user_id: str
    biometric_registration_id: str
    challenge: str


class BiometricsauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    biometric_registration_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
