#!/usr/bin/env python3

import unittest
from test.constants import (
    TEST_CRYPTO_SIGNATURE,
    TEST_CRYPTO_WALLET_ADDRESS,
    TEST_CRYPTO_WALLET_TYPE,
    TEST_MAGIC_EMAIL,
    TEST_MAGIC_TOKEN,
    TEST_OAUTH_TOKEN,
    TEST_OTP_CODE,
    TEST_OTP_EMAIL,
    TEST_OTP_PHONE_NUMBER,
    TEST_PW_HASH,
    TEST_PW_HASH_TYPE,
    TEST_SESSION_TOKEN,
    TEST_TOTP_CODE,
    TEST_TOTP_RECOVERY_CODE,
    TEST_TOTP_USER_ID,
    TEST_USERS_NAME,
)
from test.integration_base import CreatedTestUser, IntegrationTestBase


class SyncIntegrationTest(IntegrationTestBase, unittest.TestCase):
    def test_crypto_wallets(self) -> None:
        api = self.client.crypto_wallets

        self.assertTrue(
            api.authenticate_start(
                crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
            ).is_success
        )
        self.assertTrue(
            api.authenticate(
                crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                signature=TEST_CRYPTO_SIGNATURE,
            ).is_success
        )

    def test_magic_links(self) -> None:
        api = self.client.magic_links

        self.assertTrue(api.authenticate(token=TEST_MAGIC_TOKEN).is_success)

        with self.skip_if_stytcherror(
            subtest_name="create_endpoint",
            skip_reason="Not approved for embedded magic links",
            error_message_pattern="requires approval before using",
        ):
            with self._get_temporary_user() as user:
                assert isinstance(user, CreatedTestUser)
                self.assertTrue(api.create(user_id=user.user_id).is_success)

        with self.skip_if_stytcherror(
            subtest_name="email",
            skip_reason="No invite_redirect_url set up",
            error_message_pattern="There are no .* URLs",
        ):
            self.assertTrue(api.email.invite(email=TEST_MAGIC_EMAIL).is_success)
            self.assertTrue(api.email.revoke_invite(email=TEST_MAGIC_EMAIL).is_success)
            self.assertTrue(
                api.email.login_or_create(email=TEST_MAGIC_EMAIL).is_success
            )
            self.assertTrue(api.email.send(TEST_MAGIC_EMAIL).is_success)

    def test_oauth(self) -> None:
        api = self.client.oauth

        self.assertTrue(api.authenticate(token=TEST_OAUTH_TOKEN).is_success)

    def test_otp(self) -> None:
        api = self.client.otps

        with self.subTest("email"):
            self.assertTrue(api.email.login_or_create(email=TEST_OTP_EMAIL).is_success)
            email_send_response = api.email.send(email=TEST_OTP_EMAIL)
            self.assertTrue(email_send_response.is_success)
            self.assertTrue(
                api.authenticate(
                    method_id=email_send_response.email_id, code=TEST_OTP_CODE
                ).is_success
            )
        with self.subTest("sms"):
            self.assertTrue(
                api.sms.login_or_create(phone_number=TEST_OTP_PHONE_NUMBER).is_success
            )
            sms_send_response = api.sms.send(phone_number=TEST_OTP_PHONE_NUMBER)
            self.assertTrue(sms_send_response.is_success)
            self.assertTrue(
                api.authenticate(
                    method_id=sms_send_response.phone_id, code=TEST_OTP_CODE
                ).is_success
            )
        with self.subTest("whatsapp"):
            self.assertTrue(
                api.sms.login_or_create(phone_number=TEST_OTP_PHONE_NUMBER).is_success
            )
            whatsapp_send_response = api.whatsapp.send(
                phone_number=TEST_OTP_PHONE_NUMBER
            )
            self.assertTrue(whatsapp_send_response.is_success)
            self.assertTrue(
                api.authenticate(
                    method_id=whatsapp_send_response.phone_id, code=TEST_OTP_CODE
                ).is_success
            )

    def test_passwords(self) -> None:
        api = self.client.passwords

        with self._get_temporary_user(create=False) as user:
            self.assertTrue(api.strength_check(password=user.old_password).is_success)
            create_response = api.create(email=user.email, password=user.old_password)
            self.assertTrue(create_response.is_success)
            authenticate_response = api.authenticate(
                email=user.email, password=user.old_password
            )
            self.assertTrue(authenticate_response.is_success)
            # Remember to manually delete since we manually created!
            self.client.users.delete(create_response.user_id)

        # Migrate an existing user created via magic link
        with self._get_temporary_user(via_magic_link=True) as user:
            self.assertTrue(
                api.migrate(
                    email=user.email,
                    hash=TEST_PW_HASH,
                    hash_type=TEST_PW_HASH_TYPE,
                ).is_success
            )

        with self.skip_if_stytcherror(
            subtest_name="email",
            skip_reason="No login_redirect_url set up",
            error_message_pattern="There are no .* URLs",
        ):
            # Can't test: there's no reset token that can be used for testing the API
            self.skipTest("No reset token to use for testing")
            with self._get_temporary_user() as user:
                reset_start_response = api.email.reset_start(email=user.email)
                self.assertTrue(reset_start_response.is_success)
                # TODO: We don't have a sample reset token (see skipTest above)
                self.assertTrue(
                    api.email.reset(token="", password=user.new_password).is_success
                )
        with self.subTest("existing_password"):
            with self._get_temporary_user() as user:
                self.assertTrue(
                    api.existing_password.reset(
                        email=user.email,
                        existing_password=user.old_password,
                        new_password=user.new_password,
                    ).is_success
                )
        with self.subTest("session"):
            # Can't test: there's no sesison token that can be used for testing the API
            self.skipTest("No session token to use for testing")
            with self._get_temporary_user() as user:
                # TODO: We don't have a sample session token (see skipTest above)
                self.assertTrue(
                    api.session.reset(
                        session_token="",
                        password=user.new_password,
                    ).is_success
                )

    def test_sessions(self) -> None:
        api = self.client.sessions

        with self._get_temporary_user() as user:
            # TODO: With @overload, it should be possible to let
            # the type checker infer this statically. I tried, but
            # it was a bit complicated since it's not a simple type,
            # but actually returning a Generator from a @contextmanager
            assert isinstance(user, CreatedTestUser)
            self.assertTrue(api.get(user_id=user.user_id).is_success)
            self.assertTrue(
                api.authenticate(session_token=TEST_SESSION_TOKEN).is_success
            )
            # Can't test revoke -- it doesn't support the TEST_SESSION_TOKEN
            # self.assertTrue(api.revoke(session_token=TEST_SESSION_TOKEN).is_success)
            self.assertTrue(api.jwks(project_id=self.project_id).is_success)

    def test_totps(self) -> None:
        api = self.client.totps

        self.assertTrue(api.create(user_id=TEST_TOTP_USER_ID).is_success)
        self.assertTrue(
            api.authenticate(
                user_id=TEST_TOTP_USER_ID, totp_code=TEST_TOTP_CODE
            ).is_success
        )
        self.assertTrue(api.recovery_codes(user_id=TEST_TOTP_USER_ID).is_success)
        self.assertTrue(
            api.recover(
                user_id=TEST_TOTP_USER_ID, recovery_code=TEST_TOTP_RECOVERY_CODE
            ).is_success
        )

    def test_users(self) -> None:
        # NOTE: the various `delete_XXX` can't easily be tested (yet)
        # since it would require we first create the user with each of those
        # methods/auth factors present (and possibly authenticated?).
        api = self.client.users

        with self._get_temporary_user(create=False) as user:
            create_resp = api.create(email=user.email)
            self.assertTrue(create_resp.is_success)
            self.assertTrue(api.get_pending().is_success)
            self.assertTrue(api.search(limit=10).is_success)
            self.assertTrue(
                api.update(
                    user_id=create_resp.user_id,
                    name=TEST_USERS_NAME,
                ).is_success
            )
            self.assertTrue(api.get(user_id=create_resp.user_id).is_success)
            self.assertTrue(api.delete(user_id=create_resp.user_id).is_success)

    def test_webauthn(self) -> None:
        api = self.client.webauthn
        # Can't test: webauthn requires calling browser functions
        # It would probably work if we had some way of using test API
        # sample values (like a sample public_key_credential for testing)
        self.skipTest("webauthn cannot be tested from this client")

        with self._get_temporary_user() as user:
            assert isinstance(user, CreatedTestUser)
            # TODO: No test domain (see skipTest above)
            self.assertTrue(
                api.register_start(user_id=user.user_id, domain="").is_success
            )
            # TODO: No test public key credential (see skipTest above)
            self.assertTrue(
                api.register(
                    user_id=user.user_id,
                    public_key_credential="",
                ).is_success
            )
            # TODO: No test domain (see skipTest above)
            self.assertTrue(
                api.authenticate_start(user_id=user.user_id, domain="").is_success
            )
            # TODO: No test public key credential (see skipTest above)
            self.assertTrue(api.authenticate(public_key_credential="").is_success)


if __name__ == "__main__":
    unittest.main()
