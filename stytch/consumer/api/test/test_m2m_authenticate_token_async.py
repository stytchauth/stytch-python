#!/usr/bin/env python3

import asyncio
import time
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from stytch.consumer.api.m2m import M2M
from stytch.shared.jwt_helpers import GenericClaims

FAKE_JWT = "fake.jwt.token"
FAKE_PROJECT_ID = "project-test-abc123"

FAKE_GENERIC_CLAIMS = GenericClaims(
    reserved_claims={"sub": "m2m-client-test-123", "exp": 9999999999},
    untyped_claims={"scope": "read:docs write:docs"},
)


def _make_m2m() -> M2M:
    mock_api_base = MagicMock()
    mock_api_base.base_url = "https://test.stytch.com/"
    return M2M(
        api_base=mock_api_base,
        sync_client=MagicMock(),
        async_client=MagicMock(),
        jwks_client=MagicMock(),
        project_id=FAKE_PROJECT_ID,
    )


class TestM2MAuthenticateTokenAsync(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.m2m = _make_m2m()

    def test_is_coroutine_function(self) -> None:
        self.assertTrue(asyncio.iscoroutinefunction(self.m2m.authenticate_token_async))

    @patch(
        "stytch.consumer.api.m2m.jwt_helpers.authenticate_jwt_local_async",
        new_callable=AsyncMock,
    )
    async def test_returns_none_for_invalid_jwt(self, mock_jwt) -> None:
        mock_jwt.return_value = None
        result = await self.m2m.authenticate_token_async(access_token=FAKE_JWT)
        self.assertIsNone(result)

    @patch(
        "stytch.consumer.api.m2m.jwt_helpers.authenticate_jwt_local_async",
        new_callable=AsyncMock,
    )
    async def test_returns_claims_for_valid_jwt(self, mock_jwt) -> None:
        mock_jwt.return_value = FAKE_GENERIC_CLAIMS
        result = await self.m2m.authenticate_token_async(access_token=FAKE_JWT)
        self.assertIsNotNone(result)
        if result is not None:
            self.assertEqual(result.client_id, "m2m-client-test-123")
            self.assertEqual(result.scopes, ["read:docs", "write:docs"])

    @patch(
        "stytch.consumer.api.m2m.jwt_helpers.authenticate_jwt_local_async",
        new_callable=AsyncMock,
    )
    async def test_returns_none_when_required_scope_missing(self, mock_jwt) -> None:
        mock_jwt.return_value = FAKE_GENERIC_CLAIMS
        result = await self.m2m.authenticate_token_async(
            access_token=FAKE_JWT, required_scopes=["admin"]
        )
        self.assertIsNone(result)

    async def test_is_non_blocking_jwt_verification(self) -> None:
        DELAY = 0.1
        N = 5

        async def slow_authenticate_jwt_local_async(**kwargs) -> GenericClaims:
            await asyncio.sleep(DELAY)
            return FAKE_GENERIC_CLAIMS

        with patch(
            "stytch.consumer.api.m2m.jwt_helpers.authenticate_jwt_local_async",
            side_effect=slow_authenticate_jwt_local_async,
        ):
            start = time.monotonic()
            results = await asyncio.gather(
                *[
                    self.m2m.authenticate_token_async(access_token=FAKE_JWT)
                    for _ in range(N)
                ]
            )
            elapsed = time.monotonic() - start

        # All N calls should interleave at the await point, completing in ~DELAY total
        self.assertLess(elapsed, DELAY * 2)
        self.assertEqual(len(results), N)


if __name__ == "__main__":
    unittest.main()
