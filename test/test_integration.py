#!/usr/bin/env python3

import os
import unittest

import pydantic

from stytch.client import Client

RUN_INTEGRATION_TESTS_ENV_KEY = "STYTCH_PYTHON_RUN_INTEGRATION_TESTS"
PROJECT_ID_ENV_KEY = "STYTCH_PROJECT_ID"
SECRET_ENV_KEY = "STYTCH_SECRET"

# Valid values against the test API
TEST_CRYPTO_WALLET_TYPE = "ethereum"
TEST_CRYPTO_WALLET_ADDRESS = "0x6df2dB4Fb3DA35d241901Bd53367770BF03123f1"
TEST_SIGNATURE = "0x0c4f82edc3c818b6beff4b89e0682994e5878074609903cecdfb"
TEST_USER_ID = "user-test-16d9ba61-97a1-4ba4-9720-b03761dc50c6"
TEST_TOKEN = "SeiGwdj5lKkrEVgcEY3QNJXt6srxS3IK2Nwkar6mXD4="


class IntegrationTest(unittest.TestCase):
    def _skip_for_env_var(self, var: str) -> None:
        self.skipTest(f"{var} env variable not set, skipping integration tests")

    def assert_status_code(
        self, status_code: int, response: pydantic.BaseModel
    ) -> None:
        actual_status_code = getattr(response, "status_code")
        self.assertIsNotNone(actual_status_code)
        self.assertEqual(status_code, actual_status_code)

    def assert_ok(self, response: pydantic.BaseModel) -> None:
        self.assert_status_code(200, response)

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

    def test_crypto_wallets(self) -> None:
        api = self.client.crypto_wallets
        self.assert_ok(
            api.authenticate_start(
                crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                user_id=TEST_USER_ID,
            )
        )
        self.assert_ok(
            api.authenticate(
                crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                signature=TEST_SIGNATURE,
            )
        )

    def test_magic_links(self) -> None:
        api = self.client.magic_links
        self.assert_ok(api.create(user_id=TEST_USER_ID))
        self.assert_ok(api.authenticate(token=TEST_TOKEN))

    def test_oauth(self) -> None:
        pass

    def test_otp(self) -> None:
        pass

    def test_passwords(self) -> None:
        pass

    def test_sessions(self) -> None:
        pass

    def test_totps(self) -> None:
        pass

    def test_users(self) -> None:
        pass

    def test_webauthn(self) -> None:
        pass
