#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase


class CreateoidcconnectionResponse(ResponseBase):
    request_id: str
    connection: None


class CreatesamlconnectionResponse(ResponseBase):
    request_id: str
    connection: None


class UpdateoidcconnectionResponse(ResponseBase):
    request_id: str
    connection: None
    warning: Optional[str] = None


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
    oidc_connections: None


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
    member_session: None
    reset_session: bool
    organization: None


class DeletesamlverificationcertificateResponse(ResponseBase):
    request_id: str
    certificate_id: str
