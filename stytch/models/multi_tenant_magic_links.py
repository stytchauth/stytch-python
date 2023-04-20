#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantmagiclinksemailloginorsignupResponse(ResponseBase):
    request_id: str
    member_id: str
    member_created: bool
    member: TODO
    organization: TODO


class MultitenantmagiclinksemailinviteResponse(ResponseBase):
    request_id: str
    member_id: str
    member: TODO
    organization: TODO


class MultitenantmagiclinksauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    method_id: str
    reset_sessions: bool
    organization_id: str
    member: TODO
    session_token: str
    session_jwt: str
    member_session: TODO
    organization: TODO


class B2BmagiclinksemaildiscoverysendResponse(ResponseBase):
    request_id: str


class B2BmagiclinksdiscoveryauthenticateResponse(ResponseBase):
    request_id: str
    intermediate_session_token: str
    email_address: str
    discovered_organizations: TODO
