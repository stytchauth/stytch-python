#!/usr/bin/env python3

import os
import random
import string
import unittest
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass
from test.constants import (
    PROJECT_ID_ENV_KEY,
    RUN_INTEGRATION_TESTS_ENV_KEY,
    SECRET_ENV_KEY,
)
from typing import AsyncGenerator, Generator, Union

from stytch.client import Client
from stytch.core.models import ResponseBase


@dataclass
class TestUser:
    username: str
    email: str
    old_password: str
    new_password: str


@dataclass
class CreatedTestUser(TestUser):
    user_id: str


class IntegrationTestBase(unittest.TestCase):
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

    def _skip_for_env_var(self, var: str) -> None:
        self.skipTest(f"{var} env variable not set, skipping integration tests")

    def __get_temporary_test_user(self) -> TestUser:
        username = "".join(random.choice(string.ascii_letters) for _ in range(20))
        email = f"{username}@example.com"
        old_password = "".join(random.choice(string.printable) for _ in range(24))
        new_password = "".join(random.choice(string.printable) for _ in range(24))
        return TestUser(
            username=username,
            email=email,
            old_password=old_password,
            new_password=new_password,
        )

    def __get_temporary_created_test_user(
        self, test_user: TestUser, user_id: str
    ) -> CreatedTestUser:
        return CreatedTestUser(
            username=test_user.username,
            email=test_user.email,
            old_password=test_user.old_password,
            new_password=test_user.new_password,
            user_id=user_id,
        )

    @contextmanager
    def _get_temporary_user(
        self, create: bool = True, via_magic_link: bool = False
    ) -> Generator[Union[TestUser, CreatedTestUser], None, None]:
        test_user = self.__get_temporary_test_user()
        if create:
            if via_magic_link:
                users_resp = self.client.users.create(email=test_user.email)
                user_id = users_resp.user_id
            else:
                pw_resp = self.client.passwords.create(
                    email=test_user.email, password=test_user.old_password
                )
                user_id = pw_resp.user_id

            yield self.__get_temporary_created_test_user(test_user, user_id)
            self.client.users.delete(user_id=user_id)
        else:
            yield test_user

    @asynccontextmanager
    async def _get_temporary_user_async(
        self, create: bool = True, via_magic_link: bool = False
    ) -> AsyncGenerator[Union[TestUser, CreatedTestUser], None]:
        test_user = self.__get_temporary_test_user()
        if create:
            if via_magic_link:
                users_resp = await self.client.users.create_async(email=test_user.email)
                user_id = users_resp.user_id
            else:
                pw_resp = await self.client.passwords.create_async(
                    email=test_user.email, password=test_user.old_password
                )
                user_id = pw_resp.user_id

            yield self.__get_temporary_created_test_user(test_user, user_id)
            await self.client.users.delete_async(user_id=user_id)
        else:
            yield test_user
