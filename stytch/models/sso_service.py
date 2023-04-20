#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase


class CreateoidcconnectionResponse(ResponseBase):
    request_id: str
    connection: TODO


class CreatesamlconnectionResponse(ResponseBase):
    request_id: str
    connection: TODO


class UpdateoidcconnectionResponse(ResponseBase):
    request_id: str
    connection: TODO
    warning: Optional[str] = None


class UpdatesamlconnectionResponse(ResponseBase):
    request_id: str
    connection: TODO


class UpdatesamlconnectionbyurlResponse(ResponseBase):
    request_id: str
    connection: TODO


class UpdatesamlconnectionbydocResponse(ResponseBase):
    request_id: str
    connection: TODO


class GetssoconnectionsResponse(ResponseBase):
    request_id: str
    saml_connections: TODO
    oidc_connections: TODO


class DeletessoconnectionResponse(ResponseBase):
    request_id: str
    connection_id: str


class SsoauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    organization_id: str
    member: TODO
    session_token: str
    session_jwt: str
    member_session: TODO
    reset_session: bool
    organization: TODO


class DeletesamlverificationcertificateResponse(ResponseBase):
    request_id: str
    certificate_id: str
