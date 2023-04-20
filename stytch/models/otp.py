#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class OtpssmssendResponse(ResponseBase):
    request_id: str
    user_id: str
    phone_id: str


class OtpssmsloginorcreateResponse(ResponseBase):
    request_id: str
    user_id: str
    phone_id: str
    user_created: bool


class OtpswhatsappsendResponse(ResponseBase):
    request_id: str
    user_id: str
    phone_id: str


class OtpswhatsapploginorcreateResponse(ResponseBase):
    request_id: str
    user_id: str
    phone_id: str
    user_created: bool


class OtpsemailsendResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class OtpsemailloginorcreateResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str
    user_created: bool


class OtpsauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    method_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
    reset_sessions: bool
