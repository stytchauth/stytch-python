#!/usr/bin/env python3

from __future__ import annotations

import datetime
import time
import unittest
from unittest.mock import MagicMock, create_autospec, patch

from stytch.api.sessions import Sessions
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import StytchSession
from stytch.models.sessions import AuthenticateResponse


class TestSessions(unittest.TestCase):
    def test_authenticate_jwt(self) -> None:
        # Arrange
        sessions = Sessions(
            api_base=create_autospec(ApiBase),
            sync_client=create_autospec(SyncClient),
            async_client=create_autospec(AsyncClient),
        )
        # mypy doesn't approve of monkey-patching methods
        sessions.authenticate = MagicMock(  # type: ignore [assignment]
            return_value=AuthenticateResponse(
                status_code=200,
                request_id="request-api",
                session=create_autospec(StytchSession),
            )
        )

        with self.subTest("local"):
            # Arrange more
            # mypy doesn't approve of monkey-patching methods
            sessions.authenticate_jwt_local = MagicMock(  # type: ignore [assignment]
                return_value=AuthenticateResponse(
                    status_code=200,
                    request_id="request-local",
                    session=create_autospec(StytchSession),
                )
            )
            # Act
            resp = sessions.authenticate_jwt(session_jwt="fake-jwt")
            # Assert
            sessions.authenticate_jwt_local.assert_called_once()
            self.assertEqual("request-local", resp.request_id)
        with self.subTest("from_api"):
            # Arrange more
            sessions.authenticate_jwt_local = MagicMock(  # type: ignore [assignment]
                return_value=None
            )
            # Act
            resp = sessions.authenticate_jwt(session_jwt="fake-jwt")
            # Assert
            sessions.authenticate_jwt_local.assert_called_once()
            self.assertEqual("request-api", resp.request_id)

    # Same method for sync and async
    @patch("stytch.api.sessions.jwt")
    def test_authenticate_jwt_local(self, patched_jwt: MagicMock) -> None:
        # Arrange - yes, it's a lot to set up
        now = int(time.time())
        now_dt = datetime.datetime.fromtimestamp(now, tz=datetime.timezone.utc)
        now_str = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))
        attributes = {"user_agent": "unit_test"}
        user_id = "fake-user-id-123"
        session_id = "fake-session-id-456"
        auth_factor = {
            "delivery_method": "email",
            "email_factor": {
                "email_address": "sandbox@stytch.com",
                "email_id": "fake-email-id-123",
            },
            "last_authenticated_at": now_str,
            "type": "magic_link",
        }
        patched_jwt.decode.return_value = {
            "iat": now,
            "exp": now,
            "sub": user_id,
            "https://stytch.com/session": {
                "expires_at": now_str,
                "attributes": attributes,
                "authentication_factors": [auth_factor],
                "last_accessed_at": now_str,
                "id": session_id,
                "started_at": now_str,
            },
        }
        expected_session = StytchSession(
            attributes=attributes,
            authentication_factors=[auth_factor],
            custom_claims=None,
            expires_at=now_dt,
            last_accessed_at=now_dt,
            session_id=session_id,
            started_at=now_dt,
            user_id=user_id,
        )
        sessions = Sessions(
            api_base=create_autospec(ApiBase),
            sync_client=create_autospec(SyncClient, project_id="", secret=""),
            async_client=create_autospec(AsyncClient, project_id="", secret=""),
        )

        with self.subTest("no_max_token_age"):
            # Act
            res = sessions.authenticate_jwt_local(session_jwt="fake-jwt")
            self.assertIsNotNone(res)
            # Assert
            # Type checker doesn't understand the above line :(
            assert res is not None
            self.assertEqual(res.session, expected_session)
        with self.subTest("with_max_token_age_valid"):
            # Act
            res = sessions.authenticate_jwt_local(
                session_jwt="fake-jwt", max_token_age_seconds=10
            )
            # Assert
            self.assertIsNotNone(res)
            # Type checker doesn't understand the above line :(
            assert res is not None
            self.assertEqual(res.session, expected_session)
        with self.subTest("with_max_token_age_invalid"):
            # Act
            res = sessions.authenticate_jwt_local(
                session_jwt="fake-jwt", max_token_age_seconds=0
            )
            # Assert
            self.assertIsNone(res)
