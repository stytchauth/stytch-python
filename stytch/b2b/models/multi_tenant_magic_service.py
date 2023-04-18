#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantmagiclinksemailloginorsignupResponse(ResponseBase):
    request_id: str
    member_id: str
    member_created: bool
    member: None
    organization: None


class MultitenantmagiclinksemailinviteResponse(ResponseBase):
    request_id: str
    member_id: str
    member: None
    organization: None


class MultitenantmagiclinksauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    method_id: str
    reset_sessions: bool
    organization_id: str
    member: None
    session_token: str
    session_jwt: str
    member_session: None
    organization: None


class B2BmagiclinksemaildiscoverysendResponse(ResponseBase):
    request_id: str


class B2BmagiclinksdiscoveryauthenticateResponse(ResponseBase):
    request_id: str
    intermediate_session_token: str
    email_address: str
    discovered_organizations: None
