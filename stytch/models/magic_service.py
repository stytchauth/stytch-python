#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class SendmagicbyemailResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class MagiclinksemailsendResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class AuthenticatemagicResponse(ResponseBase):
    request_id: str
    user_id: str
    method_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
    reset_sessions: bool


class MagiclinksauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    method_id: str
    session_token: str
    session: Optional[StytchSession]
    session_jwt: str
    user: User
    reset_sessions: bool


class MagiclinksemailloginorcreateResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str
    user_created: bool


class SdkmagiclinksemailloginorcreateResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class InvitebyemailResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class MagiclinksemailinviteResponse(ResponseBase):
    request_id: str
    user_id: str
    email_id: str


class MagiclinksemailrevokeinviteResponse(ResponseBase):
    request_id: str


class MagiclinkscreateResponse(ResponseBase):
    request_id: str
    user_id: str
    token: str


class MagiclinkredirectResponse(ResponseBase):
    request_id: str
    redirect_url: str
    html_response_data: None


class MagiclinksredirectcaptchaResponse(ResponseBase):
    request_id: str
    redirect_url: str
