#!/usr/bin/env python3

import unittest
from typing import List
from unittest.mock import AsyncMock, Mock, patch

from stytch.consumer.models.rbac import (
    Policy,
    PolicyRole,
    PolicyRolePermission,
    PolicyScope,
    PolicyScopePermission,
)
from stytch.consumer.models.sessions import (
    AuthorizationCheck as ConsumerAuthorizationCheck,
)
from stytch.shared.rbac_local import (
    RBACConsumerPermissionError,
    perform_consumer_scope_authorization_check,
)


class TestConsumerIDP(unittest.TestCase):
    def setUp(self) -> None:
        # Set up test policy with roles and scopes
        self.admin_role = PolicyRole(
            role_id="admin",
            description="Admin role",
            permissions=[
                PolicyRolePermission(actions=["*"], resource_id="foo"),
                PolicyRolePermission(actions=["*"], resource_id="bar"),
            ],
        )
        self.writer_role = PolicyRole(
            role_id="writer",
            description="Writer role",
            permissions=[
                PolicyRolePermission(actions=["write", "read"], resource_id="foo"),
                PolicyRolePermission(actions=["write", "read"], resource_id="bar"),
            ],
        )
        self.reader_role = PolicyRole(
            role_id="reader",
            description="Reader role",
            permissions=[
                PolicyRolePermission(actions=["read"], resource_id="foo"),
                PolicyRolePermission(actions=["read"], resource_id="bar"),
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
            roles=[self.admin_role, self.writer_role, self.reader_role],
            scopes=[self.read_scope, self.write_scope, self.wildcard_scope],
        )

    def test_perform_consumer_scope_authorization_check_success(self) -> None:
        """Test successful authorization with matching scope and action."""
        # Arrange
        scopes = [self.write_scope.scope]
        req = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="write",
        )

        # Act & Assert - should not raise an exception
        perform_consumer_scope_authorization_check(self.policy, scopes, req)

    def test_perform_consumer_scope_authorization_check_wildcard_success(self) -> None:
        """Test successful authorization with wildcard scope."""
        # Arrange
        scopes = [self.wildcard_scope.scope]
        req = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="delete",  # Action not explicitly defined but covered by wildcard
        )

        # Act & Assert - should not raise an exception
        perform_consumer_scope_authorization_check(self.policy, scopes, req)

    def test_perform_consumer_scope_authorization_check_wrong_resource(self) -> None:
        """Test authorization failure when resource doesn't match."""
        # Arrange
        scopes = [self.write_scope.scope]
        req = ConsumerAuthorizationCheck(
            resource_id="baz",  # Resource not in scope
            action="write",
        )

        # Act & Assert
        with self.assertRaises(RBACConsumerPermissionError):
            perform_consumer_scope_authorization_check(self.policy, scopes, req)

    def test_perform_consumer_scope_authorization_check_wrong_action(self) -> None:
        """Test authorization failure when action doesn't match."""
        # Arrange
        scopes = [self.read_scope.scope]
        req = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="write",  # Action not in read scope
        )

        # Act & Assert
        with self.assertRaises(RBACConsumerPermissionError):
            perform_consumer_scope_authorization_check(self.policy, scopes, req)

    def test_perform_consumer_scope_authorization_check_no_matching_scope(self) -> None:
        """Test authorization failure when no scope matches."""
        # Arrange
        scopes = ["nonexistent:scope"]
        req = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="read",
        )

        # Act & Assert
        with self.assertRaises(RBACConsumerPermissionError):
            perform_consumer_scope_authorization_check(self.policy, scopes, req)

    def test_perform_consumer_scope_authorization_check_empty_scopes(self) -> None:
        """Test authorization failure with empty scopes list."""
        # Arrange
        scopes: List[str] = []
        req = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="read",
        )

        # Act & Assert
        with self.assertRaises(RBACConsumerPermissionError):
            perform_consumer_scope_authorization_check(self.policy, scopes, req)

    def test_perform_consumer_scope_authorization_check_multiple_scopes(self) -> None:
        """Test successful authorization with multiple scopes where one matches."""
        # Arrange
        scopes = ["nonexistent:scope", self.read_scope.scope, "another:scope"]
        req = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="read",
        )

        # Act & Assert - should not raise an exception
        perform_consumer_scope_authorization_check(self.policy, scopes, req)

    @patch(
        "stytch.consumer.api.idp.rbac_local.perform_consumer_scope_authorization_check"
    )
    def test_introspect_token_network_with_authorization_check(
        self, mock_auth_check
    ) -> None:
        """Test that introspect_token_network calls authorization check when provided."""
        # Arrange
        mock_api_base = Mock()
        mock_sync_client = Mock()
        mock_async_client = Mock()
        mock_jwks_client = Mock()
        mock_policy_cache = Mock()
        mock_policy_cache.get.return_value = self.policy

        # Mock the response with proper structure
        mock_response = Mock()
        mock_response.response.status_code = 200
        mock_response.json = {
            "status_code": 200,
            "request_id": "test_request_id",
            "active": True,
            "sub": "user123",
            "scope": "write:documents",
            "aud": ["test_audience"],  # aud should be a list
            "exp": 1234567890,
            "iat": 1234567890,
            "iss": "test_issuer",
            "nbf": 1234567890,
            "token_type": "access_token",
        }
        mock_sync_client.post_form.return_value = mock_response

        # Create IDP instance with policy cache
        from stytch.consumer.api.idp import IDP

        idp = IDP(
            api_base=mock_api_base,
            sync_client=mock_sync_client,
            async_client=mock_async_client,
            jwks_client=mock_jwks_client,
            project_id="test_project",
            policy_cache=mock_policy_cache,
        )

        auth_check = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="write",
        )

        # Act
        result = idp.introspect_token_network(
            token="test_token",
            client_id="test_client",
            authorization_check=auth_check,
        )

        # Assert
        mock_auth_check.assert_called_once_with(
            policy=self.policy,
            token_scopes=["write:documents"],
            authorization_check=auth_check,
        )
        self.assertIsNotNone(result)

    @patch(
        "stytch.consumer.api.idp.rbac_local.perform_consumer_scope_authorization_check"
    )
    def test_introspect_token_network_async_with_authorization_check(
        self, mock_auth_check
    ) -> None:
        """Test that introspect_token_network_async calls authorization check when provided."""
        # Arrange
        mock_api_base = Mock()
        mock_sync_client = Mock()
        mock_async_client = AsyncMock()  # Use AsyncMock for async methods
        mock_jwks_client = Mock()
        mock_policy_cache = Mock()
        mock_policy_cache.get.return_value = self.policy

        # Mock the response with proper structure
        mock_response = Mock()
        mock_response.response.status = 200
        mock_response.json = {
            "status_code": 200,
            "request_id": "test_request_id",
            "active": True,
            "sub": "user123",
            "scope": "write:documents",
            "aud": ["test_audience"],  # aud should be a list
            "exp": 1234567890,
            "iat": 1234567890,
            "iss": "test_issuer",
            "nbf": 1234567890,
            "token_type": "access_token",
        }
        mock_async_client.post_form.return_value = mock_response

        # Create IDP instance with policy cache
        from stytch.consumer.api.idp import IDP

        idp = IDP(
            api_base=mock_api_base,
            sync_client=mock_sync_client,
            async_client=mock_async_client,
            jwks_client=mock_jwks_client,
            project_id="test_project",
            policy_cache=mock_policy_cache,
        )

        auth_check = ConsumerAuthorizationCheck(
            resource_id="foo",
            action="write",
        )

        # Act
        import asyncio

        result = asyncio.run(
            idp.introspect_token_network_async(
                token="test_token",
                client_id="test_client",
                authorization_check=auth_check,
            )
        )

        # Assert
        mock_auth_check.assert_called_once_with(
            policy=self.policy,
            token_scopes=["write:documents"],
            authorization_check=auth_check,
        )
        self.assertIsNotNone(result)

    def test_introspect_token_network_without_authorization_check(self) -> None:
        """Test that introspect_token_network works without authorization check."""
        # Arrange
        mock_api_base = Mock()
        mock_sync_client = Mock()
        mock_async_client = Mock()
        mock_jwks_client = Mock()
        mock_policy_cache = Mock()

        # Mock the response with proper structure
        mock_response = Mock()
        mock_response.response.status_code = 200
        mock_response.json = {
            "status_code": 200,
            "request_id": "test_request_id",
            "active": True,
            "sub": "user123",
            "scope": "write:documents",
            "aud": ["test_audience"],  # aud should be a list
            "exp": 1234567890,
            "iat": 1234567890,
            "iss": "test_issuer",
            "nbf": 1234567890,
            "token_type": "access_token",
        }
        mock_sync_client.post_form.return_value = mock_response

        # Create IDP instance
        from stytch.consumer.api.idp import IDP

        idp = IDP(
            api_base=mock_api_base,
            sync_client=mock_sync_client,
            async_client=mock_async_client,
            jwks_client=mock_jwks_client,
            project_id="test_project",
            policy_cache=mock_policy_cache,
        )

        # Act
        result = idp.introspect_token_network(
            token="test_token",
            client_id="test_client",
        )

        # Assert
        self.assertIsNotNone(result)
        # Lint requires us to be sure this isn't None, in a way that tests doesn't check.
        if result is not None:
            self.assertEqual(result.subject, "user123")
            self.assertEqual(result.scope, "write:documents")

    def test_introspect_token_network_inactive_token(self) -> None:
        """Test that introspect_token_network returns None for inactive tokens."""
        # Arrange
        mock_api_base = Mock()
        mock_sync_client = Mock()
        mock_async_client = Mock()
        mock_jwks_client = Mock()
        mock_policy_cache = Mock()

        # Mock the response with inactive token and proper structure
        mock_response = Mock()
        mock_response.response.status_code = 200
        mock_response.json = {
            "status_code": 200,
            "request_id": "test_request_id",
            "active": False,
            "sub": "user123",
            "scope": "write:documents",
        }
        mock_sync_client.post_form.return_value = mock_response

        # Create IDP instance
        from stytch.consumer.api.idp import IDP

        idp = IDP(
            api_base=mock_api_base,
            sync_client=mock_sync_client,
            async_client=mock_async_client,
            jwks_client=mock_jwks_client,
            project_id="test_project",
            policy_cache=mock_policy_cache,
        )

        # Act
        result = idp.introspect_token_network(
            token="test_token",
            client_id="test_client",
        )

        # Assert
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
