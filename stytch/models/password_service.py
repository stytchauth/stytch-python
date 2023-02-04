#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class PasswordscreateResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User


class PasswordsauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User


class PasswordsstrengthcheckResponse(ResponseBase):
    request_id: str
    valid_password: bool
    score: None
    breached_password: bool
    feedback: None


class PasswordsemailresetstartResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class PasswordsemailresetResponse(ResponseBase):
    request_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User


class PasswordsexistingpasswordresetResponse(ResponseBase):
    request_id: str
    user_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User


class PasswordssessionresetResponse(ResponseBase):
    request_id: str
    user_id: str
    session: Optional[StytchSession]
    user: User


class PasswordsmigrateResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str
    user_created: bool
    user: User
