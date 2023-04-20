# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

import time
from typing import Any, AsyncGenerator, Dict, Generator, List, Optional, Union

import jwt
import pydantic
from stytch.core.api_base import ApiBase
from stytch.core.b2b.models import B2BStytchSession, Member, Organization
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import (
    Name,
    SearchQuery,
    SearchResultsMetadata,
    StytchSession,
    User,
)
from stytch.models.organizations import (
    CreateResponse,
    DeleteResponse,
    GetResponse,
    OrganizationsmembercreateResponse,
    OrganizationsmemberdeletepasswordResponse,
    OrganizationsmemberdeleteResponse,
    OrganizationsmembergetResponse,
    OrganizationsmembersearchexternalResponse,
    OrganizationsmemberupdateResponse,
    OrganizationssearchexternalResponse,
    UpdateResponse,
)


class Organizations:
    def __init__(
      self,
      api_base: ApiBase,
      sync_client: SyncClient,
      async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "organizations"

    def create(
        self,
        organization_name: str,
        organization_slug: str,
        organization_logo_url: str,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_jit_provisioning: Optional[str] = None,
        email_allowed_domains: List[str],
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: List[str],
    ) -> CreateResponse:

        payload: Dict[str, Any] = {
            "organization_name": organization_name,

            "organization_slug": organization_slug,

            "organization_logo_url": organization_logo_url,

            "email_allowed_domains": email_allowed_domains,

            "allowed_auth_methods": allowed_auth_methods,

        }

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if sso_jit_provisioning is not None:
            payload["sso_jit_provisioning"] = sso_jit_provisioning

        if email_jit_provisioning is not None:
            payload["email_jit_provisioning"] = email_jit_provisioning

        if email_invites is not None:
            payload["email_invites"] = email_invites

        if auth_methods is not None:
            payload["auth_methods"] = auth_methods


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations")

        res = self.sync_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
      self,
      organization_name: str,
      organization_slug: str,
      organization_logo_url: str,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      sso_jit_provisioning: Optional[str] = None,
      email_allowed_domains: List[str],
      email_jit_provisioning: Optional[str] = None,
      email_invites: Optional[str] = None,
      auth_methods: Optional[str] = None,
      allowed_auth_methods: List[str],
    ) -> CreateResponse:

        payload: Dict[str, Any] = {
            "organization_name": organization_name,

            "organization_slug": organization_slug,

            "organization_logo_url": organization_logo_url,

            "email_allowed_domains": email_allowed_domains,

            "allowed_auth_methods": allowed_auth_methods,

        }

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if sso_jit_provisioning is not None:
            payload["sso_jit_provisioning"] = sso_jit_provisioning

        if email_jit_provisioning is not None:
            payload["email_jit_provisioning"] = email_jit_provisioning

        if email_invites is not None:
            payload["email_invites"] = email_invites

        if auth_methods is not None:
            payload["auth_methods"] = auth_methods


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations")

        res = await self.async_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status, res.json)

    def get(
        self,
        organization_id: str,
    ) -> GetResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}")

        res = self.sync_client.get(url, params=payload)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
      self,
      organization_id: str,
    ) -> GetResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}")

        res = await self.async_client.get(url, params=payload)
        return GetResponse.from_json(res.response.status, res.json)

    def update(
        self,
        organization_id: str,
        organization_name: Optional[str] = None,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_default_connection_id: Optional[str] = None,
        sso_jit_provisioning: Optional[str] = None,
        sso_jit_provisioning_allowed_connections: Optional[List[str]] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
    ) -> UpdateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

        }

        if organization_name is not None:
            payload["organization_name"] = organization_name

        if organization_slug is not None:
            payload["organization_slug"] = organization_slug

        if organization_logo_url is not None:
            payload["organization_logo_url"] = organization_logo_url

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if sso_default_connection_id is not None:
            payload["sso_default_connection_id"] = sso_default_connection_id

        if sso_jit_provisioning is not None:
            payload["sso_jit_provisioning"] = sso_jit_provisioning

        if sso_jit_provisioning_allowed_connections is not None:
            payload["sso_jit_provisioning_allowed_connections"] = sso_jit_provisioning_allowed_connections

        if email_allowed_domains is not None:
            payload["email_allowed_domains"] = email_allowed_domains

        if email_jit_provisioning is not None:
            payload["email_jit_provisioning"] = email_jit_provisioning

        if email_invites is not None:
            payload["email_invites"] = email_invites

        if auth_methods is not None:
            payload["auth_methods"] = auth_methods

        if allowed_auth_methods is not None:
            payload["allowed_auth_methods"] = allowed_auth_methods


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}")

        res = self.sync_client.put(url, json=payload)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
      self,
      organization_id: str,
      organization_name: Optional[str] = None,
      organization_slug: Optional[str] = None,
      organization_logo_url: Optional[str] = None,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      sso_default_connection_id: Optional[str] = None,
      sso_jit_provisioning: Optional[str] = None,
      sso_jit_provisioning_allowed_connections: Optional[List[str]] = None,
      email_allowed_domains: Optional[List[str]] = None,
      email_jit_provisioning: Optional[str] = None,
      email_invites: Optional[str] = None,
      auth_methods: Optional[str] = None,
      allowed_auth_methods: Optional[List[str]] = None,
    ) -> UpdateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

        }

        if organization_name is not None:
            payload["organization_name"] = organization_name

        if organization_slug is not None:
            payload["organization_slug"] = organization_slug

        if organization_logo_url is not None:
            payload["organization_logo_url"] = organization_logo_url

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if sso_default_connection_id is not None:
            payload["sso_default_connection_id"] = sso_default_connection_id

        if sso_jit_provisioning is not None:
            payload["sso_jit_provisioning"] = sso_jit_provisioning

        if sso_jit_provisioning_allowed_connections is not None:
            payload["sso_jit_provisioning_allowed_connections"] = sso_jit_provisioning_allowed_connections

        if email_allowed_domains is not None:
            payload["email_allowed_domains"] = email_allowed_domains

        if email_jit_provisioning is not None:
            payload["email_jit_provisioning"] = email_jit_provisioning

        if email_invites is not None:
            payload["email_invites"] = email_invites

        if auth_methods is not None:
            payload["auth_methods"] = auth_methods

        if allowed_auth_methods is not None:
            payload["allowed_auth_methods"] = allowed_auth_methods


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}")

        res = await self.async_client.put(url, json=payload)
        return UpdateResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        organization_id: str,
    ) -> DeleteResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}")

        res = self.sync_client.delete(url)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
      self,
      organization_id: str,
    ) -> DeleteResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}")

        res = await self.async_client.delete(url)
        return DeleteResponse.from_json(res.response.status, res.json)

    def OrganizationsMemberCreate(
        self,
        organization_id: str,
        email_address: str,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        create_member_as_pending: bool,
        is_breakglass: bool,
    ) -> OrganizationsmembercreateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

            "email_address": email_address,

            "create_member_as_pending": create_member_as_pending,

            "is_breakglass": is_breakglass,

        }

        if name is not None:
            payload["name"] = name

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members")

        res = self.sync_client.post(url, json=payload)
        return OrganizationsmembercreateResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsMemberCreate_async(
      self,
      organization_id: str,
      email_address: str,
      name: Optional[str] = None,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      untrusted_metadata: Optional[Dict[str, Any]] = None,
      create_member_as_pending: bool,
      is_breakglass: bool,
    ) -> OrganizationsmembercreateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

            "email_address": email_address,

            "create_member_as_pending": create_member_as_pending,

            "is_breakglass": is_breakglass,

        }

        if name is not None:
            payload["name"] = name

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members")

        res = await self.async_client.post(url, json=payload)
        return OrganizationsmembercreateResponse.from_json(res.response.status, res.json)

    def OrganizationsMemberUpdate(
        self,
        organization_id: str,
        member_id: str,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        is_breakglass: Optional[bool] = None,
    ) -> OrganizationsmemberupdateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

            "member_id": member_id,

        }

        if name is not None:
            payload["name"] = name

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        if is_breakglass is not None:
            payload["is_breakglass"] = is_breakglass


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members/{member_id}")

        res = self.sync_client.put(url, json=payload)
        return OrganizationsmemberupdateResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsMemberUpdate_async(
      self,
      organization_id: str,
      member_id: str,
      name: Optional[str] = None,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      untrusted_metadata: Optional[Dict[str, Any]] = None,
      is_breakglass: Optional[bool] = None,
    ) -> OrganizationsmemberupdateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

            "member_id": member_id,

        }

        if name is not None:
            payload["name"] = name

        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata

        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        if is_breakglass is not None:
            payload["is_breakglass"] = is_breakglass


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members/{member_id}")

        res = await self.async_client.put(url, json=payload)
        return OrganizationsmemberupdateResponse.from_json(res.response.status, res.json)

    def OrganizationsMemberDelete(
        self,
        organization_id: str,
        member_id: str,
    ) -> OrganizationsmemberdeleteResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members/{member_id}")

        res = self.sync_client.delete(url)
        return OrganizationsmemberdeleteResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsMemberDelete_async(
      self,
      organization_id: str,
      member_id: str,
    ) -> OrganizationsmemberdeleteResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members/{member_id}")

        res = await self.async_client.delete(url)
        return OrganizationsmemberdeleteResponse.from_json(res.response.status, res.json)

    def OrganizationsSearchExternal(
        self,
        cursor: str,
        limit: Optional[int] = None,
        query: Optional[SearchQuery] = None,
    ) -> OrganizationssearchexternalResponse:

        payload: Dict[str, Any] = {
            "cursor": cursor,

        }

        if limit is not None:
            payload["limit"] = limit

        if query is not None:
            payload["query"] = query


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/search")

        res = self.sync_client.post(url, json=payload)
        return OrganizationssearchexternalResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsSearchExternal_async(
      self,
      cursor: str,
      limit: Optional[int] = None,
      query: Optional[SearchQuery] = None,
    ) -> OrganizationssearchexternalResponse:

        payload: Dict[str, Any] = {
            "cursor": cursor,

        }

        if limit is not None:
            payload["limit"] = limit

        if query is not None:
            payload["query"] = query


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/search")

        res = await self.async_client.post(url, json=payload)
        return OrganizationssearchexternalResponse.from_json(res.response.status, res.json)

    def OrganizationsMemberSearchExternal(
        self,
        cursor: str,
        limit: Optional[int] = None,
        query: Optional[SearchQuery] = None,
        organization_ids: List[str],
    ) -> OrganizationsmembersearchexternalResponse:

        payload: Dict[str, Any] = {
            "cursor": cursor,

            "organization_ids": organization_ids,

        }

        if limit is not None:
            payload["limit"] = limit

        if query is not None:
            payload["query"] = query


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/members/search")

        res = self.sync_client.post(url, json=payload)
        return OrganizationsmembersearchexternalResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsMemberSearchExternal_async(
      self,
      cursor: str,
      limit: Optional[int] = None,
      query: Optional[SearchQuery] = None,
      organization_ids: List[str],
    ) -> OrganizationsmembersearchexternalResponse:

        payload: Dict[str, Any] = {
            "cursor": cursor,

            "organization_ids": organization_ids,

        }

        if limit is not None:
            payload["limit"] = limit

        if query is not None:
            payload["query"] = query


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/members/search")

        res = await self.async_client.post(url, json=payload)
        return OrganizationsmembersearchexternalResponse.from_json(res.response.status, res.json)

    def OrganizationsMemberDeletePassword(
        self,
        organization_id: str,
        member_password_id: str,
    ) -> OrganizationsmemberdeletepasswordResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members/passwords/{member_password_id}")

        res = self.sync_client.delete(url)
        return OrganizationsmemberdeletepasswordResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsMemberDeletePassword_async(
      self,
      organization_id: str,
      member_password_id: str,
    ) -> OrganizationsmemberdeletepasswordResponse:


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/members/passwords/{member_password_id}")

        res = await self.async_client.delete(url)
        return OrganizationsmemberdeletepasswordResponse.from_json(res.response.status, res.json)

    def OrganizationsMemberGet(
        self,
        organization_id: str,
        member_id: Optional[str] = None,
        email_address: Optional[str] = None,
    ) -> OrganizationsmembergetResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

        }

        if member_id is not None:
            payload["member_id"] = member_id

        if email_address is not None:
            payload["email_address"] = email_address


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/member")

        res = self.sync_client.get(url, params=payload)
        return OrganizationsmembergetResponse.from_json(res.response.status_code, res.json)

    async def OrganizationsMemberGet_async(
      self,
      organization_id: str,
      member_id: Optional[str] = None,
      email_address: Optional[str] = None,
    ) -> OrganizationsmembergetResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,

        }

        if member_id is not None:
            payload["member_id"] = member_id

        if email_address is not None:
            payload["email_address"] = email_address


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/organizations/{organization_id}/member")

        res = await self.async_client.get(url, params=payload)
        return OrganizationsmembergetResponse.from_json(res.response.status, res.json)

