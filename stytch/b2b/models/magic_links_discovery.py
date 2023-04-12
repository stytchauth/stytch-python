#!/usr/bin/env python3

from typing import List

from stytch.b2b.core.models import DiscoveredOrganization
from stytch.core.models import ResponseBase


class AuthenticateResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `intermediate_session_token`: The Intermediate Session Token. This token does not belong to a specific instance of a member, but may be exchanged for an existing Member Session or used to create a new organization.

    - `email_address`: The email address associated with the intermediate session token.

    - `discovered_organizations`: An array of `discovered_organization` objects tied to the `intermediate_session_token`. See the [Discovered Organization Object](https://stytch.com/docs/b2b/api/discovered-organization-object) for complete details.
    """  # noqa

    intermediate_session_token: str
    email_address: str
    discovered_organizations: List[DiscoveredOrganization]
