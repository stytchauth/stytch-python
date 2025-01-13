# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from stytch.b2b.models.discovery_organizations import CreateResponse, ListResponse
from stytch.b2b.models.organizations import EmailImplicitRoleAssignment
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Organizations:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def create(
        self,
        intermediate_session_token: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        organization_name: Optional[str] = None,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_jit_provisioning: Optional[str] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
        mfa_policy: Optional[str] = None,
        rbac_email_implicit_role_assignments: Optional[
            List[Union[EmailImplicitRoleAssignment, Dict[str, Any]]]
        ] = None,
        mfa_methods: Optional[str] = None,
        allowed_mfa_methods: Optional[List[str]] = None,
        oauth_tenant_jit_provisioning: Optional[str] = None,
        allowed_oauth_tenants: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """If an end user does not want to join any already-existing, or has no possible Organizations to join, this endpoint can be used to create a new
        [Organization](https://stytch.com/docs/b2b/api/organization-object) and [Member](https://stytch.com/docs/b2b/api/member-object).

        This operation consumes the Intermediate Session.

        This endpoint will also create an initial Member Session for the newly created Member.

        The created by this endpoint will automatically be granted the `stytch_admin` Role. See the
        [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for more details on this Role.

        If the new Organization is created with a `mfa_policy` of `REQUIRED_FOR_ALL`, the newly created Member will need to complete an MFA step to log in to the Organization.
        The `intermediate_session_token` will not be consumed and instead will be returned in the response.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `intermediate_session_token` can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to join a different Organization or create a new one.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        Fields:
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - organization_name: The name of the Organization. If the name is not specified, a default name will be created based on the email used to initiate the discovery flow. If the email domain is a common email provider such as gmail.com, or if the email is a .edu email, the organization name will be generated based on the name portion of the email. Otherwise, the organization name will be generated based on the email domain.
          - organization_slug: The unique URL slug of the Organization. A minimum of two characters is required. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`. If the slug is not specified, a default slug will be created based on the email used to initiate the discovery flow. If the email domain is a common email provider such as gmail.com, or if the email is a .edu email, the organization slug will be generated based on the name portion of the email. Otherwise, the organization slug will be generated based on the email domain.
          - organization_logo_url: The image URL of the Organization logo.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

          `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

          `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

          `NOT_ALLOWED` – disable JIT provisioning via SSO.

          - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


            Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
          - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link or OAuth. The accepted values are:

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link or OAuth.

          `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link and OAuth.

          - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

          `ALL_ALLOWED` – any new Member can be invited to join via email.

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

          `NOT_ALLOWED` – disable email invites.

          - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_auth_methods: An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sso`, `magic_link`, `email_otp`, `password`, `google_oauth`, `microsoft_oauth`, `slack_oauth`, `github_oauth`, and `hubspot_oauth`.

          - mfa_policy: The setting that controls the MFA policy for all Members in the Organization. The accepted values are:

          `REQUIRED_FOR_ALL` – All Members within the Organization will be required to complete MFA every time they wish to log in. However, any active Session that existed prior to this setting change will remain valid.

          `OPTIONAL` – The default value. The Organization does not require MFA by default for all Members. Members will be required to complete MFA only if their `mfa_enrolled` status is set to true.

          - rbac_email_implicit_role_assignments: Implicit role assignments based off of email domains.
          For each domain-Role pair, all Members whose email addresses have the specified email domain will be granted the
          associated Role, regardless of their login method. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment)
          for more information about role assignment.
          - mfa_methods: The setting that controls which MFA methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_mfa_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_mfa_methods: An array of allowed MFA authentication methods. This list is enforced when `mfa_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sms_otp` and `totp`.

          - oauth_tenant_jit_provisioning: The authentication setting that controls how a new Member can JIT provision into an organization by tenant. The accepted values are:

          `RESTRICTED` – only new Members with tenants in `allowed_oauth_tenants` can JIT provision via tenant.

          `NOT_ALLOWED` – disable JIT provisioning by OAuth Tenant.

          - allowed_oauth_tenants: A map of allowed OAuth tenants. If this field is not passed in, the Organization will not allow JIT provisioning by OAuth Tenant. Allowed keys are "slack", "hubspot", and "github".
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,
        }
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if organization_name is not None:
            data["organization_name"] = organization_name
        if organization_slug is not None:
            data["organization_slug"] = organization_slug
        if organization_logo_url is not None:
            data["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if sso_jit_provisioning is not None:
            data["sso_jit_provisioning"] = sso_jit_provisioning
        if email_allowed_domains is not None:
            data["email_allowed_domains"] = email_allowed_domains
        if email_jit_provisioning is not None:
            data["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            data["email_invites"] = email_invites
        if auth_methods is not None:
            data["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            data["allowed_auth_methods"] = allowed_auth_methods
        if mfa_policy is not None:
            data["mfa_policy"] = mfa_policy
        if rbac_email_implicit_role_assignments is not None:
            data["rbac_email_implicit_role_assignments"] = [
                item if isinstance(item, dict) else item.dict()
                for item in rbac_email_implicit_role_assignments
            ]
        if mfa_methods is not None:
            data["mfa_methods"] = mfa_methods
        if allowed_mfa_methods is not None:
            data["allowed_mfa_methods"] = allowed_mfa_methods
        if oauth_tenant_jit_provisioning is not None:
            data["oauth_tenant_jit_provisioning"] = oauth_tenant_jit_provisioning
        if allowed_oauth_tenants is not None:
            data["allowed_oauth_tenants"] = allowed_oauth_tenants

        url = self.api_base.url_for("/v1/b2b/discovery/organizations/create", data)
        res = self.sync_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        intermediate_session_token: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        organization_name: Optional[str] = None,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_jit_provisioning: Optional[str] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
        mfa_policy: Optional[str] = None,
        rbac_email_implicit_role_assignments: Optional[
            List[EmailImplicitRoleAssignment]
        ] = None,
        mfa_methods: Optional[str] = None,
        allowed_mfa_methods: Optional[List[str]] = None,
        oauth_tenant_jit_provisioning: Optional[str] = None,
        allowed_oauth_tenants: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """If an end user does not want to join any already-existing, or has no possible Organizations to join, this endpoint can be used to create a new
        [Organization](https://stytch.com/docs/b2b/api/organization-object) and [Member](https://stytch.com/docs/b2b/api/member-object).

        This operation consumes the Intermediate Session.

        This endpoint will also create an initial Member Session for the newly created Member.

        The created by this endpoint will automatically be granted the `stytch_admin` Role. See the
        [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for more details on this Role.

        If the new Organization is created with a `mfa_policy` of `REQUIRED_FOR_ALL`, the newly created Member will need to complete an MFA step to log in to the Organization.
        The `intermediate_session_token` will not be consumed and instead will be returned in the response.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `intermediate_session_token` can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to join a different Organization or create a new one.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        Fields:
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - organization_name: The name of the Organization. If the name is not specified, a default name will be created based on the email used to initiate the discovery flow. If the email domain is a common email provider such as gmail.com, or if the email is a .edu email, the organization name will be generated based on the name portion of the email. Otherwise, the organization name will be generated based on the email domain.
          - organization_slug: The unique URL slug of the Organization. A minimum of two characters is required. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`. If the slug is not specified, a default slug will be created based on the email used to initiate the discovery flow. If the email domain is a common email provider such as gmail.com, or if the email is a .edu email, the organization slug will be generated based on the name portion of the email. Otherwise, the organization slug will be generated based on the email domain.
          - organization_logo_url: The image URL of the Organization logo.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

          `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

          `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

          `NOT_ALLOWED` – disable JIT provisioning via SSO.

          - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


            Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
          - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link or OAuth. The accepted values are:

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link or OAuth.

          `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link and OAuth.

          - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

          `ALL_ALLOWED` – any new Member can be invited to join via email.

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

          `NOT_ALLOWED` – disable email invites.

          - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_auth_methods: An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sso`, `magic_link`, `email_otp`, `password`, `google_oauth`, `microsoft_oauth`, `slack_oauth`, `github_oauth`, and `hubspot_oauth`.

          - mfa_policy: The setting that controls the MFA policy for all Members in the Organization. The accepted values are:

          `REQUIRED_FOR_ALL` – All Members within the Organization will be required to complete MFA every time they wish to log in. However, any active Session that existed prior to this setting change will remain valid.

          `OPTIONAL` – The default value. The Organization does not require MFA by default for all Members. Members will be required to complete MFA only if their `mfa_enrolled` status is set to true.

          - rbac_email_implicit_role_assignments: Implicit role assignments based off of email domains.
          For each domain-Role pair, all Members whose email addresses have the specified email domain will be granted the
          associated Role, regardless of their login method. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment)
          for more information about role assignment.
          - mfa_methods: The setting that controls which MFA methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_mfa_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_mfa_methods: An array of allowed MFA authentication methods. This list is enforced when `mfa_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sms_otp` and `totp`.

          - oauth_tenant_jit_provisioning: The authentication setting that controls how a new Member can JIT provision into an organization by tenant. The accepted values are:

          `RESTRICTED` – only new Members with tenants in `allowed_oauth_tenants` can JIT provision via tenant.

          `NOT_ALLOWED` – disable JIT provisioning by OAuth Tenant.

          - allowed_oauth_tenants: A map of allowed OAuth tenants. If this field is not passed in, the Organization will not allow JIT provisioning by OAuth Tenant. Allowed keys are "slack", "hubspot", and "github".
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,
        }
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if organization_name is not None:
            data["organization_name"] = organization_name
        if organization_slug is not None:
            data["organization_slug"] = organization_slug
        if organization_logo_url is not None:
            data["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if sso_jit_provisioning is not None:
            data["sso_jit_provisioning"] = sso_jit_provisioning
        if email_allowed_domains is not None:
            data["email_allowed_domains"] = email_allowed_domains
        if email_jit_provisioning is not None:
            data["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            data["email_invites"] = email_invites
        if auth_methods is not None:
            data["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            data["allowed_auth_methods"] = allowed_auth_methods
        if mfa_policy is not None:
            data["mfa_policy"] = mfa_policy
        if rbac_email_implicit_role_assignments is not None:
            data["rbac_email_implicit_role_assignments"] = [
                item if isinstance(item, dict) else item.dict()
                for item in rbac_email_implicit_role_assignments
            ]
        if mfa_methods is not None:
            data["mfa_methods"] = mfa_methods
        if allowed_mfa_methods is not None:
            data["allowed_mfa_methods"] = allowed_mfa_methods
        if oauth_tenant_jit_provisioning is not None:
            data["oauth_tenant_jit_provisioning"] = oauth_tenant_jit_provisioning
        if allowed_oauth_tenants is not None:
            data["allowed_oauth_tenants"] = allowed_oauth_tenants

        url = self.api_base.url_for("/v1/b2b/discovery/organizations/create", data)
        res = await self.async_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status, res.json)

    def list(
        self,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ListResponse:
        """List all possible organization relationships connected to a [Member Session](https://stytch.com/docs/b2b/api/session-object) or Intermediate Session.

        When a Member Session is passed in, relationships with a type of `active_member`, `pending_member`, or `invited_member`
        will be returned, and any membership can be assumed by calling the [Exchange Session](https://stytch.com/docs/b2b/api/exchange-session) endpoint.

        When an Intermediate Session is passed in, all relationship types - `active_member`, `pending_member`, `invited_member`,
        `eligible_to_join_by_email_domain`, and `eligible_to_join_by_oauth_tenant` - will be returned,
        and any membership can be assumed by calling the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) endpoint.

        This endpoint requires either an `intermediate_session_token`, `session_jwt` or `session_token` be included in the request.
        It will return an error if multiple are present.

        This operation does not consume the Intermediate Session or Session Token passed in.

        Fields:
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/b2b/discovery/organizations", data)
        res = self.sync_client.post(url, data, headers)
        return ListResponse.from_json(res.response.status_code, res.json)

    async def list_async(
        self,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ListResponse:
        """List all possible organization relationships connected to a [Member Session](https://stytch.com/docs/b2b/api/session-object) or Intermediate Session.

        When a Member Session is passed in, relationships with a type of `active_member`, `pending_member`, or `invited_member`
        will be returned, and any membership can be assumed by calling the [Exchange Session](https://stytch.com/docs/b2b/api/exchange-session) endpoint.

        When an Intermediate Session is passed in, all relationship types - `active_member`, `pending_member`, `invited_member`,
        `eligible_to_join_by_email_domain`, and `eligible_to_join_by_oauth_tenant` - will be returned,
        and any membership can be assumed by calling the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) endpoint.

        This endpoint requires either an `intermediate_session_token`, `session_jwt` or `session_token` be included in the request.
        It will return an error if multiple are present.

        This operation does not consume the Intermediate Session or Session Token passed in.

        Fields:
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/b2b/discovery/organizations", data)
        res = await self.async_client.post(url, data, headers)
        return ListResponse.from_json(res.response.status, res.json)
