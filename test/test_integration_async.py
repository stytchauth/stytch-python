#!/usr/bin/env python3

import sys
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

if sys.version_info < (3, 8):
    # When running 3.7, we unfortunately can't test async properly
    IsolatedAsyncioTestCase = unittest.TestCase
else:
    from unittest import IsolatedAsyncioTestCase


class AsyncIntegrationTest(IntegrationTestBase, IsolatedAsyncioTestCase):
    async def test_crypto_wallets_async(self) -> None:
        api = self.client.crypto_wallets

        self.assertTrue(
            (
                await api.authenticate_start_async(
                    crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                    crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                )
            ).is_success
        )
        self.assertTrue(
            (
                await api.authenticate_async(
                    crypto_wallet_type=TEST_CRYPTO_WALLET_TYPE,
                    crypto_wallet_address=TEST_CRYPTO_WALLET_ADDRESS,
                    signature=TEST_CRYPTO_SIGNATURE,
                )
            ).is_success
        )

    async def test_magic_links_async(self) -> None:
        api = self.client.magic_links

        self.assertTrue(
            (await api.authenticate_async(token=TEST_MAGIC_TOKEN)).is_success
        )

        with self.skip_if_stytcherror(
            subtest_name="create_endpoint",
            skip_reason="Not approved for embedded magic links",
            error_message_pattern="requires approval before using",
        ):
            async with self._get_temporary_user_async() as user:
                assert isinstance(user, CreatedTestUser)
                self.assertTrue(
                    (await api.create_async(user_id=user.user_id)).is_success
                )

        with self.skip_if_stytcherror(
            subtest_name="email",
            skip_reason="No invite_redirect_url set up",
            error_message_pattern="There are no .* URLs registered",
        ):
            self.assertTrue(
                (await api.email.invite_async(email=TEST_MAGIC_EMAIL)).is_success
            )
            self.assertTrue(
                (await api.email.revoke_invite_async(email=TEST_MAGIC_EMAIL)).is_success
            )
            self.assertTrue(
                (
                    await api.email.login_or_create_async(email=TEST_MAGIC_EMAIL)
                ).is_success
            )
            self.assertTrue((await api.email.send_async(TEST_MAGIC_EMAIL)).is_success)

    async def test_oauth_async(self) -> None:
        api = self.client.oauth

        self.assertTrue(
            (await api.authenticate_async(token=TEST_OAUTH_TOKEN)).is_success
        )

    async def test_otp_async(self) -> None:
        api = self.client.otps

        with self.subTest("email"):
            self.assertTrue(
                (await api.email.login_or_create_async(email=TEST_OTP_EMAIL)).is_success
            )
            email_send_response = await api.email.send_async(email=TEST_OTP_EMAIL)
            self.assertTrue(email_send_response.is_success)
            self.assertTrue(
                (
                    await api.authenticate_async(
                        method_id=email_send_response.email_id, code=TEST_OTP_CODE
                    )
                ).is_success
            )
        with self.subTest("sms"):
            self.assertTrue(
                (
                    await api.sms.login_or_create_async(
                        phone_number=TEST_OTP_PHONE_NUMBER
                    )
                ).is_success
            )
            sms_send_response = await api.sms.send_async(
                phone_number=TEST_OTP_PHONE_NUMBER
            )
            self.assertTrue(sms_send_response.is_success)
            self.assertTrue(
                (
                    await api.authenticate_async(
                        method_id=sms_send_response.phone_id, code=TEST_OTP_CODE
                    )
                ).is_success
            )
        with self.subTest("whatsapp"):
            self.assertTrue(
                (
                    await api.sms.login_or_create_async(
                        phone_number=TEST_OTP_PHONE_NUMBER
                    )
                ).is_success
            )
            whatsapp_send_response = await api.whatsapp.send_async(
                phone_number=TEST_OTP_PHONE_NUMBER
            )
            self.assertTrue(whatsapp_send_response.is_success)
            self.assertTrue(
                (
                    await api.authenticate_async(
                        method_id=whatsapp_send_response.phone_id, code=TEST_OTP_CODE
                    )
                ).is_success
            )

    async def test_passwords_async(self) -> None:
        api = self.client.passwords

        async with self._get_temporary_user_async(create=False) as user:
            self.assertTrue(
                (await api.strength_check_async(password=user.old_password)).is_success
            )
            create_response = await api.create_async(
                email=user.email, password=user.old_password
            )
            self.assertTrue(create_response.is_success)
            authenticate_response = await api.authenticate_async(
                email=user.email, password=user.old_password
            )
            self.assertTrue(authenticate_response.is_success)
            # Remember to manually delete since we manually created!
            await self.client.users.delete_async(create_response.user_id)

        # Migrate an existing user created via magic link
        async with self._get_temporary_user_async(via_magic_link=True) as user:
            self.assertTrue(
                (
                    await api.migrate_async(
                        email=user.email,
                        hash=TEST_PW_HASH,
                        hash_type=TEST_PW_HASH_TYPE,
                    )
                ).is_success
            )

        with self.skip_if_stytcherror(
            subtest_name="email",
            skip_reason="No login_redirect_url set up",
            error_message_pattern="There are no .* URLs",
        ):
            # Can't test: there's no reset token that can be used for testing the API
            self.skipTest("No reset token to use for testing")
            async with self._get_temporary_user_async() as user:
                reset_start_response = await api.email.reset_start_async(
                    email=user.email
                )
                self.assertTrue(reset_start_response.is_success)
                # TODO: We don't have a sample reset token (see skipTest above)
                self.assertTrue(
                    (
                        await api.email.reset_async(
                            token="", password=user.new_password
                        )
                    ).is_success
                )
        with self.subTest("existing_password"):
            async with self._get_temporary_user_async() as user:
                self.assertTrue(
                    (
                        await api.existing_password.reset_async(
                            email=user.email,
                            existing_password=user.old_password,
                            new_password=user.new_password,
                        )
                    ).is_success
                )
        with self.subTest("session"):
            # Can't test: there's no sesison token that can be used for testing the API
            self.skipTest("No session token to use for testing")
            async with self._get_temporary_user_async() as user:
                # TODO: We don't have a sample session token (see skipTest above)
                self.assertTrue(
                    (
                        await api.session.reset_async(
                            session_token="",
                            password=user.new_password,
                        )
                    ).is_success
                )

    async def test_sessions_async(self) -> None:
        api = self.client.sessions

        async with self._get_temporary_user_async() as user:
            # TODO: With @overload, it should be possible to let
            # the type checker infer this statically. I tried, but
            # it was a bit complicated since it's not a simple type,
            # but actually returning a Generator from a @contextmanager
            assert isinstance(user, CreatedTestUser)
            self.assertTrue((await api.get_async(user_id=user.user_id)).is_success)
            self.assertTrue(
                (
                    await api.authenticate_async(session_token=TEST_SESSION_TOKEN)
                ).is_success
            )
            # Can't test revoke -- it doesn't support the TEST_SESSION_TOKEN
            # self.assertTrue(api.revoke(session_token=TEST_SESSION_TOKEN).is_success)
            self.assertTrue(
                (await api.jwks_async(project_id=self.project_id)).is_success
            )

    async def test_totps_async(self) -> None:
        api = self.client.totps

        self.assertTrue((await api.create_async(user_id=TEST_TOTP_USER_ID)).is_success)
        self.assertTrue(
            (
                await api.authenticate_async(
                    user_id=TEST_TOTP_USER_ID, totp_code=TEST_TOTP_CODE
                )
            ).is_success
        )
        self.assertTrue(
            (await api.recovery_codes_async(user_id=TEST_TOTP_USER_ID)).is_success
        )
        self.assertTrue(
            (
                await api.recover_async(
                    user_id=TEST_TOTP_USER_ID, recovery_code=TEST_TOTP_RECOVERY_CODE
                )
            ).is_success
        )

    async def test_users_async(self) -> None:
        # NOTE: the various `delete_XXX` can't easily be tested (yet)
        # since it would require we first create the user with each of those
        # methods/auth factors present (and possibly authenticated?).
        api = self.client.users

        async with self._get_temporary_user_async(create=False) as user:
            create_resp = await api.create_async(email=user.email)
            self.assertTrue(create_resp.is_success)
            self.assertTrue((await api.get_pending_async()).is_success)
            self.assertTrue((await api.search_async(limit=10)).is_success)
            self.assertTrue(
                (
                    await api.update_async(
                        user_id=create_resp.user_id,
                        name=TEST_USERS_NAME,
                    )
                ).is_success
            )
            self.assertTrue(
                (await api.get_async(user_id=create_resp.user_id)).is_success
            )
            self.assertTrue(
                (await api.delete_async(user_id=create_resp.user_id)).is_success
            )

    async def test_webauthn_async(self) -> None:
        api = self.client.webauthn
        # Can't test: webauthn requires calling browser functions
        # It would probably work if we had some way of using test API
        # sample values (like a sample public_key_credential for testing)
        self.skipTest("webauthn cannot be tested from this client")

        async with self._get_temporary_user_async() as user:
            assert isinstance(user, CreatedTestUser)
            # TODO: No test domain (see skipTest above)
            self.assertTrue(
                (
                    await api.register_start_async(user_id=user.user_id, domain="")
                ).is_success
            )
            # TODO: No test public key credential (see skipTest above)
            self.assertTrue(
                (
                    await api.register_async(
                        user_id=user.user_id,
                        public_key_credential="",
                    )
                ).is_success
            )
            # TODO: No test domain (see skipTest above)
            self.assertTrue(
                (
                    await api.authenticate_start_async(user_id=user.user_id, domain="")
                ).is_success
            )
            # TODO: No test public key credential (see skipTest above)
            self.assertTrue(
                (await api.authenticate_async(public_key_credential="")).is_success
            )
