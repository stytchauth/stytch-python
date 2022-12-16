#!/usr/bin/env python3

import unittest
import unittest.mock

from stytch.client import Client


class TestClient(unittest.TestCase):
    # Logically private methods
    def test__env_url(self) -> None:
        # Arrange
        env_with_expected = [
            ("test", "https://test.stytch.com/v1/"),
            ("live", "https://api.stytch.com/v1/"),
            ("something_else", "something_else"),
        ]

        for env, expected in env_with_expected:
            # Act
            with unittest.mock.patch("stytch.client.warnings", autospec=True):
                actual = Client._env_url(env)
            # Assert
            self.assertEqual(expected, actual)
