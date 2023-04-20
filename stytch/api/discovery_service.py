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
from stytch.models.discovery_service import (
    DiscoveryintermediatesessionexchangeResponse,
    DiscoveryorganizationcreateResponse,
    DiscoveryorganizationsResponse,
)


class DiscoveryService:
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
        return "discovery_service"

    def DiscoveryOrganizations(
        self,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> DiscoveryorganizationsResponse:

        payload: Dict[str, Any] = {
        }

        if intermediate_session_token is not None:
            payload["intermediate_session_token"] = intermediate_session_token

        if session_token is not None:
            payload["session_token"] = session_token

        if session_jwt is not None:
            payload["session_jwt"] = session_jwt


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/discovery/organizations")

        res = self.sync_client.post(url, json=payload)
        return DiscoveryorganizationsResponse.from_json(res.response.status_code, res.json)

    async def DiscoveryOrganizations_async(
      self,
      intermediate_session_token: Optional[str] = None,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
    ) -> DiscoveryorganizationsResponse:

        payload: Dict[str, Any] = {
        }

        if intermediate_session_token is not None:
            payload["intermediate_session_token"] = intermediate_session_token

        if session_token is not None:
            payload["session_token"] = session_token

        if session_jwt is not None:
            payload["session_jwt"] = session_jwt


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/discovery/organizations")

        res = await self.async_client.post(url, json=payload)
        return DiscoveryorganizationsResponse.from_json(res.response.status, res.json)

    def DiscoveryIntermediateSessionExchange(
        self,
        intermediate_session_token: str,
        organization_id: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> DiscoveryintermediatesessionexchangeResponse:

        payload: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,

            "organization_id": organization_id,

        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes

        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/discovery/intermediate_sessions/exchange")

        res = self.sync_client.post(url, json=payload)
        return DiscoveryintermediatesessionexchangeResponse.from_json(res.response.status_code, res.json)

    async def DiscoveryIntermediateSessionExchange_async(
      self,
      intermediate_session_token: str,
      organization_id: str,
      session_duration_minutes: Optional[int] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> DiscoveryintermediatesessionexchangeResponse:

        payload: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,

            "organization_id": organization_id,

        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes

        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/discovery/intermediate_sessions/exchange")

        res = await self.async_client.post(url, json=payload)
        return DiscoveryintermediatesessionexchangeResponse.from_json(res.response.status, res.json)

    def DiscoveryOrganizationCreate(
        self,
        intermediate_session_token: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
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
    ) -> DiscoveryorganizationcreateResponse:

        payload: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,

            "organization_name": organization_name,

            "organization_slug": organization_slug,

            "organization_logo_url": organization_logo_url,

            "email_allowed_domains": email_allowed_domains,

            "allowed_auth_methods": allowed_auth_methods,

        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes

        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

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


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/discovery/organizations/create")

        res = self.sync_client.post(url, json=payload)
        return DiscoveryorganizationcreateResponse.from_json(res.response.status_code, res.json)

    async def DiscoveryOrganizationCreate_async(
      self,
      intermediate_session_token: str,
      session_duration_minutes: Optional[int] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
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
    ) -> DiscoveryorganizationcreateResponse:

        payload: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,

            "organization_name": organization_name,

            "organization_slug": organization_slug,

            "organization_logo_url": organization_logo_url,

            "email_allowed_domains": email_allowed_domains,

            "allowed_auth_methods": allowed_auth_methods,

        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes

        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

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


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/discovery/organizations/create")

        res = await self.async_client.post(url, json=payload)
        return DiscoveryorganizationcreateResponse.from_json(res.response.status, res.json)

