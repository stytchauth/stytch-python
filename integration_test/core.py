#!/usr/bin/env python3

import os
import unittest

from stytch.client import Client

RUN_INTEGRATION_TESTS_ENV_KEY = "STYTCH_PYTHON_RUN_INTEGRATION_TESTS"
PROJECT_ID_ENV_KEY = "STYTCH_PROJECT_ID"
SECRET_ENV_KEY = "STYTCH_SECRET"


class IntegrationTest(unittest.TestCase):
    def _skip_for_env_var(self, var: str) -> None:
        self.skipTest(f"{var} env variable not set, skipping integration tests")

    def setUp(self) -> None:
        run_integration_tests = int(os.getenv(RUN_INTEGRATION_TESTS_ENV_KEY, "0"))
        project_id = os.getenv(PROJECT_ID_ENV_KEY)
        secret = os.getenv(SECRET_ENV_KEY)

        if run_integration_tests != 1:
            self._skip_for_env_var(RUN_INTEGRATION_TESTS_ENV_KEY)
            return
        if project_id is None:
            self._skip_for_env_var(PROJECT_ID_ENV_KEY)
            return
        if secret is None:
            self._skip_for_env_var(SECRET_ENV_KEY)
            return

        self.client = Client(project_id, secret, "test")
