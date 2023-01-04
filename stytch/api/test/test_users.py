#!/usr/bin/env python3

import unittest
from typing import List
from unittest.mock import create_autospec

from stytch.api.users import Users
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import SearchResultsMetadata, User
from stytch.models.users import SearchResponse

EXPECTED_RESPONSES = 3


def generate_fake_search_responses(num_results: int) -> List[SearchResponse]:
    return [
        SearchResponse(
            status_code=200,
            request_id=f"request-{i}",
            results=[create_autospec(User)],
            results_metadata=SearchResultsMetadata(next_cursor=f"cursor{i}", total=1),
        )
        for i in range(num_results - 1)
    ] + [
        SearchResponse(
            status_code=200,
            request_id=f"request-{num_results}",
            results=[create_autospec(User)],
            results_metadata=SearchResultsMetadata(next_cursor=None, total=1),
        )
    ]


class TestUsers(unittest.TestCase):
    def test_search_all(self) -> None:
        # Arrange
        users = Users(
            api_base=create_autospec(ApiBase),
            sync_client=create_autospec(SyncClient),
            async_client=create_autospec(AsyncClient),
        )
        # mypy doesn't approve of monkey-patching methods
        users.search = MagicMock(  # type: ignore [assignment]
            side_effect=generate_fake_search_responses(EXPECTED_RESPONSES)
        )
        # Act
        for _ in users.search_all():
            pass
        # Assert
        self.assertEqual(EXPECTED_RESPONSES, len(users.search.mock_calls))