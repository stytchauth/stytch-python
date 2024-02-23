# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import List

from stytch.b2b.models.discovery import DiscoveredOrganization
from stytch.core.response_base import ResponseBase


class AuthenticateResponse(ResponseBase):
    """Response type for `Discovery.authenticate`.
    Fields:
      - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session.
        The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp),
        or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow;
        the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token;
        or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
      - email_address: The email address.
      - discovered_organizations: An array of `discovered_organization` objects tied to the `intermediate_session_token`, `session_token`, or `session_jwt`. See the [Discovered Organization Object](https://stytch.com/docs/b2b/api/discovered-organization-object) for complete details.

      Note that Organizations will only appear here under any of the following conditions:
      1. The end user is already a Member of the Organization.
      2. The end user is invited to the Organization.
      3. The end user can join the Organization because:

          a) The Organization allows JIT provisioning.

          b) The Organizations' allowed domains list contains the Member's email domain.

          c) The Organization has at least one other Member with a verified email address with the same domain as the end user (to prevent phishing attacks).
    """  # noqa

    intermediate_session_token: str
    email_address: str
    discovered_organizations: List[DiscoveredOrganization]
