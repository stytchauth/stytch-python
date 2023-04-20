#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantgetResponse(ResponseBase):
    request_id: str
    member_sessions: TODO


class MultitenantauthenticateResponse(ResponseBase):
    request_id: str
    member_session: TODO
    session_token: str
    session_jwt: str
    member: TODO
    organization: TODO


class MultitenantsessionsrevokeResponse(ResponseBase):
    request_id: str


class MultitenantsessionsexchangeResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: TODO
    session_token: str
    session_jwt: str
    member: TODO
    organization: TODO
