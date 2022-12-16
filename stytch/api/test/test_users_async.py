#!/usr/bin/env python3

import sys
import unittest
from unittest.mock import MagicMock, create_autospec

if sys.version_info < (3, 8):
    # When running 3.7, we unfortunately can't test async properly
    AsyncMock = MagicMock
    IsolatedAsyncioTestCase = unittest.TestCase
else:
    from unittest import IsolatedAsyncioTestCase
    from unittest.mock import AsyncMock

from stytch.api.test.test_users import EXPECTED_RESPONSES, get_fake_search_responses
from stytch.api.users import Users
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class TestUsersAsync(IsolatedAsyncioTestCase):
    async def test_search_all_async(self) -> None:
        # Arrange
        users = Users(
            api_base=create_autospec(ApiBase),
            sync_client=create_autospec(SyncClient),
            async_client=create_autospec(AsyncClient),
        )
        users.search_async = AsyncMock(  # type: ignore [assignment]
            side_effect=get_fake_search_responses(EXPECTED_RESPONSES)
        )
        # Act
        async for _ in users.search_all_async():
            pass
        # Assert
        self.assertEqual(EXPECTED_RESPONSES, len(users.search_async.mock_calls))
