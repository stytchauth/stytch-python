#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class DiscoveryorganizationsResponse(ResponseBase):
    request_id: str
    email_address: str
    discovered_organizations: None


class DiscoveryintermediatesessionexchangeResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: None
    session_token: str
    session_jwt: str
    member: None
    organization: None


class DiscoveryorganizationcreateResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: None
    session_token: str
    session_jwt: str
    member: None
    organization: None
