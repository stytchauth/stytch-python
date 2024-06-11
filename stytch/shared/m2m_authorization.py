import collections
from typing import List

import pydantic


class AuthorizationCheckParams(pydantic.BaseModel):
    has_scopes: List[str]
    required_scopes: List[str]


def perform_authorization_check(params: AuthorizationCheckParams) -> bool:
    """Performs an authorization check against an M2M client and a set of required
    scopes. Returns True if the client has all the required scopes, False otherwise.
    A scope can match if the client has a wildcard resource or the specific resource.
    This function assumes that scopes are of the form "action:resource" or just
    "specific_scope". It is _also_ possible to represent scopes as "resource:action",
    but it is ultimately up to the developer to ensure consistency in the scopes format.

    Note that a scope of "*" will only match another literal "*" because wildcards are
    *not* supported in the prefix piece of a scope.
    """
    client_scopes = collections.defaultdict(set)
    for scope in params.has_scopes:
        if ":" not in scope:
            client_scopes[scope].add("-")
        else:
            action, resource = scope.split(":")
            client_scopes[action].add(resource)

    for required_scope in params.required_scopes:
        required_action = required_scope
        required_resource = "-"
        if ":" in required_scope:
            required_action, required_resource = required_scope.split(":")
        if required_action not in client_scopes:
            return False
        resources = client_scopes[required_action]

        # The client can either have a wildcard resource or the specific resource
        if "*" not in resources and required_resource not in resources:
            return False

    # If we haven't returned False yet, the client has all the required scopes
    return True
