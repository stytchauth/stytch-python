import unittest

from stytch.b2b.models.rbac import Policy, PolicyRole, PolicyRolePermission
from stytch.shared.rbac_local import (
    AuthZRequest,
    RBACPermissionError,
    TenancyError,
    perform_authorization_check,
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
        self.policy = Policy(
            resources=[],
            roles=[self.admin, self.global_writer, self.global_reader, self.bar_writer],
        )

    def test_perform_authorization_check(self) -> None:
        with self.subTest("tenancy mismatch"):
            with self.assertRaises(TenancyError):
                # Arrange
                roles = [self.admin.role_id]
                org_id = "my_org"
                req = AuthZRequest(
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
                req = AuthZRequest(
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
                req = AuthZRequest(
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
            req = AuthZRequest(
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
            req = AuthZRequest(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_authorization_check(self.policy, roles, org_id, req)
            # Assertion is that no exception is raised
