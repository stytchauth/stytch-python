#!/usr/bin/env python3

from typing import List

from stytch.core.models import ResponseBase


class OrganizationscreateResponse(ResponseBase):
    request_id: str
    organization: Organization


class OrganizationsgetResponse(ResponseBase):
    request_id: str
    organization: Organization


class OrganizationsupdateResponse(ResponseBase):
    request_id: str
    organization: Organization


class OrganizationsdeleteResponse(ResponseBase):
    request_id: str
    organization_id: str


class OrganizationsmemberdeleteResponse(ResponseBase):
    request_id: str
    member_id: str


class OrganizationssearchexternalResponse(ResponseBase):
    request_id: str
    organizations: List[Organization]
    results_metadata: ResultsMetadata


class OrganizationsmembersearchexternalResponse(ResponseBase):
    request_id: str
    members: List[Member]
    results_metadata: ResultsMetadata
