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

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase
from stytch.shared.method_options import Authorization


class AuthenticateRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class ConnectionImplicitRoleAssignment(pydantic.BaseModel):
    role_id: str


class DeleteConnectionRequestOptions(pydantic.BaseModel):
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


class GetConnectionsRequestOptions(pydantic.BaseModel):
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


class GroupImplicitRoleAssignment(pydantic.BaseModel):
    role_id: str
    group: str


class Connection(pydantic.BaseModel):
    organization_id: str
    connection_id: str
    external_organization_id: str
    external_connection_id: str
    display_name: str
    status: str
    external_connection_implicit_role_assignments: List[
        ConnectionImplicitRoleAssignment
    ]
    external_group_implicit_role_assignments: List[GroupImplicitRoleAssignment]


class OIDCConnection(pydantic.BaseModel):
    organization_id: str
    connection_id: str
    status: str
    display_name: str
    redirect_url: str
    client_id: str
    client_secret: str
    issuer: str
    authorization_url: str
    token_url: str
    userinfo_url: str
    jwks_url: str
    identity_provider: str


class SAMLConnectionImplicitRoleAssignment(pydantic.BaseModel):
    """
    Fields:
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


    """  # noqa

    role_id: str


class SAMLGroupImplicitRoleAssignment(pydantic.BaseModel):
    """
    Fields:
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


      - group: The name of the SAML group that grants the specified role assignment.
    """  # noqa

    role_id: str
    group: str


class X509Certificate(pydantic.BaseModel):
    certificate_id: str
    certificate: str
    issuer: str
    created_at: Optional[datetime.datetime] = None
    expires_at: Optional[datetime.datetime] = None


class SAMLConnection(pydantic.BaseModel):
    organization_id: str
    connection_id: str
    status: str
    idp_entity_id: str
    display_name: str
    idp_sso_url: str
    acs_url: str
    audience_uri: str
    signing_certificates: List[X509Certificate]
    verification_certificates: List[X509Certificate]
    saml_connection_implicit_role_assignments: List[
        SAMLConnectionImplicitRoleAssignment
    ]
    saml_group_implicit_role_assignments: List[SAMLGroupImplicitRoleAssignment]
    alternative_audience_uri: str
    identity_provider: str
    attribute_mapping: Optional[Dict[str, Any]] = None


class AuthenticateResponse(ResponseBase):
    """Response type for `SSO.authenticate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - reset_session: Indicates if all Sessions linked to the Member need to be reset. You should check this field if you aren't using
        Stytch's Session product. If you are using Stytch's Session product, we revoke the Member’s other Sessions for you.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - intermediate_session_token: The returned Intermediate Session Token contains an SSO factor associated with the Member. If this value is non-empty, the member must complete an MFA step to finish logging in to the Organization. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. SSO factors are not transferable between Organizations, so the intermediate session token is not valid for use with discovery endpoints.
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
    """  # noqa

    member_id: str
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    reset_session: bool
    organization: Organization
    intermediate_session_token: str
    member_authenticated: bool
    member_session: Optional[MemberSession] = None
    mfa_required: Optional[MfaRequired] = None


class DeleteConnectionResponse(ResponseBase):
    """Response type for `SSO.delete_connection`.
    Fields:
      - connection_id: The `connection_id` that was deleted as part of the delete request.
    """  # noqa

    connection_id: str


class GetConnectionsResponse(ResponseBase):
    """Response type for `SSO.get_connections`.
    Fields:
      - saml_connections: The list of [SAML Connections](https://stytch.com/docs/b2b/api/saml-connection-object) owned by this organization.
      - oidc_connections: The list of [OIDC Connections](https://stytch.com/docs/b2b/api/oidc-connection-object) owned by this organization.
      - external_connections: (no documentation yet)
    """  # noqa

    saml_connections: List[SAMLConnection]
    oidc_connections: List[OIDCConnection]
    external_connections: List[Connection]
