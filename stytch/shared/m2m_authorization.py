import collections
from typing import List


class M2MPermissionError(PermissionError):
    def __init__(self, has_scopes: List[str], missing_scope: str) -> None:
        self.has_scopes = has_scopes
        self.missing_scope = missing_scope

    def __str__(self):
        return f"Permission denied. Client has scopes {self.has_scopes} but is missing scope: {self.missing_scope}"


def perform_authorization_check(
    has_scopes: List[str],
    required_scopes: List[str],
) -> None:
    """Performs an authorization check against an M2M client and a set of required
    scopes. If the check fails, a PermissionError will be raised.
    """
    client_scopes = collections.defaultdict(set)
    for scope in has_scopes:
        if ":" not in scope:
            client_scopes[scope].add("*")
        else:
            action, resource = scope.split(":")
            client_scopes[action].add(resource)

    for required_scope in required_scopes:
        required_action = required_scope
        required_resource = "*"
        if ":" in required_scope:
            required_action, required_resource = required_scope.split(":")
        if required_action not in client_scopes:
            raise M2MPermissionError(has_scopes, required_scope)
        resources = client_scopes[required_action]

        # The client can either have a wildcard resource or the specific resource
        if "*" not in resources and required_resource not in resources:
            raise M2MPermissionError(has_scopes, required_scope)
