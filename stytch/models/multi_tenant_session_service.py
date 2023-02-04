#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantsessionsgetResponse(ResponseBase):
    request_id: str
    sessions: None


class MultitenantsessionsauthenticateResponse(ResponseBase):
    request_id: str
    member_session: None
    session_token: str
    session_jwt: str
    member: None


class MultitenantsessionsrevokeResponse(ResponseBase):
    request_id: str
