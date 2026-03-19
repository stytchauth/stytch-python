#!/usr/bin/env python3

import asyncio
import time
import unittest
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

from stytch.consumer.api.sessions import Sessions
from stytch.consumer.models.sessions import AuthorizationCheck
from stytch.shared.jwt_helpers import GenericClaims

FAKE_JWT = "fake.jwt.token"
FAKE_PROJECT_ID = "project-test-abc123"
_SESSION_CLAIM = "https://stytch.com/session"

FAKE_GENERIC_CLAIMS = GenericClaims(
    reserved_claims={"sub": "user-test-123", "exp": 9999999999},
    untyped_claims={
        _SESSION_CLAIM: {
            "id": "session-test-123",
            "attributes": None,
            "authentication_factors": [],
            "last_accessed_at": "2026-01-01T00:00:00Z",
            "started_at": "2026-01-01T00:00:00Z",
            "expires_at": "2026-01-01T01:00:00Z",
            "roles": ["stytch_member"],
        }
    },
)


def _make_sessions() -> Sessions:
    mock_api_base = MagicMock()
    mock_api_base.base_url = "https://test.stytch.com/"
    return Sessions(
        api_base=mock_api_base,
        sync_client=MagicMock(),
        async_client=MagicMock(),
        jwks_client=MagicMock(),
        project_id=FAKE_PROJECT_ID,
        policy_cache=MagicMock(),
    )


class TestConsumerAuthenticateJWTLocalAsync(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.sessions = _make_sessions()
        self.auth_check = AuthorizationCheck(resource_id="documents", action="read")

    def test_is_coroutine_function(self) -> None:
        self.assertTrue(
            asyncio.iscoroutinefunction(self.sessions.authenticate_jwt_local_async)
        )

    @patch(
        "stytch.consumer.api.sessions.jwt_helpers.authenticate_jwt_local_async",
        new_callable=AsyncMock,
    )
    async def test_returns_none_for_invalid_jwt(self, mock_jwt) -> None:
        mock_jwt.return_value = None
        result = await self.sessions.authenticate_jwt_local_async(session_jwt=FAKE_JWT)
        self.assertIsNone(result)

    @patch(
        "stytch.consumer.api.sessions.jwt_helpers.authenticate_jwt_local_async",
        new_callable=AsyncMock,
    )
    async def test_returns_session_for_valid_jwt_without_auth_check(
        self, mock_jwt
    ) -> None:
        mock_jwt.return_value = FAKE_GENERIC_CLAIMS
        result = await self.sessions.authenticate_jwt_local_async(session_jwt=FAKE_JWT)
        self.assertIsNotNone(result)
        if result is not None:
            self.assertEqual(result.session_id, "session-test-123")
            self.assertEqual(result.user_id, "user-test-123")

    @patch(
        "stytch.consumer.api.sessions.rbac_local.perform_consumer_authorization_check"
    )
    @patch(
        "stytch.consumer.api.sessions.jwt_helpers.authenticate_jwt_local_async",
        new_callable=AsyncMock,
    )
    async def test_uses_get_async_not_get_for_authorization_check(
        self, mock_jwt, _mock_rbac
    ) -> None:
        mock_jwt.return_value = FAKE_GENERIC_CLAIMS
        mock_policy = MagicMock()
        policy_cache = cast(MagicMock, self.sessions.policy_cache)
        policy_cache.get_async = AsyncMock(return_value=mock_policy)

        await self.sessions.authenticate_jwt_local_async(
            session_jwt=FAKE_JWT, authorization_check=self.auth_check
        )

        policy_cache.get_async.assert_awaited_once()
        policy_cache.get.assert_not_called()

    async def test_is_non_blocking_jwt_verification(self) -> None:
        DELAY = 0.1
        N = 5

        async def slow_authenticate_jwt_local_async(**kwargs) -> GenericClaims:
            await asyncio.sleep(DELAY)
            return FAKE_GENERIC_CLAIMS

        with patch(
            "stytch.consumer.api.sessions.jwt_helpers.authenticate_jwt_local_async",
            side_effect=slow_authenticate_jwt_local_async,
        ):
            start = time.monotonic()
            results = await asyncio.gather(
                *[
                    self.sessions.authenticate_jwt_local_async(session_jwt=FAKE_JWT)
                    for _ in range(N)
                ]
            )
            elapsed = time.monotonic() - start

        # All N calls should interleave at the await point, completing in ~DELAY total
        # (not N * DELAY as would happen if get_signing_key_from_jwt blocked the event loop)
        self.assertLess(elapsed, DELAY * 2)
        self.assertEqual(len(results), N)


if __name__ == "__main__":
    unittest.main()
