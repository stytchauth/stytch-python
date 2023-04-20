#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class DiscoveryorganizationsResponse(ResponseBase):
    request_id: str
    email_address: str
    discovered_organizations: TODO


class DiscoveryintermediatesessionexchangeResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: TODO
    session_token: str
    session_jwt: str
    member: TODO
    organization: TODO


class DiscoveryorganizationcreateResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: TODO
    session_token: str
    session_jwt: str
    member: TODO
    organization: TODO
