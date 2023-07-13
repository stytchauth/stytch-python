#!/usr/bin/env python3

from stytch.consumer.models.passwords import MigrateRequestHashType
from stytch.consumer.models.users import Name

# Constants for loading creds to call the real API
RUN_INTEGRATION_TESTS_ENV_KEY = "STYTCH_PYTHON_RUN_INTEGRATION_TESTS"
PROJECT_ID_ENV_KEY = "STYTCH_PROJECT_ID"
SECRET_ENV_KEY = "STYTCH_SECRET"

# Crypto wallets test constants
TEST_CRYPTO_WALLET_TYPE = "ethereum"
TEST_CRYPTO_WALLET_ADDRESS = "0x6df2dB4Fb3DA35d241901Bd53367770BF03123f1"
TEST_CRYPTO_SIGNATURE = "0x0c4f82edc3c818b6beff4b89e0682994e5878074609903cecdfb"
# Magic links test constants
TEST_MAGIC_EMAIL = "sandbox@stytch.com"
TEST_MAGIC_TOKEN = "DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94="
# OAuth test constants
TEST_OAUTH_TOKEN = "hdPVZHHX0UoRa7hJTuuPHi1vlddffSnoweRbVFf5-H8g"
# OTP test constants
TEST_OTP_EMAIL = "sandbox@stytch.com"
TEST_OTP_PHONE_NUMBER = "+10000000000"
TEST_OTP_CODE = "000000"
# Passwords test constants
TEST_PW_HASH = "$2a$12$vefoDBbzuMb/NczV/fc9QemTizkNAZr9EO02pIUHPAAJibcYp0.ne"
TEST_PW_HASH_TYPE = MigrateRequestHashType.BCRYPT
# Sessions test constants
TEST_SESSION_TOKEN = "WJtR5BCy38Szd5AfoDpf0iqFKEt4EE5JhjlWUY7l3FtY"
# TOTP test constants
TEST_TOTP_USER_ID = "user-test-e3795c81-f849-4167-bfda-e4a6e9c280fd"
TEST_TOTP_CODE = "000000"
TEST_TOTP_RECOVERY_CODE = "a1b2-c3d4-e5f6"
# Users test constants
TEST_USERS_NAME = Name(first_name="Jane", last_name="Doe")
