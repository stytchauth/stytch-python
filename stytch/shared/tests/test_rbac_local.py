import unittest

from stytch.b2b.models.rbac import Policy, PolicyRole, PolicyRolePermission, PolicyScope, PolicyScopePermission
from stytch.b2b.models.sessions import AuthorizationCheck
from stytch.shared.rbac_local import (
    RBACPermissionError,
    TenancyError,
    perform_authorization_check,
    perform_scope_authorization_check,
)


class TestRbacLocal(unittest.TestCase):
    def setUp(self) -> None:
        self.admin = PolicyRole(
            role_id="admin",
            description="Admin role",
            permissions=[
                PolicyRolePermission(actions=["*"], resource_id="foo"),
                PolicyRolePermission(actions=["*"], resource_id="bar"),
            ],
        )
        self.global_writer = PolicyRole(
            role_id="global_writer",
            description="Global writer role",
            permissions=[
                PolicyRolePermission(actions=["write", "read"], resource_id="foo"),
                PolicyRolePermission(actions=["write", "read"], resource_id="bar"),
            ],
        )
        self.global_reader = PolicyRole(
            role_id="global_reader",
            description="Global reader role",
            permissions=[
                PolicyRolePermission(actions=["read"], resource_id="foo"),
                PolicyRolePermission(actions=["read"], resource_id="bar"),
            ],
        )
        self.bar_writer = PolicyRole(
            role_id="bar_writer",
            description="Bar writer role",
            permissions=[
                PolicyRolePermission(actions=["write", "read"], resource_id="bar")
            ],
        )
        self.read_scope = PolicyScope(
            scope="read:documents",
            description="Read documents",
            permissions=[
                PolicyScopePermission(actions=["read"], resource_id="foo"),
                PolicyScopePermission(actions=["read"], resource_id="bar"),
            ],
        )
        self.write_scope = PolicyScope(
            scope="write:documents",
            description="Write documents",
            permissions=[
                PolicyScopePermission(actions=["write", "read"], resource_id="foo"),
                PolicyScopePermission(actions=["write", "read"], resource_id="bar"),
            ],
        )
        self.wildcard_scope = PolicyScope(
            scope="wildcard:documents",
            description="Wildcard documents",
            permissions=[
                PolicyScopePermission(actions=["*"], resource_id="foo"),
                PolicyScopePermission(actions=["*"], resource_id="bar"),
            ],
        )
        self.policy = Policy(
            resources=[],
            roles=[self.admin, self.global_writer, self.global_reader, self.bar_writer],
            scopes=[self.read_scope, self.write_scope, self.wildcard_scope],
        )

    def test_perform_authorization_check(self) -> None:
        with self.subTest("tenancy mismatch"):
            with self.assertRaises(TenancyError):
                # Arrange
                roles = [self.admin.role_id]
                org_id = "my_org"
                req = AuthorizationCheck(
                    organization_id="other_org",
                    resource_id="foo",
                    action="write",
                )
                # Act
                perform_authorization_check(self.policy, roles, org_id, req)

        with self.subTest("has matching action but not resource"):
            with self.assertRaises(RBACPermissionError):
                # Arrange
                roles = [self.global_writer.role_id]
                org_id = "my_org"
                req = AuthorizationCheck(
                    organization_id=org_id,
                    resource_id="baz",
                    action="write",
                )
                # Act
                perform_authorization_check(self.policy, roles, org_id, req)

        with self.subTest("has matching resource but not action"):
            with self.assertRaises(RBACPermissionError):
                # Arrange
                roles = [self.global_reader.role_id]
                org_id = "my_org"
                req = AuthorizationCheck(
                    organization_id=org_id,
                    resource_id="foo",
                    action="write",
                )
                # Act
                perform_authorization_check(self.policy, roles, org_id, req)

        with self.subTest("has matching resource and specific action"):
            # Arrange
            roles = [self.global_writer.role_id]
            org_id = "my_org"
            req = AuthorizationCheck(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_authorization_check(self.policy, roles, org_id, req)
            # Assertion is that no exception is raised

        with self.subTest("has matching resource and star action"):
            # Arrange
            roles = [self.admin.role_id]
            org_id = "my_org"
            req = AuthorizationCheck(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_authorization_check(self.policy, roles, org_id, req)
            # Assertion is that no exception is raised

    def test_perform_scope_authorization_check(self) -> None:
        with self.subTest("has matching action but not resource"):
            with self.assertRaises(RBACPermissionError):
                # Arrange
                scopes = [self.write_scope.scope]
                org_id = "my_org"
                req = AuthorizationCheck(
                    organization_id=org_id,
                    resource_id="baz",
                    action="write",
                )
                # Act
                perform_scope_authorization_check(self.policy, scopes, org_id, req)

        with self.subTest("has matching resource but not action"):
            with self.assertRaises(RBACPermissionError):
                # Arrange
                scopes = [self.read_scope.scope]
                org_id = "my_org"
                req = AuthorizationCheck(
                    organization_id=org_id,
                    resource_id="foo",
                    action="write",
                )
                # Act
                perform_scope_authorization_check(self.policy, scopes, org_id, req)

        with self.subTest("has matching resource and specific action"):
            # Arrange
            scopes = [self.write_scope.scope]
            org_id = "my_org"
            req = AuthorizationCheck(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_scope_authorization_check(self.policy, scopes, org_id, req)
            # Assertion is that no exception is raised

        with self.subTest("has matching resource and star action"):
            # Arrange
            scopes = [self.wildcard_scope.scope]
            org_id = "my_org"
            req = AuthorizationCheck(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_scope_authorization_check(self.policy, scopes, org_id, req)
            # Assertion is that no exception is raised
