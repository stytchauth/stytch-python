# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import PrimaryRequired


class Membership(pydantic.BaseModel):
    """
    Fields:
      - type: Either `active_member`, `pending_member`, `invited_member`, `eligible_to_join_by_email_domain`, or `eligible_to_join_by_oauth_tenant`
      - details: An object containing additional metadata about the membership, if available.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object) if one already exists, or null if one does not.
    """  # noqa

    type: str
    details: Optional[Dict[str, Any]] = None
    member: Optional[Member] = None


class DiscoveredOrganization(pydantic.BaseModel):
    """
    Fields:
      - member_authenticated: Indicates whether the Member has all of the factors needed to fully authenticate to this Organization. If false, the Member may need to complete an MFA step or complete a different primary authentication flow. See the `primary_required` and `mfa_required` fields for more details on each.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - membership: Information about the membership.
      - primary_required: Information about the primary authentication requirements of the Organization.
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
    """  # noqa

    member_authenticated: bool
    organization: Optional[Organization] = None
    membership: Optional[Membership] = None
    primary_required: Optional[PrimaryRequired] = None
    mfa_required: Optional[MfaRequired] = None
