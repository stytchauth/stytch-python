#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class CreatesamlconnectionResponse(ResponseBase):
    request_id: str
    connection: None


class UpdatesamlconnectionResponse(ResponseBase):
    request_id: str
    connection: None


class UpdatesamlconnectionbyurlResponse(ResponseBase):
    request_id: str
    connection: None


class UpdatesamlconnectionbydocResponse(ResponseBase):
    request_id: str
    connection: None


class GetssoconnectionsResponse(ResponseBase):
    request_id: str
    saml_connections: None


class DeletessoconnectionResponse(ResponseBase):
    request_id: str
    connection_id: str


class SsoauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    organization_id: str
    member: None
    session_token: str
    session_jwt: str
    session: None
    reset_session: bool


class DeletesamlverificationcertificateResponse(ResponseBase):
    request_id: str
    certificate_id: str
