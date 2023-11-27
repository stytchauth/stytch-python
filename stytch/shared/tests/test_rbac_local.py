import unittest

import pydantic

from stytch.shared.rbac_local import (
    AuthZRequest,
    RBACPermissionError,
    TenancyError,
    perform_authorization_check,
)


class Permission(pydantic.BaseModel):
    actions: list[str]
    resources: list[str]


class Role(pydantic.BaseModel):
    role_id: str
    permissions: list[Permission]


class Policy(pydantic.BaseModel):
    roles: list[Role]


class TestRbacLocal(unittest.TestCase):
    def setUp(self) -> None:
        self.admin = Role(
            role_id="admin",
            permissions=[Permission(actions=["*"], resources=["foo", "bar"])],
        )
        self.global_writer = Role(
            role_id="global_writer",
            permissions=[
                Permission(actions=["write", "read"], resources=["foo", "bar"])
            ],
        )
        self.global_reader = Role(
            role_id="global_reader",
            permissions=[Permission(actions=["read"], resources=["foo", "bar"])],
        )
        self.bar_writer = Role(
            role_id="bar_writer",
            permissions=[Permission(actions=["write", "read"], resources=["bar"])],
        )
        self.policy = Policy(
            roles=[self.admin, self.global_writer, self.global_reader, self.bar_writer]
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
