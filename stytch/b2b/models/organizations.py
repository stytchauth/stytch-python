# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
import enum
from typing import Any, Dict, List, Optional

import pydantic

from stytch.b2b.models.scim import SCIMAttributes
from stytch.core.response_base import ResponseBase
from stytch.shared.method_options import Authorization


class CreateRequestFirstPartyConnectedAppsAllowedType(str, enum.Enum):
    ALL_ALLOWED = "ALL_ALLOWED"
    RESTRICTED = "RESTRICTED"
    NOT_ALLOWED = "NOT_ALLOWED"


class CreateRequestThirdPartyConnectedAppsAllowedType(str, enum.Enum):
    ALL_ALLOWED = "ALL_ALLOWED"
    RESTRICTED = "RESTRICTED"
    NOT_ALLOWED = "NOT_ALLOWED"


class SearchQueryOperator(str, enum.Enum):
    OR = "OR"
    AND = "AND"


class UpdateRequestFirstPartyConnectedAppsAllowedType(str, enum.Enum):
    ALL_ALLOWED = "ALL_ALLOWED"
    RESTRICTED = "RESTRICTED"
    NOT_ALLOWED = "NOT_ALLOWED"


class UpdateRequestThirdPartyConnectedAppsAllowedType(str, enum.Enum):
    ALL_ALLOWED = "ALL_ALLOWED"
    RESTRICTED = "RESTRICTED"
    NOT_ALLOWED = "NOT_ALLOWED"


class ActiveSCIMConnection(pydantic.BaseModel):
    """
    Fields:
      - connection_id: The ID of the SCIM connection.
      - display_name: A human-readable display name for the connection.
      - bearer_token_last_four: (no documentation yet)
      - bearer_token_expires_at: (no documentation yet)
    """  # noqa

    connection_id: str
    display_name: str
    bearer_token_last_four: str
    bearer_token_expires_at: Optional[datetime.datetime] = None


class ActiveSSOConnection(pydantic.BaseModel):
    """
    Fields:
      - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
      - display_name: A human-readable display name for the connection.
      - identity_provider: (no documentation yet)
    """  # noqa

    connection_id: str
    display_name: str
    identity_provider: str


class ConnectedAppsRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class DeleteRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class EmailImplicitRoleAssignment(pydantic.BaseModel):
    """
    Fields:
      - domain: Email domain that grants the specified Role.
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


    """  # noqa

    domain: str
    role_id: str


class GetConnectedAppRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class GithubProviderInfo(pydantic.BaseModel):
    """
    Fields:
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - provider_tenant_ids: All tenant IDs returned by the OAuth provider. These is typically used to identify organizations or groups within the provider's domain. For example, in HubSpot this is a Hub ID, in Slack this is the Workspace ID, and in GitHub this is an organization ID. Some OAuth providers do not return tenant IDs, some providers are guaranteed to return one, and some may return multiple. This field will always be populated if at least one tenant ID was returned from the OAuth provider and developers should prefer this field over `provider_tenant_id`.
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
    """  # noqa

    provider_subject: str
    provider_tenant_ids: List[str]
    access_token: str
    scopes: List[str]


class HubspotProviderInfo(pydantic.BaseModel):
    """
    Fields:
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - provider_tenant_id: The tenant ID returned by the OAuth provider. This is typically used to identify an organization or group within the provider's domain. For example, in HubSpot this is a Hub ID, in Slack this is the Workspace ID, and in GitHub this is an organization ID. This field will only be populated if exactly one tenant ID is returned from a successful OAuth authentication and developers should prefer `provider_tenant_ids` over this since it accounts for the possibility of an OAuth provider yielding multiple tenant IDs.
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - access_token_expires_in: The number of seconds until the access token expires.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
      - refresh_token: The `refresh_token` that you may use to obtain a new `access_token` for the User within the provider's API.
    """  # noqa

    provider_subject: str
    provider_tenant_id: str
    access_token: str
    access_token_expires_in: int
    scopes: List[str]
    refresh_token: Optional[str] = None


class MemberConnectedApp(pydantic.BaseModel):
    """
    Fields:
      - connected_app_id: The ID of the Connected App.
      - name: The name of the Connected App.
      - description: A description of the Connected App.
      - client_type: The type of Connected App. Supported values are `first_party`, `first_party_public`, `third_party`, and `third_party_public`.
      - scopes_granted: The scopes granted to the Connected App at the completion of the last authorization flow.
      - logo_url: The logo URL of the Connected App, if any.
    """  # noqa

    connected_app_id: str
    name: str
    description: str
    client_type: str
    scopes_granted: str
    logo_url: Optional[str] = None


class MemberRoleSource(pydantic.BaseModel):
    """
    Fields:
      - type: The type of role assignment. The possible values are:

      `direct_assignment` – an explicitly assigned Role.

      Directly assigned roles can be updated by passing in the `roles` argument to the
      [Update Member](https://stytch.com/docs/b2b/api/update-member) endpoint.

      `email_assignment` – an implicit Role granted by the Member's email domain, regardless of their login method.

      Email implicit role assignments can be updated by passing in the `rbac_email_implicit_role_assignments` argument to
      the [Update Organization](https://stytch.com/docs/b2b/api/update-organization) endpoint.

      `sso_connection` – an implicit Role granted by the Member's SSO connection. This is currently only available
      for SAML connections and not for OIDC. If the Member has a SAML Member registration with the given connection, this
      role assignment will appear in the list. However, for authorization check purposes (in
      [sessions authenticate](https://stytch.com/docs/b2b/api/authenticate-session) or in any endpoint that enforces RBAC with session
      headers), the Member will only be granted the Role if their session contains an authentication factor with the
      specified SAML connection.

      SAML connection implicit role assignments can be updated by passing in the
      `saml_connection_implicit_role_assignments` argument to the
      [Update SAML connection](https://stytch.com/docs/b2b/api/update-saml-connection) endpoint.

      `sso_connection_group` – an implicit Role granted by the Member's SSO connection and group. This is currently only
      available for SAML connections and not for OIDC. If the Member has a SAML Member registration with the given
      connection, and belongs to a specific group within the IdP, this role assignment will appear in the list. However,
      for authorization check purposes (in [sessions authenticate](https://stytch.com/docs/b2b/api/authenticate-session) or in any endpoint
      that enforces RBAC with session headers), the Member will only be granted the role if their session contains an
      authentication factor with the specified SAML connection.

      SAML group implicit role assignments can be updated by passing in the `saml_group_implicit_role_assignments`
      argument to the [Update SAML connection](https://stytch.com/docs/b2b/api/update-saml-connection) endpoint.

        `scim_connection_group` – an implicit Role granted by the Member's SCIM connection and group. If the Member has
      a SCIM Member registration with the given connection, and belongs to a specific group within the IdP, this role assignment will appear in the list.

      SCIM group implicit role assignments can be updated by passing in the `scim_group_implicit_role_assignments`
      argument to the [Update SCIM connection](https://stytch.com/docs/b2b/api/update-scim-connection) endpoint.

      - details: An object containing additional metadata about the source assignment. The fields will vary depending
      on the role assignment type as follows:

      `direct_assignment` – no additional details.

      `email_assignment` – will contain the email domain that granted the assignment.

      `sso_connection` – will contain the `connection_id` of the SAML connection that granted the assignment.

      `sso_connection_group` – will contain the `connection_id` of the SAML connection and the name of the `group`
      that granted the assignment.

      `scim_connection_group` – will contain the `connection_id` of the SAML connection and the `group_id`
      that granted the assignment.

    """  # noqa

    type: str
    details: Optional[Dict[str, Any]] = None


class MemberRole(pydantic.BaseModel):
    """
    Fields:
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


      - sources: A list of sources for this role assignment. A role assignment can come from multiple sources - for example, the Role could be both explicitly assigned and implicitly granted from the Member's email domain.
    """  # noqa

    role_id: str
    sources: List[MemberRoleSource]


class OAuthRegistration(pydantic.BaseModel):
    """
    Fields:
      - provider_type: Denotes the OAuth identity provider that the user has authenticated with, e.g. Google, Microsoft, GitHub etc.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - member_oauth_registration_id: The unique ID of an OAuth registration.
      - profile_picture_url: If available, the `profile_picture_url` is a URL of the User's profile picture set in OAuth identity the provider that the User has authenticated with, e.g. Google profile picture.
      - locale: If available, the `locale` is the Member's locale set in the OAuth identity provider that the user has authenticated with.
    """  # noqa

    provider_type: str
    provider_subject: str
    member_oauth_registration_id: str
    profile_picture_url: Optional[str] = None
    locale: Optional[str] = None


class OIDCProviderInfo(pydantic.BaseModel):
    """
    Fields:
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - id_token: The `id_token` returned by the OAuth provider. ID Tokens are JWTs that contain structured information about a user. The exact content of each ID Token varies from provider to provider. ID Tokens are returned from OAuth providers that conform to the [OpenID Connect](https://openid.net/foundation/) specification, which is based on OAuth.
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - access_token_expires_in: The number of seconds until the access token expires.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
      - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
      - refresh_token: The `refresh_token` that you may use to obtain a new `access_token` for the User within the provider's API.
    """  # noqa

    provider_subject: str
    id_token: str
    access_token: str
    access_token_expires_in: int
    scopes: List[str]
    connection_id: str
    refresh_token: Optional[str] = None


class Organization(pydantic.BaseModel):
    """
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
      - organization_name: The name of the Organization. Must be between 1 and 128 characters in length.
      - organization_logo_url: The image URL of the Organization logo.
      - organization_slug: The unique URL slug of the Organization. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`. Must be between 2 and 128 characters in length. Wherever an organization_id is expected in a path or request parameter, you may also use the organization_slug as a convenience.
      - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

      `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

      `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

      `NOT_ALLOWED` – disable JIT provisioning via SSO.

      - sso_jit_provisioning_allowed_connections: An array of `connection_id`s that reference [SAML Connection objects](https://stytch.com/docs/b2b/api/saml-connection-object).
      Only these connections will be allowed to JIT provision Members via SSO when `sso_jit_provisioning` is set to `RESTRICTED`.
      - sso_active_connections: An array of active [SAML Connection references](https://stytch.com/docs/b2b/api/saml-connection-object) or [OIDC Connection references](https://stytch.com/docs/b2b/api/oidc-connection-object).
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

      - mfa_policy: (no documentation yet)
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

      - claimed_email_domains: (no documentation yet)
      - first_party_connected_apps_allowed_type: The authentication setting that sets the Organization's policy towards first party Connected Apps. The accepted values are:

      `ALL_ALLOWED` – any first party Connected App in the Project is permitted for use by Members.

      `RESTRICTED` – only first party Connected Apps with IDs in `allowed_first_party_connected_apps` can be used by Members.

      `NOT_ALLOWED` – no first party Connected Apps are permitted.

      - allowed_first_party_connected_apps: An array of first party Connected App IDs that are allowed for the Organization. Only used when the Organization's `first_party_connected_apps_allowed_type` is `RESTRICTED`.
      - third_party_connected_apps_allowed_type: The authentication setting that sets the Organization's policy towards third party Connected Apps. The accepted values are:

      `ALL_ALLOWED` – any third party Connected App in the Project is permitted for use by Members.

      `RESTRICTED` – only third party Connected Apps with IDs in `allowed_first_party_connected_apps` can be used by Members.

      `NOT_ALLOWED` – no third party Connected Apps are permitted.

      - allowed_third_party_connected_apps: An array of third party Connected App IDs that are allowed for the Organization. Only used when the Organization's `third_party_connected_apps_allowed_type` is `RESTRICTED`.
      - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
      - created_at: The timestamp of the Organization's creation. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - updated_at: The timestamp of when the Organization was last updated. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - sso_default_connection_id: The default connection used for SSO when there are multiple active connections.
      - scim_active_connection: An active [SCIM Connection references](https://stytch.com/docs/b2b/api/scim-connection-object).
      - allowed_oauth_tenants: A map of allowed OAuth tenants. If this field is not passed in, the Organization will not allow JIT provisioning by OAuth Tenant. Allowed keys are "slack", "hubspot", and "github".
    """  # noqa

    organization_id: str
    organization_name: str
    organization_logo_url: str
    organization_slug: str
    sso_jit_provisioning: str
    sso_jit_provisioning_allowed_connections: List[str]
    sso_active_connections: List[ActiveSSOConnection]
    email_allowed_domains: List[str]
    email_jit_provisioning: str
    email_invites: str
    auth_methods: str
    allowed_auth_methods: List[str]
    mfa_policy: str
    rbac_email_implicit_role_assignments: List[EmailImplicitRoleAssignment]
    mfa_methods: str
    allowed_mfa_methods: List[str]
    oauth_tenant_jit_provisioning: str
    claimed_email_domains: List[str]
    first_party_connected_apps_allowed_type: str
    allowed_first_party_connected_apps: List[str]
    third_party_connected_apps_allowed_type: str
    allowed_third_party_connected_apps: List[str]
    trusted_metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    sso_default_connection_id: Optional[str] = None
    scim_active_connection: Optional[ActiveSCIMConnection] = None
    allowed_oauth_tenants: Optional[Dict[str, Any]] = None


class OrganizationConnectedApp(pydantic.BaseModel):
    connected_app_id: str
    name: str
    description: str
    client_type: str
    logo_url: Optional[str] = None


class OrganizationConnectedAppActiveMember(pydantic.BaseModel):
    """
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - granted_scopes: Scopes that were granted at the completion of the last authorization flow.
    """  # noqa

    member_id: str
    granted_scopes: List[str]


class ResultsMetadata(pydantic.BaseModel):
    """
    Fields:
      - total: The total number of results returned by your search query. If totals have been disabled for your Stytch Workspace to improve search performance, the value will always be -1.
      - next_cursor: The `next_cursor` string is returned when your search result contains more than one page of results. This value is passed into your next search call in the `cursor` field.
    """  # noqa

    total: int
    next_cursor: Optional[str] = None


class RetiredEmail(pydantic.BaseModel):
    """
    Fields:
      - email_id: The globally unique UUID of a Member's email.
      - email_address: The email address of the Member.
    """  # noqa

    email_id: str
    email_address: str


class SCIMRegistration(pydantic.BaseModel):
    """
    Fields:
      - connection_id: The ID of the SCIM connection.
      - registration_id: The unique ID of a SCIM Registration.
      - external_id: The ID of the member given by the identity provider.
      - scim_attributes: An object for storing SCIM attributes brought over from the identity provider.
    """  # noqa

    connection_id: str
    registration_id: str
    external_id: Optional[str] = None
    scim_attributes: Optional[SCIMAttributes] = None


class SSORegistration(pydantic.BaseModel):
    """
    Fields:
      - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
      - external_id: The ID of the member given by the identity provider.
      - registration_id: The unique ID of an SSO Registration.
      - sso_attributes: An object for storing SSO attributes brought over from the identity provider.
    """  # noqa

    connection_id: str
    external_id: str
    registration_id: str
    sso_attributes: Optional[Dict[str, Any]] = None


class Member(pydantic.BaseModel):
    """
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
      - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value. You may use an external_id here if one is set for the member.
      - email_address: The email address of the Member.
      - status: The status of the Member. The possible values are: `pending`, `invited`, `active`, or `deleted`.
      - name: The name of the Member.
      - sso_registrations: An array of registered [SAML Connection](saml-connection-object) or [OIDC Connection](oidc-connection-object) objects the Member has authenticated with.
      - is_breakglass: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
      - member_password_id: Globally unique UUID that identifies a Member's password.
      - oauth_registrations: A list of OAuth registrations for this member.
      - email_address_verified: Whether or not the Member's email address is verified.
      - mfa_phone_number_verified: Whether or not the Member's phone number is verified.
      - is_admin: Whether or not the Member has the `stytch_admin` Role. This Role is automatically granted to Members
      who create an Organization through the [discovery flow](https://stytch.com/docs/b2b/api/create-organization-via-discovery). See the
      [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for more details on this Role.
      - totp_registration_id: (no documentation yet)
      - retired_email_addresses:
      A list of retired email addresses for this member.
      A previously active email address can be marked as retired in one of two ways:
      - It's replaced with a new primary email address during an explicit Member update.
      - A new email address is surfaced by an OAuth, SAML or OIDC provider. In this case the new email address becomes the
      Member's primary email address and the old primary email address is retired.

      A retired email address cannot be used by other Members in the same Organization. However, unlinking retired email
      addresses allows them to be subsequently re-used by other Organization Members. Retired email addresses can be unlinked
      using the [Unlink Retired Email endpoint](https://stytch.com/docs/b2b/api/unlink-retired-member-email).

      - is_locked: (no documentation yet)
      - mfa_enrolled: Sets whether the Member is enrolled in MFA. If true, the Member must complete an MFA step whenever they wish to log in to their Organization. If false, the Member only needs to complete an MFA step if the Organization's MFA policy is set to `REQUIRED_FOR_ALL`.
      - mfa_phone_number: The Member's phone number. A Member may only have one phone number. The phone number should be in E.164 format (i.e. +1XXXXXXXXXX).
      - default_mfa_method: (no documentation yet)
      - roles: Explicit or implicit Roles assigned to this Member, along with details about the role assignment source.
       See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.
      - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
      - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
      frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
      for complete field behavior details.
      - created_at: The timestamp of the Member's creation. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - updated_at: The timestamp of when the Member was last updated. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - scim_registration: A scim member registration, referencing a [SCIM Connection](scim-connection-object) object in use for the Member creation.
      - external_id: The ID of the member given by the identity provider.
      - lock_created_at: (no documentation yet)
      - lock_expires_at: (no documentation yet)
    """  # noqa

    organization_id: str
    member_id: str
    email_address: str
    status: str
    name: str
    sso_registrations: List[SSORegistration]
    is_breakglass: bool
    member_password_id: str
    oauth_registrations: List[OAuthRegistration]
    email_address_verified: bool
    mfa_phone_number_verified: bool
    is_admin: bool
    totp_registration_id: str
    retired_email_addresses: List[RetiredEmail]
    is_locked: bool
    mfa_enrolled: bool
    mfa_phone_number: str
    default_mfa_method: str
    roles: List[MemberRole]
    trusted_metadata: Optional[Dict[str, Any]] = None
    untrusted_metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    scim_registration: Optional[SCIMRegistration] = None
    external_id: Optional[str] = None
    lock_created_at: Optional[datetime.datetime] = None
    lock_expires_at: Optional[datetime.datetime] = None


class SearchQuery(pydantic.BaseModel):
    """
    Fields:
      - operator: The action to perform on the operands. The accepted value are:

      `AND` – all the operand values provided must match.

      `OR` – the operator will return any matches to at least one of the operand values you supply.
      - operands: An array of operand objects that contains all of the filters and values to apply to your search query.
    """  # noqa

    operator: SearchQueryOperator
    operands: List[Dict[str, Any]]


class SlackProviderInfo(pydantic.BaseModel):
    """
    Fields:
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - provider_tenant_id: The tenant ID returned by the OAuth provider. This is typically used to identify an organization or group within the provider's domain. For example, in HubSpot this is a Hub ID, in Slack this is the Workspace ID, and in GitHub this is an organization ID. This field will only be populated if exactly one tenant ID is returned from a successful OAuth authentication and developers should prefer `provider_tenant_ids` over this since it accounts for the possibility of an OAuth provider yielding multiple tenant IDs.
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
      - bot_access_token: The `access_token` that you may use to access data as a bot application in Slack. Use in conjunction with `bot_scopes`.
      - bot_scopes: The scopes that the bot application has access to in Slack.
    """  # noqa

    provider_subject: str
    provider_tenant_id: str
    access_token: str
    scopes: List[str]
    bot_access_token: str
    bot_scopes: List[str]


class UpdateRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class ConnectedAppsResponse(ResponseBase):
    """Response type for `Organizations.connected_apps`.
    Fields:
      - connected_apps: (no documentation yet)
    """  # noqa

    connected_apps: List[OrganizationConnectedApp]


class CreateResponse(ResponseBase):
    """Response type for `Organizations.create`.
    Fields:
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    organization: Organization


class DeleteResponse(ResponseBase):
    """Response type for `Organizations.delete`.
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
    """  # noqa

    organization_id: str


class GetConnectedAppResponse(ResponseBase):
    """Response type for `Organizations.get_connected_app`.
    Fields:
      - connected_app_id: The ID of the Connected App.
      - name: The name of the Connected App.
      - description: A description of the Connected App.
      - client_type: The type of Connected App. Supported values are `first_party`, `first_party_public`, `third_party`, and `third_party_public`.
      - active_members: Details about Members who has installed a Connected App.
      - logo_url: (no documentation yet)
    """  # noqa

    connected_app_id: str
    name: str
    description: str
    client_type: str
    active_members: List[OrganizationConnectedAppActiveMember]
    logo_url: Optional[str] = None


class GetResponse(ResponseBase):
    """Response type for `Organizations.get`.
    Fields:
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    organization: Organization


class MetricsResponse(ResponseBase):
    member_count: int


class SearchResponse(ResponseBase):
    """Response type for `Organizations.search`.
    Fields:
      - organizations: An array of [Organization objects](https://stytch.com/docs/b2b/api/organization-object).
      - results_metadata: The search `results_metadata` object contains metadata relevant to your specific query like `total` and `next_cursor`.
    """  # noqa

    organizations: List[Organization]
    results_metadata: ResultsMetadata


class UpdateResponse(ResponseBase):
    """Response type for `Organizations.update`.
    Fields:
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    organization: Organization
