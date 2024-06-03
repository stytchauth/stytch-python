import unittest

from stytch.shared.m2m_authorization import (
    perform_authorization_check,
    M2MPermissionError,
)


class TestM2MAuthorization(unittest.TestCase):
    def test_perform_authorization_check(self):
        with self.subTest("basic"):
            has = ["read:users", "write:users"]
            needs = ["read:users"]

            # Assertion is just that no exception is raised
            perform_authorization_check(has, needs)

        with self.subTest("multiple required scopes"):
            has = ["read:users", "write:users", "read:books"]
            needs = ["read:users", "read:books"]

            # Assertion is just that no exception is raised
            perform_authorization_check(has, needs)

        with self.subTest("simple scopes"):
            has = ["read_users", "write_users"]
            needs = ["read_users"]

            # Assertion is just that no exception is raised
            perform_authorization_check(has, needs)

        with self.subTest("wildcard resource"):
            has = ["read:*", "write:*"]
            needs = ["read:users"]

            # Assertion is just that no exception is raised
            perform_authorization_check(has, needs)

        with self.subTest("missing required scope"):
            has = ["read:users"]
            needs = ["write:users"]

            with self.assertRaises(M2MPermissionError):
                perform_authorization_check(has, needs)

        with self.subTest("missing required scope with wildcard"):
            has = ["read:users", "write:*"]
            needs = ["delete:books"]

            with self.assertRaises(M2MPermissionError):
                perform_authorization_check(has, needs)
