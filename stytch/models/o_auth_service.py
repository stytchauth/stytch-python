#!/usr/bin/env python3


from stytch.core.models import OAuthSession, ResponseBase, User


class OauthattachResponse(ResponseBase):
    request_id: str
    oauth_attach_token: str


class OauthauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    provider_subject: str
    provider_type: str
    session: OAuthSession
    session_token: str
    session_jwt: str
    provider_values: None
    user: User
    reset_sessions: bool
    oauth_user_registration_id: str
