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

from stytch.api.sessions import Sessions
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import StytchSession
from stytch.models.sessions import AuthenticateResponse


class TestSessionsAsync(IsolatedAsyncioTestCase):
    async def test_authenticate_jwt_async(self) -> None:
        # Arrange
        sessions = Sessions(
            api_base=create_autospec(ApiBase),
            sync_client=create_autospec(SyncClient),
            async_client=create_autospec(AsyncClient),
        )
        sessions.authenticate_async = AsyncMock(  # type: ignore [assignment]
            return_value=AuthenticateResponse(
                status_code=200,
                request_id="request-api",
                session=create_autospec(StytchSession),
            )
        )

        with self.subTest("local"):
            # Arrange more
            sessions.authenticate_jwt_local = MagicMock(  # type: ignore [assignment]
                return_value=AuthenticateResponse(
                    status_code=200,
                    request_id="request-local",
                    session=create_autospec(StytchSession),
                )
            )
            # Act
            resp = await sessions.authenticate_jwt_async(session_jwt="fake-jwt")
            # Assert
            sessions.authenticate_jwt_local.assert_called_once()
            self.assertEqual("request-local", resp.request_id)
        with self.subTest("from_api"):
            # Arrange more
            sessions.authenticate_jwt_local = MagicMock(  # type: ignore [assignment]
                return_value=None
            )
            # Act
            resp = await sessions.authenticate_jwt_async(session_jwt="fake-jwt")
            # Assert
            sessions.authenticate_jwt_local.assert_called_once()
            self.assertEqual("request-api", resp.request_id)
