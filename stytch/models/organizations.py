#!/usr/bin/env python3

from typing import List

from stytch.b2b.core.models import Member, Organization
from stytch.core.models import ResponseBase, SearchResultsMetadata


class CreateResponse(ResponseBase):
    request_id: str
    organization: TODO


class GetResponse(ResponseBase):
    request_id: str
    organization: TODO


class UpdateResponse(ResponseBase):
    request_id: str
    organization: TODO


class DeleteResponse(ResponseBase):
    request_id: str
    organization_id: str


class OrganizationsmembercreateResponse(ResponseBase):
    request_id: str
    member_id: str
    member: TODO
    organization: TODO


class OrganizationsmemberupdateResponse(ResponseBase):
    request_id: str
    member_id: str
    member: TODO
    organization: TODO


class OrganizationsmemberdeleteResponse(ResponseBase):
    request_id: str
    member_id: str


class OrganizationssearchexternalResponse(ResponseBase):
    request_id: str
    organizations: List[Organization]
    results_metadata: SearchResultsMetadata


class OrganizationsmembersearchexternalResponse(ResponseBase):
    request_id: str
    members: List[Member]
    results_metadata: SearchResultsMetadata


class OrganizationsmemberdeletepasswordResponse(ResponseBase):
    request_id: str
    member_id: str
    member: TODO
    organization: TODO


class OrganizationsmembergetResponse(ResponseBase):
    request_id: str
    member_id: str
    member: TODO
    organization: TODO
