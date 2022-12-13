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
TEST_OTP_METHOD_ID = "phone-number-test-d5a3b680-e8a3-40c0-b815-ab79986666d0"
TEST_OTP_CODE = "123456"
TEST_EMAIL = "sandbox@stytch.com"
TEST_PHONE_NUMBER = "+10000000000"


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
        with self.subTest("authenticate_start"):
            self.assert_ok(
                api.authenticate_start(
                    crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                    crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                    user_id=TEST_USER_ID,
                )
            )
        with self.subTest("authenticate"):
            self.assert_ok(
                api.authenticate(
                    crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                    crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                    signature=TEST_SIGNATURE,
                )
            )

    def test_magic_links(self) -> None:
        api = self.client.magic_links
        with self.subTest("create"):
            self.assert_ok(api.create(user_id=TEST_USER_ID))
        with self.subTest("authenticate"):
            self.assert_ok(api.authenticate(token=TEST_TOKEN))

    def test_oauth(self) -> None:
        api = self.client.oauth
        with self.subTest("authenticate"):
            self.assert_ok(api.authenticate(token=TEST_TOKEN))

    def test_otp(self) -> None:
        api = self.client.otps
        with self.subTest("authenticate"):
            self.assert_ok(
                api.authenticate(method_id=TEST_OTP_METHOD_ID, code=TEST_OTP_CODE)
            )

    def test_otp_email(self) -> None:
        api = self.client.otps.email
        with self.subTest("send"):
            self.assert_ok(api.send(email=TEST_EMAIL))
        with self.subTest("login_or_create"):
            self.assert_ok(api.login_or_create(email=TEST_EMAIL))

    def test_otp_sms(self) -> None:
        api = self.client.otps.sms
        with self.subTest("send"):
            self.assert_ok(api.send(phone_number=TEST_PHONE_NUMBER))
        with self.subTest("login_or_create"):
            self.assert_ok(api.login_or_create(phone_number=TEST_PHONE_NUMBER))

    def test_otp_whatsapp(self) -> None:
        api = self.client.otps.whatsapp
        with self.subTest("send"):
            self.assert_ok(api.send(phone_number=TEST_PHONE_NUMBER))
        with self.subTest("login_or_create"):
            self.assert_ok(api.login_or_create(phone_number=TEST_PHONE_NUMBER))

    def test_passwords(self) -> None:
        api = self.client.passwords
        with self.subTest("create"):
            pass
        with self.subTest("authenticate"):
            pass
        with self.subTest("strength_check"):
            pass
        with self.subTest("migrate"):
            pass
        pass

    def test_passwords_email(self) -> None:
        api = self.client.passwords.email
        with self.subTest("reset_start"):
            pass
        with self.subTest("reset"):
            pass

    def test_passwords_existing_password(self) -> None:
        api = self.client.passwords.existing_password
        with self.subTest("reset"):
            pass

    def test_passwords_session(self) -> None:
        api = self.client.passwords.session
        with self.subTest("reset"):
            pass

    def test_sessions(self) -> None:
        api = self.client.sessions
        with self.subTest("get"):
            pass
        with self.subTest("authenticate"):
            pass
        with self.subTest("revoke"):
            pass
        with self.subTest("jwks"):
            pass

    def test_totps(self) -> None:
        api = self.client.totps
        with self.subTest("create"):
            pass
        with self.subTest("authenticate"):
            pass
        with self.subTest("recovery_codes"):
            pass
        with self.subTest("recover"):
            pass

    def test_users(self) -> None:
        api = self.client.users
        with self.subTest("create"):
            pass
        with self.subTest("get"):
            pass
        with self.subTest("get_pending"):
            pass
        with self.subTest("search"):
            pass
        with self.subTest("delete"):
            pass
        with self.subTest("update"):
            pass
        with self.subTest("delete_email"):
            pass
        with self.subTest("delete_phone_number"):
            pass
        with self.subTest("delete_webauthn_registration"):
            pass
        with self.subTest("delete_totp"):
            pass
        with self.subTest("delete_crypto_wallet"):
            pass
        with self.subTest("delete_password"):
            pass
        with self.subTest("delete_biometric_registration"):
            pass
        with self.subTest("delete_oauth_user_registration"):
            pass

    def test_webauthn(self) -> None:
        api = self.client.webauthn
        with self.subTest("register_start"):
            pass
        with self.subTest("register"):
            pass
        with self.subTest("authenticate_start"):
            pass
        with self.subTest("authenticate"):
            pass
