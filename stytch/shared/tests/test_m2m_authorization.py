import unittest

from stytch.shared.m2m_authorization import (
    AuthorizationCheckParams,
    perform_authorization_check,
)


class TestM2MAuthorization(unittest.TestCase):
    def test_perform_authorization_check(self):
        with self.subTest("basic"):
            params = AuthorizationCheckParams(
                has_scopes=["read:users"], required_scopes=["read:users"]
            )
            self.assertTrue(perform_authorization_check(params))

        with self.subTest("multiple required scopes"):
            params = AuthorizationCheckParams(
                has_scopes=["read:users", "write:users", "read:books"],
                required_scopes=["read:users", "read:books"],
            )
            self.assertTrue(perform_authorization_check(params))

        with self.subTest("simple scopes"):
            params = AuthorizationCheckParams(
                has_scopes=["read_users", "write_users"], required_scopes=["read_users"]
            )
            self.assertTrue(perform_authorization_check(params))

        with self.subTest("wildcard resource"):
            params = AuthorizationCheckParams(
                has_scopes=["read:*", "write:*"], required_scopes=["read:users"]
            )
            self.assertTrue(perform_authorization_check(params))

        with self.subTest("missing required scope"):
            params = AuthorizationCheckParams(
                has_scopes=["read:users"], required_scopes=["write:users"]
            )
            self.assertFalse(perform_authorization_check(params))

        with self.subTest("missing required scope with wildcard"):
            params = AuthorizationCheckParams(
                has_scopes=["read:users", "write:*"], required_scopes=["delete:books"]
            )
            self.assertFalse(perform_authorization_check(params))

        with self.subTest("has simple scope and wants specific scope"):
            params = AuthorizationCheckParams(
                has_scopes=["read"], required_scopes=["read:users"]
            )
            self.assertFalse(perform_authorization_check(params))

        with self.subTest("has specific scope and wants simple scope"):
            params = AuthorizationCheckParams(
                has_scopes=["read:users"], required_scopes=["read"]
            )
            self.assertFalse(perform_authorization_check(params))
