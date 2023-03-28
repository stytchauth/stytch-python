# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional, Union

from stytch.api.passwords_email import Email
from stytch.api.passwords_existing_password import ExistingPassword
from stytch.api.passwords_session import Session
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.passwords import (
    AuthenticateResponse,
    CreateResponse,
    MigrateResponse,
    StrengthCheckResponse,
)


class Passwords:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.email = Email(api_base, sync_client, async_client)
        self.existing_password = ExistingPassword(api_base, sync_client, async_client)
        self.session = Session(api_base, sync_client, async_client)

    @property
    def sub_url(self) -> str:
        return "passwords"

    def create(
        self,
        email: str,
        password: str,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-create)

        Create a new user with a password and an authenticated session for the user if requested. If a user with this email already exists in the project, this API will return an error.

        Existing passwordless users who wish to create a password need to go through the reset password flow.

        This endpoint will return an error if the password provided does not meet our strength requirements, which you can check beforehand with the password strength endpoint.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
            "password": password,
        }

        if name is not None:
            payload["name"] = name
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        res = self.sync_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        email: str,
        password: str,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-create)

        Create a new user with a password and an authenticated session for the user if requested. If a user with this email already exists in the project, this API will return an error.

        Existing passwordless users who wish to create a password need to go through the reset password flow.

        This endpoint will return an error if the password provided does not meet our strength requirements, which you can check beforehand with the password strength endpoint.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
            "password": password,
        }

        if name is not None:
            payload["name"] = name
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        res = await self.async_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        email: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-authenticate)

        Authenticate a user with their email address and password. This endpoint verifies that the user has a password currently set, and that the entered password is correct. There are two instances where the endpoint will return a reset_password error even if they enter their previous password:

        - The user’s credentials appeared in the HaveIBeenPwned dataset.

          - We force a password reset to ensure that the user is the legitimate owner of the email address, and not a malicious actor abusing the compromised credentials.

        - A user that has previously authenticated with email/password uses a passwordless authentication method tied to the same email address (e.g. Magic Links, Google OAuth) for the first time. Any subsequent email/password authentication attempt will result in this error.

          - We force a password reset in this instance in order to safely deduplicate the account by email address, without introducing the risk of a pre-hijack account takeover attack. Imagine a bad actor creates many accounts using passwords and the known email addresses of their victims. If a victim comes to the site and logs in for the first time with an email-based passwordless authentication method then both the victim and the bad actor have credentials to access to the same account. To prevent this, any further email/password login attempts first require a password reset which can only be accomplished by someone with access to the underlying email address.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        res = self.sync_client.post(url, json=payload)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        email: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-authenticate)

        Authenticate a user with their email address and password. This endpoint verifies that the user has a password currently set, and that the entered password is correct. There are two instances where the endpoint will return a reset_password error even if they enter their previous password:

        - The user’s credentials appeared in the HaveIBeenPwned dataset.

          - We force a password reset to ensure that the user is the legitimate owner of the email address, and not a malicious actor abusing the compromised credentials.

        - A user that has previously authenticated with email/password uses a passwordless authentication method tied to the same email address (e.g. Magic Links, Google OAuth) for the first time. Any subsequent email/password authentication attempt will result in this error.

          - We force a password reset in this instance in order to safely deduplicate the account by email address, without introducing the risk of a pre-hijack account takeover attack. Imagine a bad actor creates many accounts using passwords and the known email addresses of their victims. If a victim comes to the site and logs in for the first time with an email-based passwordless authentication method then both the victim and the bad actor have credentials to access to the same account. To prevent this, any further email/password login attempts first require a password reset which can only be accomplished by someone with access to the underlying email address.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        res = await self.async_client.post(url, json=payload)
        return AuthenticateResponse.from_json(res.response.status, res.json)

    def strength_check(
        self,
        password: str,
        email: Optional[str] = None,
    ) -> StrengthCheckResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-strength-check)

        This API allows you to check whether or not the user’s provided password is valid, and to provide feedback to the user on how to increase the strength of their password.

        Passwords are considered invalid if either of the following is true:
        [zxcvbn's](https://github.com/dropbox/zxcvbn) strength score is <= 2.
        The password is present in the HaveIBeenPwned dataset.

        This endpoint takes email as an optional argument, and if it is passed it will be factored into zxcvbn’s evaluation of the strength of the password. If you do not pass the email, it is possible that the password will evaluate as valid – but will fail with a `weak_password` error when used in the Create password endpoint.

        Feedback will be present in the response for any password that does not meet the strength requirements, and mirrors that feedback provided by the zxcvbn library. If you would like to run the library directly in the client to further reduce latency you can find the implementation [here](https://github.com/dropbox/zxcvbn).
        """  # noqa

        payload: Dict[str, Any] = {
            "password": password,
        }

        if email is not None:
            payload["email"] = email

        url = self.api_base.route_with_sub_url(self.sub_url, "strength_check")

        res = self.sync_client.post(url, json=payload)
        return StrengthCheckResponse.from_json(res.response.status_code, res.json)

    async def strength_check_async(
        self,
        password: str,
        email: Optional[str] = None,
    ) -> StrengthCheckResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-strength-check)

        This API allows you to check whether or not the user’s provided password is valid, and to provide feedback to the user on how to increase the strength of their password.

        Passwords are considered invalid if either of the following is true:
        [zxcvbn's](https://github.com/dropbox/zxcvbn) strength score is <= 2.
        The password is present in the HaveIBeenPwned dataset.

        This endpoint takes email as an optional argument, and if it is passed it will be factored into zxcvbn’s evaluation of the strength of the password. If you do not pass the email, it is possible that the password will evaluate as valid – but will fail with a `weak_password` error when used in the Create password endpoint.

        Feedback will be present in the response for any password that does not meet the strength requirements, and mirrors that feedback provided by the zxcvbn library. If you would like to run the library directly in the client to further reduce latency you can find the implementation [here](https://github.com/dropbox/zxcvbn).
        """  # noqa

        payload: Dict[str, Any] = {
            "password": password,
        }

        if email is not None:
            payload["email"] = email

        url = self.api_base.route_with_sub_url(self.sub_url, "strength_check")

        res = await self.async_client.post(url, json=payload)
        return StrengthCheckResponse.from_json(res.response.status, res.json)

    def migrate(
        self,
        email: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-migrate)

        Adds a existing password to a user's email that doesn't have a password yet. We support migrating users from passwords stored with bcrypt, scrypt, argon2, MD-5, and SHA-1. This endpoint has a rate limit of 10 requests per second.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
            "hash": hash,
            "hash_type": hash_type,
        }

        if md_5_config is not None:
            payload["md_5_config"] = md_5_config
        if argon_2_config is not None:
            payload["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            payload["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            payload["scrypt_config"] = scrypt_config
        if name is not None:
            payload["name"] = name
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "migrate")

        res = self.sync_client.post(url, json=payload)
        return MigrateResponse.from_json(res.response.status_code, res.json)

    async def migrate_async(
        self,
        email: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        """[Stytch docs](https://stytch.com/docs/api/password-migrate)

        Adds a existing password to a user's email that doesn't have a password yet. We support migrating users from passwords stored with bcrypt, scrypt, argon2, MD-5, and SHA-1. This endpoint has a rate limit of 10 requests per second.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
            "hash": hash,
            "hash_type": hash_type,
        }

        if md_5_config is not None:
            payload["md_5_config"] = md_5_config
        if argon_2_config is not None:
            payload["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            payload["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            payload["scrypt_config"] = scrypt_config
        if name is not None:
            payload["name"] = name
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "migrate")

        res = await self.async_client.post(url, json=payload)
        return MigrateResponse.from_json(res.response.status, res.json)
