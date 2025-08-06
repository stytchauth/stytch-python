from __future__ import annotations

from typing import List, Union

import pydantic

from stytch.b2b.models.rbac import Policy as B2BPolicy
from stytch.b2b.models.sessions import AuthorizationCheck
from stytch.consumer.models.rbac import Policy as ConsumerPolicy
from stytch.consumer.models.sessions import (
    AuthorizationCheck as ConsumerAuthorizationCheck,
)


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
    def __init__(self, authorization_check: AuthorizationCheck) -> None:
        self.authorization_check = authorization_check

    def __str__(self):
        return f"Permission denied for {self.authorization_check}"


class RBACConsumerPermissionError(ValueError):
    def __init__(self, authorization_check: ConsumerAuthorizationCheck) -> None:
        self.authorization_check = authorization_check

    def __str__(self):
        return f"Permission denied for {self.authorization_check}"


class PolicyResource(pydantic.BaseModel):
    resource_id: str
    description: str
    actions: List[str]


class PolicyRolePermission(pydantic.BaseModel):
    resource_id: str
    actions: List[str]


class PolicyRole(pydantic.BaseModel):
    role_id: str
    description: str
    permissions: List[PolicyRolePermission]


class PolicyScopePermission(pydantic.BaseModel):
    resource_id: str
    actions: List[str]


class PolicyScope(pydantic.BaseModel):
    scope: str
    description: str
    permissions: List[PolicyScopePermission]


class Policy(pydantic.BaseModel):
    roles: List[PolicyRole]
    resources: List[PolicyResource]
    scopes: List[PolicyScope]


def policy_from_b2b_policy(policy: B2BPolicy) -> Policy:
    roles = []
    for role in policy.roles:
        roles.append(
            PolicyRole(
                role_id=role.role_id,
                description=role.description,
                permissions=[
                    PolicyRolePermission(
                        resource_id=permission.resource_id, actions=permission.actions
                    )
                    for permission in role.permissions
                ],
            )
        )
    resources = []
    for resource in policy.resources:
        resources.append(
            PolicyResource(
                resource_id=resource.resource_id,
                description=resource.description,
                actions=resource.actions,
            )
        )
    scopes = []
    for scope in policy.scopes:
        scopes.append(
            PolicyScope(
                scope=scope.scope,
                description=scope.description,
                permissions=[
                    PolicyScopePermission(
                        resource_id=permission.resource_id, actions=permission.actions
                    )
                    for permission in scope.permissions
                ],
            )
        )
    return Policy(
        roles=roles,
        resources=resources,
        scopes=scopes,
    )


def policy_from_consumer_policy(policy: ConsumerPolicy) -> Policy:
    roles = []
    for role in policy.roles:
        roles.append(
            PolicyRole(
                role_id=role.role_id,
                description=role.description,
                permissions=[
                    PolicyRolePermission(
                        resource_id=permission.resource_id, actions=permission.actions
                    )
                    for permission in role.permissions
                ],
            )
        )
    resources = []
    for resource in policy.resources:
        resources.append(
            PolicyResource(
                resource_id=resource.resource_id,
                description=resource.description,
                actions=resource.actions,
            )
        )
    scopes = []
    for scope in policy.scopes:
        scopes.append(
            PolicyScope(
                scope=scope.scope,
                description=scope.description,
                permissions=[
                    PolicyScopePermission(
                        resource_id=permission.resource_id, actions=permission.actions
                    )
                    for permission in scope.permissions
                ],
            )
        )
    return Policy(
        roles=roles,
        resources=resources,
        scopes=scopes,
    )


def perform_authorization_check(
    policy: B2BPolicy,
    subject_roles: List[str],
    subject_org_id: str,
    authorization_check: AuthorizationCheck,
) -> None:
    """Performs an authorization check against a policy and a set of roles. If the check
    succeeds, this method will return. If the check fails, a PermissionError will be
    raised. It's also possible for a TenancyError to be raised if the subject_org_id
    does not match the authZ request organization_id.
    """
    if subject_org_id != authorization_check.organization_id:
        raise TenancyError(subject_org_id, authorization_check.organization_id)

    if not is_authorized(
        policy_from_b2b_policy(policy), subject_roles, authorization_check
    ):
        raise RBACPermissionError(authorization_check)
    return


def perform_consumer_authorization_check(
    policy: ConsumerPolicy,
    subject_roles: List[str],
    authorization_check: ConsumerAuthorizationCheck,
) -> None:
    """Performs an authorization check against a policy and a set of roles. If the check
    succeeds, this method will return. If the check fails, a PermissionError will be
    raised.
    """
    if not is_authorized(
        policy_from_consumer_policy(policy), subject_roles, authorization_check
    ):
        raise RBACConsumerPermissionError(authorization_check)
    return


def is_authorized(
    policy: Policy,
    subject_roles: List[str],
    authorization_check: Union[AuthorizationCheck, ConsumerAuthorizationCheck],
) -> bool:
    for role in policy.roles:
        if role.role_id in subject_roles:
            for permission in role.permissions:
                has_matching_action = (
                    "*" in permission.actions
                    or authorization_check.action in permission.actions
                )
                has_matching_resource = (
                    authorization_check.resource_id == permission.resource_id
                )
                if has_matching_action and has_matching_resource:
                    # All good, we found a matching permission
                    return True

    # If we made it here, we didn't find a matching permission
    return False


def perform_scope_authorization_check(
    policy: B2BPolicy,
    token_scopes: List[str],
    subject_org_id: str,
    authorization_check: AuthorizationCheck,
) -> None:
    """Performs an authorization check against a policy and a set of scopes. If the check
    succeeds, this method will return. If the check fails, a PermissionError will be
    raised. It's also possible for a TenancyError to be raised if the subject_org_id
    does not match the token's organization_id.
    """
    if subject_org_id != authorization_check.organization_id:
        raise TenancyError(subject_org_id, authorization_check.organization_id)

    if scope_authorization_check(
        policy_from_b2b_policy(policy),
        token_scopes,
        authorization_check.resource_id,
        authorization_check.action,
    ):
        return
    raise RBACPermissionError(authorization_check)


def perform_consumer_scope_authorization_check(
    policy: ConsumerPolicy,
    token_scopes: List[str],
    authorization_check: ConsumerAuthorizationCheck,
) -> None:
    """Performs an authorization check against a policy and a set of scopes. If the check
    succeeds, this method will return. If the check fails, a PermissionError will be
    raised.
    """
    if not scope_authorization_check(
        policy_from_consumer_policy(policy),
        token_scopes,
        authorization_check.resource_id,
        authorization_check.action,
    ):
        raise RBACConsumerPermissionError(authorization_check)
    return


def scope_authorization_check(
    policy: Policy,
    token_scopes: List[str],
    resource_id: str,
    action: str,
) -> bool:
    for scope in policy.scopes:
        if scope.scope in token_scopes:
            for permission in scope.permissions:
                has_matching_action = (
                    "*" in permission.actions or action in permission.actions
                )
                has_matching_resource = resource_id == permission.resource_id
                if has_matching_action and has_matching_resource:
                    # All good, we found a matching permission
                    return True

    # If we made it here, we didn't find a matching permission
    return False
