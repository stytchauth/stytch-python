import unittest

from stytch.b2b.api.rbac_organizations import Organizations
from stytch.b2b.models.rbac import (
    OrgPolicy,
    Policy,
    PolicyResource,
    PolicyRole,
    PolicyRolePermission,
    PolicyScope,
    PolicyScopePermission,
)
from stytch.b2b.models.sessions import AuthorizationCheck as B2BAuthorizationCheck
from stytch.consumer.models.rbac import Policy as ConsumerPolicy
from stytch.consumer.models.rbac import PolicyRole as ConsumerPolicyRole
from stytch.consumer.models.rbac import (
    PolicyRolePermission as ConsumerPolicyRolePermission,
)
from stytch.consumer.models.rbac import PolicyScope as ConsumerPolicyScope
from stytch.consumer.models.rbac import (
    PolicyScopePermission as ConsumerPolicyScopePermission,
)
from stytch.consumer.models.sessions import (
    AuthorizationCheck as ConsumerAuthorizationCheck,
)
from stytch.shared.rbac_local import (
    RBACConsumerPermissionError,
    RBACPermissionError,
    TenancyError,
    perform_authorization_check,
    perform_consumer_scope_authorization_check,
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
                req = B2BAuthorizationCheck(
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
                req = B2BAuthorizationCheck(
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
                req = B2BAuthorizationCheck(
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
            req = B2BAuthorizationCheck(
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
            req = B2BAuthorizationCheck(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_authorization_check(self.policy, roles, org_id, req)
            # Assertion is that no exception is raised

    def test_perform_scope_authorization_check(self) -> None:
        with self.subTest("tenancy mismatch"):
            with self.assertRaises(TenancyError):
                # Arrange
                scopes = [self.write_scope.scope]
                org_id = "my_org"
                req = B2BAuthorizationCheck(
                    organization_id="other_org",
                    resource_id="foo",
                    action="write",
                )
                # Act
                perform_scope_authorization_check(self.policy, scopes, org_id, req)

        with self.subTest("has matching action but not resource"):
            with self.assertRaises(RBACPermissionError):
                # Arrange
                scopes = [self.write_scope.scope]
                org_id = "my_org"
                req = B2BAuthorizationCheck(
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
                req = B2BAuthorizationCheck(
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
            req = B2BAuthorizationCheck(
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
            req = B2BAuthorizationCheck(
                organization_id=org_id,
                resource_id="foo",
                action="write",
            )
            # Act
            perform_scope_authorization_check(self.policy, scopes, org_id, req)
            # Assertion is that no exception is raised


class TestRbacLocalConsumer(unittest.TestCase):
    def setUp(self) -> None:
        self.admin = ConsumerPolicyRole(
            role_id="admin",
            description="Admin role",
            permissions=[
                ConsumerPolicyRolePermission(actions=["*"], resource_id="foo"),
                ConsumerPolicyRolePermission(actions=["*"], resource_id="bar"),
            ],
        )
        self.global_writer = ConsumerPolicyRole(
            role_id="global_writer",
            description="Global writer role",
            permissions=[
                ConsumerPolicyRolePermission(
                    actions=["write", "read"], resource_id="foo"
                ),
                ConsumerPolicyRolePermission(
                    actions=["write", "read"], resource_id="bar"
                ),
            ],
        )
        self.global_reader = ConsumerPolicyRole(
            role_id="global_reader",
            description="Global reader role",
            permissions=[
                ConsumerPolicyRolePermission(actions=["read"], resource_id="foo"),
                ConsumerPolicyRolePermission(actions=["read"], resource_id="bar"),
            ],
        )
        self.bar_writer = ConsumerPolicyRole(
            role_id="bar_writer",
            description="Bar writer role",
            permissions=[
                ConsumerPolicyRolePermission(
                    actions=["write", "read"], resource_id="bar"
                )
            ],
        )
        self.read_scope = ConsumerPolicyScope(
            scope="read:documents",
            description="Read documents",
            permissions=[
                ConsumerPolicyScopePermission(actions=["read"], resource_id="foo"),
                ConsumerPolicyScopePermission(actions=["read"], resource_id="bar"),
            ],
        )
        self.write_scope = ConsumerPolicyScope(
            scope="write:documents",
            description="Write documents",
            permissions=[
                ConsumerPolicyScopePermission(
                    actions=["write", "read"], resource_id="foo"
                ),
                ConsumerPolicyScopePermission(
                    actions=["write", "read"], resource_id="bar"
                ),
            ],
        )
        self.wildcard_scope = ConsumerPolicyScope(
            scope="wildcard:documents",
            description="Wildcard documents",
            permissions=[
                ConsumerPolicyScopePermission(actions=["*"], resource_id="foo"),
                ConsumerPolicyScopePermission(actions=["*"], resource_id="bar"),
            ],
        )
        self.policy = ConsumerPolicy(
            resources=[],
            roles=[self.admin, self.global_writer, self.global_reader, self.bar_writer],
            scopes=[self.read_scope, self.write_scope, self.wildcard_scope],
        )

    def test_perform_consumer_scope_authorization_check(self) -> None:
        with self.subTest("has matching action but not resource"):
            with self.assertRaises(RBACConsumerPermissionError):
                # Arrange
                scopes = [self.write_scope.scope]
                req = ConsumerAuthorizationCheck(
                    resource_id="baz",
                    action="write",
                )
                # Act
                perform_consumer_scope_authorization_check(self.policy, scopes, req)

        with self.subTest("has matching resource but not action"):
            with self.assertRaises(RBACConsumerPermissionError):
                # Arrange
                scopes = [self.read_scope.scope]
                req = ConsumerAuthorizationCheck(
                    resource_id="foo",
                    action="write",
                )
                # Act
                perform_consumer_scope_authorization_check(self.policy, scopes, req)

        with self.subTest("has matching resource and specific action"):
            # Arrange
            scopes = [self.write_scope.scope]
            req = ConsumerAuthorizationCheck(
                resource_id="foo",
                action="write",
            )
            # Act
            perform_consumer_scope_authorization_check(self.policy, scopes, req)
            # Assertion is that no exception is raised

        with self.subTest("has matching resource and star action"):
            # Arrange
            scopes = [self.wildcard_scope.scope]
            req = ConsumerAuthorizationCheck(
                resource_id="foo",
                action="write",
            )
            # Act
            perform_consumer_scope_authorization_check(self.policy, scopes, req)
            # Assertion is that no exception is raised

        with self.subTest("no matching scope"):
            with self.assertRaises(RBACConsumerPermissionError):
                # Arrange
                scopes = ["nonexistent:scope"]
                req = ConsumerAuthorizationCheck(
                    resource_id="foo",
                    action="read",
                )
                # Act
                perform_consumer_scope_authorization_check(self.policy, scopes, req)

        with self.subTest("empty scopes list"):
            with self.assertRaises(RBACConsumerPermissionError):
                # Arrange
                scopes = []
                req = ConsumerAuthorizationCheck(
                    resource_id="foo",
                    action="read",
                )
                # Act
                perform_consumer_scope_authorization_check(self.policy, scopes, req)

        with self.subTest("multiple scopes with one matching"):
            # Arrange
            scopes = ["nonexistent:scope", self.read_scope.scope, "another:scope"]
            req = ConsumerAuthorizationCheck(
                resource_id="foo",
                action="read",
            )
            # Act
            perform_consumer_scope_authorization_check(self.policy, scopes, req)
            # Assertion is that no exception is raised


class TestRbacOrgPolicyValidations(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_project_policy = Policy(
            resources=[
                PolicyResource(
                    resource_id="document",
                    description="Documents",
                    actions=["read", "write", "delete"],
                ),
                PolicyResource(
                    resource_id="program",
                    description="An executable program",
                    actions=["read", "write", "execute"],
                ),
            ],
            roles=[
                PolicyRole(
                    role_id="stytch_member",
                    description="member",
                    permissions=[
                        PolicyRolePermission(
                            resource_id="document",
                            actions=["read", "write"],
                        ),
                        PolicyRolePermission(
                            resource_id="program",
                            actions=["read"],
                        ),
                    ],
                ),
                PolicyRole(
                    role_id="stytch_editor",
                    description="editor",
                    permissions=[
                        PolicyRolePermission(
                            resource_id="document",
                            actions=["read", "write"],
                        ),
                        PolicyRolePermission(
                            resource_id="program",
                            actions=["read", "execute"],
                        ),
                    ],
                ),
                PolicyRole(
                    role_id="stytch_admin",
                    description="admin",
                    permissions=[
                        PolicyRolePermission(
                            resource_id="document",
                            actions=["read", "write", "delete"],
                        ),
                        PolicyRolePermission(
                            resource_id="program",
                            actions=["*"],
                        ),
                    ],
                ),
            ],
            scopes=[],  # No scopes in Org RBAC policies.
        )

    def test_validate_org_rbac_policies(self) -> None:
        with self.subTest("exception if a role is already defined in Project policy"):
            with self.assertRaisesRegex(Exception, r"Role \w+ already defined in Project RBAC policy"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="stytch_editor",
                                description="",
                                permissions=[
                                    PolicyRolePermission(actions=["*"], resource_id="resource")
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("exception if a role is already defined in Org policy"):
            with self.assertRaisesRegex(Exception, r"Duplicate role \w+ in Organization RBAC policy"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="researcher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=["*"])
                                ],
                            ),
                            PolicyRole(
                                role_id="researcher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=["*"])
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("exception if a role uses an undefined resource"):
            with self.assertRaisesRegex(Exception, r"Resource \w+ not defined in Project RBAC policy"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="researcher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="computer", actions=["boot"])
                                ],
                            ),
                            PolicyRole(
                                role_id="teacher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=["*"])
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("exception if a role does not define actions for a permission"):
            with self.assertRaisesRegex(Exception, r"No actions defined for role \w+, resource \w+"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="teacher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=[])
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("exception if a role uses a wildcard with other actions"):
            with self.assertRaisesRegex(Exception,
                                        r"Wildcard actions must be the only action defined for a role and resource"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="teacher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=["*", "read"])
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("exception an action is left empty"):
            with self.assertRaisesRegex(Exception, r"Empty action on resource \w+ is not permitted"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="teacher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=["", "read"])
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("exception if an unknown action is defined on a resource"):
            with self.assertRaisesRegex(Exception, r"Unknown action \w+ defined on resource \w+"):
                Organizations.validate_org_policy(
                    project_policy=self.sample_project_policy,
                    org_policy=OrgPolicy(
                        roles=[
                            PolicyRole(
                                role_id="teacher",
                                description="",
                                permissions=[
                                    PolicyRolePermission(resource_id="document", actions=["read", "shred"])
                                ],
                            )
                        ]
                    ),
                )

        with self.subTest("success with a valid Org policy"):
            # Assert no exception is raised.
            Organizations.validate_org_policy(
                project_policy=self.sample_project_policy,
                org_policy=OrgPolicy(
                    roles=[
                        PolicyRole(
                            role_id="teacher",
                            description="High school teacher",
                            permissions=[
                                PolicyRolePermission(resource_id="document", actions=["*"])
                            ],
                        ),
                        PolicyRole(
                            role_id="student",
                            description="High school student",
                            permissions=[
                                PolicyRolePermission(resource_id="document", actions=["read"])
                            ],
                        ),
                        PolicyRole(
                            role_id="sys_admin",
                            description="Network administrator",
                            permissions=[
                                PolicyRolePermission(resource_id="program", actions=["read", "write", "execute"])
                            ],
                        )
                    ]
                ),
            )
