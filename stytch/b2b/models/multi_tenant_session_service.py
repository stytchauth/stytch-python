#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantsessionsgetResponse(ResponseBase):
    request_id: str
    member_sessions: None


class MultitenantsessionsauthenticateResponse(ResponseBase):
    request_id: str
    member_session: None
    session_token: str
    session_jwt: str
    member: None
    organization: None


class MultitenantsessionsrevokeResponse(ResponseBase):
    request_id: str


class MultitenantsessionsexchangeResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: None
    session_token: str
    session_jwt: str
    member: None
    organization: None
