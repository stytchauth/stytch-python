#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantmagiclinksemailloginorsignupResponse(ResponseBase):
    request_id: str
    member_id: str
    member_created: bool
    member: None


class MultitenantmagiclinksemailinviteResponse(ResponseBase):
    request_id: str
    member_id: str
    member: None


class MultitenantmagiclinksauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    method_id: str
    reset_sessions: bool
    organization_id: str
    member: None
    session_token: str
    session_jwt: str
    session: None
