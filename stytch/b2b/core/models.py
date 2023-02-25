#!/usr/bin/env python3

from __future__ import annotations

import datetime
from typing import Any, Dict, List, Optional

import pydantic


class Organization(pydantic.BaseModel):
    organization_id: str
    organization_name: str
    organization_slug: str
    organization_logo_url: str
    trusted_metadata: Dict[str, Any]
    sso_default_connection_id: Optional[str]
    sso_jit_provisioning_allowed_connections: List[str]
    sso_jit_provisioning: str
    email_allowed_domains: List[str]
    email_jit_provisioning: str
    email_invites: str


class SSORegistration(pydantic.BaseModel):
    connection_id: str
    identity_provider: str
    external_id: str
    registration_id: str
    sso_registration_attributes: Dict[str, Any]


class Member(pydantic.BaseModel):
    organization_id: str
    member_id: str
    email_address: str
    status: str
    name: str
    sso_registrations: List[SSORegistration]


class B2BStytchSession(pydantic.BaseModel):
    member_session_id: str
    member_id: str
    started_at: datetime.datetime
    last_accessed_at: datetime.datetime
    expires_at: datetime.datetime
    authentication_factors: List[Dict[str, Any]]
    custom_claims: Optional[Dict[str, Any]]
