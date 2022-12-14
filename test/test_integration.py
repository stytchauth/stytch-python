#!/usr/bin/env python3

import os
import random
import string
import unittest
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generator, Union

from stytch.client import Client
from stytch.core.models import Name

RUN_INTEGRATION_TESTS_ENV_KEY = "STYTCH_PYTHON_RUN_INTEGRATION_TESTS"
PROJECT_ID_ENV_KEY = "STYTCH_PROJECT_ID"
SECRET_ENV_KEY = "STYTCH_SECRET"


@dataclass
class TestUser:
    username: str
    email: str
    old_password: str
    new_password: str


@dataclass
class CreatedTestUser(TestUser):
    user_id: str


class IntegrationTest(unittest.TestCase):
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

        self.project_id: str = project_id
        self.secret: str = secret
        self.client = Client(self.project_id, self.secret, environment="test")

    @contextmanager
    def _get_temporary_user(
        self, create: bool = True, via_magic_link: bool = False
    ) -> Generator[Union[TestUser, CreatedTestUser], None, None]:
        username = "".join(random.choice(string.ascii_letters) for _ in range(20))
        email = f"{username}@example.com"
        old_password = "".join(random.choice(string.printable) for _ in range(24))
        new_password = "".join(random.choice(string.printable) for _ in range(24))

        if create:
            if via_magic_link:
                resp = self.client.users.create(email=email)
            else:
                resp = self.client.passwords.create(email=email, password=old_password)

            user_id = resp.user_id
            yield CreatedTestUser(
                username=username,
                email=email,
                old_password=old_password,
                new_password=new_password,
                user_id=user_id,
            )
            self.client.users.delete(user_id=user_id)
        else:
            yield TestUser(
                username=username,
                email=email,
                old_password=old_password,
                new_password=new_password,
            )

    def _skip_for_env_var(self, var: str) -> None:
        self.skipTest(f"{var} env variable not set, skipping integration tests")

    def test_crypto_wallets(self) -> None:
        api = self.client.crypto_wallets
        TEST_WALLET_TYPE = "ethereum"
        TEST_WALLET_ADDRESS = "0x6df2dB4Fb3DA35d241901Bd53367770BF03123f1"
        TEST_SIGNATURE = "0x0c4f82edc3c818b6beff4b89e0682994e5878074609903cecdfb"

        self.assertTrue(
            api.authenticate_start(
                crypto_wallet_type=TEST_WALLET_TYPE,
                crypto_wallet_address=TEST_WALLET_ADDRESS,
            ).is_success
        )
        self.assertTrue(
            api.authenticate(
                crypto_wallet_type=TEST_WALLET_TYPE,
                crypto_wallet_address=TEST_WALLET_ADDRESS,
                signature=TEST_SIGNATURE,
            ).is_success
        )

    def test_magic_links(self) -> None:
        api = self.client.magic_links

        TEST_EMAIL = "sandbox@stytch.com"
        TEST_TOKEN = "DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94="

        # Can't test create endpoint -- requires approval
        # self.assertTrue(api.create(user_id=user.user_id).is_success)
        self.assertTrue(api.authenticate(token=TEST_TOKEN).is_success)
        with self.subTest("email"):
            # Can't test: there's no way to call the test API without
            # first setting up an invite_redirect_url in the dashboard
            self.skipTest("No invite_redirect_url set up")
            self.assertTrue(api.email.invite(email=TEST_EMAIL).is_success)
            self.assertTrue(api.email.revoke_invite(email=TEST_EMAIL).is_success)
            self.assertTrue(api.email.login_or_create(email=TEST_EMAIL).is_success)
            self.assertTrue(api.email.send(TEST_EMAIL))

    def test_oauth(self) -> None:
        api = self.client.oauth

        TEST_TOKEN = "hdPVZHHX0UoRa7hJTuuPHi1vlddffSnoweRbVFf5-H8g"

        self.assertTrue(api.authenticate(token=TEST_TOKEN).is_success)

    def test_otp(self) -> None:
        api = self.client.otps
        TEST_EMAIL = "sandbox@stytch.com"
        TEST_PHONE_NUMBER = "+10000000000"
        TEST_CODE = "000000"

        with self.subTest("email"):
            self.assertTrue(api.email.login_or_create(email=TEST_EMAIL).is_success)
            send_response = api.email.send(email=TEST_EMAIL)
            self.assertTrue(send_response.is_success)
            self.assertTrue(
                api.authenticate(
                    method_id=send_response.email_id, code=TEST_CODE
                ).is_success
            )
        with self.subTest("sms"):
            self.assertTrue(
                api.sms.login_or_create(phone_number=TEST_PHONE_NUMBER).is_success
            )
            send_response = api.sms.send(phone_number=TEST_PHONE_NUMBER)
            self.assertTrue(send_response.is_success)
            self.assertTrue(
                api.authenticate(
                    method_id=send_response.phone_id, code=TEST_CODE
                ).is_success
            )
        with self.subTest("whatsapp"):
            self.assertTrue(
                api.sms.login_or_create(phone_number=TEST_PHONE_NUMBER).is_success
            )
            send_response = api.whatsapp.send(phone_number=TEST_PHONE_NUMBER)
            self.assertTrue(send_response.is_success)
            self.assertTrue(
                api.authenticate(
                    method_id=send_response.phone_id, code=TEST_CODE
                ).is_success
            )

    def test_passwords(self) -> None:
        api = self.client.passwords
        TEST_HASH = "$2a$12$vefoDBbzuMb/NczV/fc9QemTizkNAZr9EO02pIUHPAAJibcYp0.ne"
        TEST_HASH_TYPE = "bcrypt"

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
                    hash=TEST_HASH,
                    hash_type=TEST_HASH_TYPE,
                ).is_success
            )

        with self.subTest("email"):
            # Can't test: there's no way to call the test API without
            # first setting up a login_redirect_url in the dashboard
            self.skipTest("No login_redirect_url setup")
            # Can't test: there's no reset token that can be used for testing the API
            # NOTE: Yes, there's two skipTests in a row, but this is a reminder
            # that it's due to two separate issues with testing this endpoint
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
                    )
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
                    )
                )

    def test_sessions(self) -> None:
        api = self.client.sessions
        TEST_SESSION_TOKEN = "WJtR5BCy38Szd5AfoDpf0iqFKEt4EE5JhjlWUY7l3FtY"

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
        TEST_USER_ID = "user-test-e3795c81-f849-4167-bfda-e4a6e9c280fd"
        TEST_CODE = "000000"
        TEST_RECOVERY_CODE = "a1b2-c3d4-e5f6"

        self.assertTrue(api.create(user_id=TEST_USER_ID).is_success)
        self.assertTrue(
            api.authenticate(user_id=TEST_USER_ID, totp_code=TEST_CODE).is_success
        )
        self.assertTrue(api.recovery_codes(user_id=TEST_USER_ID).is_success)
        self.assertTrue(
            api.recover(
                user_id=TEST_USER_ID, recovery_code=TEST_RECOVERY_CODE
            ).is_success
        )

    def test_users(self) -> None:
        # NOTE: the various `delete_XXX` can't easily be tested (yet)
        # since it would require we first create the user with each of those
        # methods/auth factors present (and possibly authenticated?).
        api = self.client.users
        TEST_NAME = Name(first_name="Jane", last_name="Doe")

        with self._get_temporary_user(create=False) as user:
            create_resp = api.create(email=user.email)
            self.assertTrue(create_resp.is_success)
            self.assertTrue(api.get_pending().is_success)
            self.assertTrue(api.search().is_success)
            self.assertTrue(
                api.update(
                    user_id=create_resp.user_id,
                    name=TEST_NAME,
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
