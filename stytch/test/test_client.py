#!/usr/bin/env python3

import unittest
import unittest.mock

from stytch.client import Client

TEST_PROJECT_ID = "project-test-11111111-2222-3333-4444-555555555555"
LIVE_PROJECT_ID = "project-live-66666666-7777-8888-9999-000000000000"


class TestClient(unittest.TestCase):
    # Logically private methods
    def test__env_url(self) -> None:
        # Arrange
        env_with_expected = [
            (TEST_PROJECT_ID, "test", "https://test.stytch.com/v1/"),
            (LIVE_PROJECT_ID, "live", "https://api.stytch.com/v1/"),
            (LIVE_PROJECT_ID, "something_else", "something_else"),
            (LIVE_PROJECT_ID, None, "https://api.stytch.com/v1/"),
        ]

        for project_id, env, expected in env_with_expected:
            # Act
            with unittest.mock.patch("stytch.client.warnings", autospec=True):
                actual = Client._env_url(project_id=project_id, env=env)
            # Assert
            self.assertEqual(expected, actual)
