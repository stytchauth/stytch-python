from __future__ import annotations

from typing import List

import pydantic

from stytch.b2b.models.rbac import Policy


class TenancyError(ValueError):
    def __init__(self, subject_org_id: str, request_org_id: str) -> None:
        self.subject_org_id = subject_org_id
        self.request_org_id = request_org_id

    def __str__(self):
        return (
            f"Subject organization ID {self.subject_org_id} does not "
            f"match request organization ID {self.request_org_id}"
        )


class RBACPermissionError(ValueError):
    def __init__(self, authz_request: AuthZRequest) -> None:
        self.authz_request = authz_request

    def __str__(self):
        return f"Permission denied for {self.authz_request}"


class AuthZRequest(pydantic.BaseModel):
    organization_id: str
    resource_id: str
    action: str


def perform_authorization_check(
    policy: Policy,
    subject_roles: List[str],
    subject_org_id: str,
    authz_request: AuthZRequest,
) -> None:
    """Performs an authorization check against a policy and a set of roles. If the check
    succeeds, this method will return. If the check fails, a PermissionError will be
    raised. It's also possible for a TenancyError to be raised if the subject_org_id
    does not match the authZ request organization_id.
    """
    if subject_org_id != authz_request.organization_id:
        raise TenancyError(subject_org_id, authz_request.organization_id)

    for role in policy.roles:
        if role.role_id in subject_roles:
            for permission in role.permissions:
                has_matching_action = (
                    "*" in permission.actions
                    or authz_request.action in permission.actions
                )
                has_matching_resource = (
                    authz_request.resource_id in permission.resources
                )
                if has_matching_action and has_matching_resource:
                    # All good, we found a matching permission
                    return

    # If we made it here, we didn't find a matching permission
    raise PermissionError(authz_request)
