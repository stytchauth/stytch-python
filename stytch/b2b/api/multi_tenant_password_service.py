# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, List, Optional, Union

import pydantic

from stytch.b2b.models.multi_tenant_password_service import (
    MultitenantpasswordauthenticateResponse,
    MultitenantpasswordemailresetResponse,
    MultitenantpasswordemailresetstartResponse,
    MultitenantpasswordexistingpasswordresetResponse,
    MultitenantpasswordmigrateResponse,
    MultitenantpasswordsessionresetResponse,
    MultitenantpasswordstrengthcheckResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class MultiTenantPasswordService:
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
        return "multi_tenant_password_service"

    def MultiTenantPasswordStrengthCheck(
        self,
        password: str,
        email_address: Optional[str] = None,
    ) -> MultitenantpasswordstrengthcheckResponse:

        payload: Dict[str, Any] = {
            "password": password,
        }

        if email_address is not None:
            payload["email_address"] = email_address

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/strength_check")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordstrengthcheckResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordStrengthCheck_async(
      self,
      password: str,
      email_address: Optional[str] = None,
    ) -> MultitenantpasswordstrengthcheckResponse:

        payload: Dict[str, Any] = {
            "password": password,
        }

        if email_address is not None:
            payload["email_address"] = email_address

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/strength_check")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordstrengthcheckResponse.from_json(res.response.status, res.json)

    def MultiTenantPasswordMigrate(
        self,
        email_address: str,
        hash: str,
        hash_type: str,
        md_5_config: None,
        argon_2_config: None,
        sha_1_config: None,
        scrypt_config: None,
        organization_id: str,
        name: str,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> MultitenantpasswordmigrateResponse:

        payload: Dict[str, Any] = {
            "email_address": email_address,
            "hash": hash,
            "hash_type": hash_type,
            "organization_id": organization_id,
            "name": name,
        }

        if md_5_config is not None:
            payload["md_5_config"] = md_5_config
        if argon_2_config is not None:
            payload["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            payload["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            payload["scrypt_config"] = scrypt_config
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/migrate")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordmigrateResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordMigrate_async(
      self,
      email_address: str,
      hash: str,
      hash_type: str,
      md_5_config: None,
      argon_2_config: None,
      sha_1_config: None,
      scrypt_config: None,
      organization_id: str,
      name: str,
      trusted_metadata: Optional[Dict[str, Any]] = None,
      untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> MultitenantpasswordmigrateResponse:

        payload: Dict[str, Any] = {
            "email_address": email_address,
            "hash": hash,
            "hash_type": hash_type,
            "organization_id": organization_id,
            "name": name,
        }

        if md_5_config is not None:
            payload["md_5_config"] = md_5_config
        if argon_2_config is not None:
            payload["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            payload["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            payload["scrypt_config"] = scrypt_config
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/migrate")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordmigrateResponse.from_json(res.response.status, res.json)

    def MultiTenantPasswordAuthenticate(
        self,
        organization_id: str,
        email_address: str,
        password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> MultitenantpasswordauthenticateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/authenticate")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordauthenticateResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordAuthenticate_async(
      self,
      organization_id: str,
      email_address: str,
      password: str,
      session_token: Optional[str] = None,
      session_duration_minutes: Optional[int] = None,
      session_jwt: Optional[str] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> MultitenantpasswordauthenticateResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/authenticate")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordauthenticateResponse.from_json(res.response.status, res.json)

    def MultiTenantPasswordEmailResetStart(
        self,
        organization_id: str,
        email_address: str,
        reset_password_redirect_url: str,
        reset_password_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        login_redirect_url: str,
        locale: Optional[str] = None,
        reset_password_template_id: Optional[str] = None,
    ) -> MultitenantpasswordemailresetstartResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "reset_password_redirect_url": reset_password_redirect_url,
            "login_redirect_url": login_redirect_url,
        }

        if reset_password_expiration_minutes is not None:
            payload["reset_password_expiration_minutes"] = reset_password_expiration_minutes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if locale is not None:
            payload["locale"] = locale
        if reset_password_template_id is not None:
            payload["reset_password_template_id"] = reset_password_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/email/reset/start")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordemailresetstartResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordEmailResetStart_async(
      self,
      organization_id: str,
      email_address: str,
      reset_password_redirect_url: str,
      reset_password_expiration_minutes: Optional[int] = None,
      code_challenge: Optional[str] = None,
      login_redirect_url: str,
      locale: Optional[str] = None,
      reset_password_template_id: Optional[str] = None,
    ) -> MultitenantpasswordemailresetstartResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "reset_password_redirect_url": reset_password_redirect_url,
            "login_redirect_url": login_redirect_url,
        }

        if reset_password_expiration_minutes is not None:
            payload["reset_password_expiration_minutes"] = reset_password_expiration_minutes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if locale is not None:
            payload["locale"] = locale
        if reset_password_template_id is not None:
            payload["reset_password_template_id"] = reset_password_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/email/reset/start")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordemailresetstartResponse.from_json(res.response.status, res.json)

    def MultiTenantPasswordEmailReset(
        self,
        password_reset_token: str,
        password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        code_verifier: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> MultitenantpasswordemailresetResponse:

        payload: Dict[str, Any] = {
            "password_reset_token": password_reset_token,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/email/reset")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordemailresetResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordEmailReset_async(
      self,
      password_reset_token: str,
      password: str,
      session_token: Optional[str] = None,
      session_duration_minutes: Optional[int] = None,
      session_jwt: Optional[str] = None,
      code_verifier: Optional[str] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> MultitenantpasswordemailresetResponse:

        payload: Dict[str, Any] = {
            "password_reset_token": password_reset_token,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/email/reset")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordemailresetResponse.from_json(res.response.status, res.json)

    def MultiTenantPasswordSessionReset(
        self,
        organization_id: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> MultitenantpasswordsessionresetResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/session/reset")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordsessionresetResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordSessionReset_async(
      self,
      organization_id: str,
      password: str,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
    ) -> MultitenantpasswordsessionresetResponse:

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/session/reset")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordsessionresetResponse.from_json(res.response.status, res.json)

    def MultiTenantPasswordExistingPasswordReset(
        self,
        email_address: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        organization_id: str,
    ) -> MultitenantpasswordexistingpasswordresetResponse:

        payload: Dict[str, Any] = {
            "email_address": email_address,
            "existing_password": existing_password,
            "new_password": new_password,
            "organization_id": organization_id,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/existing_password/reset")

        res = self.sync_client.post(url, json=payload)
        return MultitenantpasswordexistingpasswordresetResponse.from_json(res.response.status_code, res.json)

    async def MultiTenantPasswordExistingPasswordReset_async(
      self,
      email_address: str,
      existing_password: str,
      new_password: str,
      session_token: Optional[str] = None,
      session_duration_minutes: Optional[int] = None,
      session_jwt: Optional[str] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
      organization_id: str,
    ) -> MultitenantpasswordexistingpasswordresetResponse:

        payload: Dict[str, Any] = {
            "email_address": email_address,
            "existing_password": existing_password,
            "new_password": new_password,
            "organization_id": organization_id,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/passwords/existing_password/reset")

        res = await self.async_client.post(url, json=payload)
        return MultitenantpasswordexistingpasswordresetResponse.from_json(res.response.status, res.json)

