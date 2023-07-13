#!/usr/bin/env python3

from __future__ import annotations

import unittest
from unittest.mock import create_autospec

from stytch.core.response_base import ResponseBase, StytchError, StytchErrorDetails


class DummyResponse(ResponseBase):
    extra_string: str

    @classmethod
    def with_status_code(
        cls, status_code: int, extra_string: str = "foo"
    ) -> DummyResponse:
        return DummyResponse(
            status_code=status_code,
            request_id="dummy-request",
            extra_string=extra_string,
        )

    @classmethod
    def error(cls) -> DummyResponse:
        return DummyResponse.from_json(
            status_code=400,
            json={
                "status_code": 400,
                "request_id": "dummy-request",
                "error_type": "dummy_error_type",
                "error_message": "something went wrong",
                "error_url": "localhost",
            },
        )

    @classmethod
    def fatal(cls) -> DummyResponse:
        return DummyResponse.from_json(
            status_code=502,
            json={},
        )


class TestModels(unittest.TestCase):
    def test_is_informational(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(101)
        resp2 = DummyResponse.with_status_code(200)
        # Assert
        self.assertTrue(resp.is_informational)
        self.assertFalse(resp2.is_informational)

    def test_is_success(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(200)
        resp2 = DummyResponse.with_status_code(401)
        # Assert
        self.assertTrue(resp.is_success)
        self.assertFalse(resp2.is_success)

    def test_is_redirection(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(301)
        resp2 = DummyResponse.with_status_code(200)
        # Assert
        self.assertTrue(resp.is_redirection)
        self.assertFalse(resp2.is_redirection)

    def test_is_client_error(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(403)
        resp2 = DummyResponse.with_status_code(200)
        # Assert
        self.assertTrue(resp.is_client_error)
        self.assertFalse(resp2.is_client_error)

    def test_is_server_error(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(500)
        resp2 = DummyResponse.with_status_code(200)
        # Assert
        self.assertTrue(resp.is_server_error)
        self.assertFalse(resp2.is_server_error)

    def test_stytcherror_from_validation_error(self) -> None:
        with self.assertRaises(StytchError) as e:
            DummyResponse.error()
        self.assertTrue(e.exception.details.is_client_error)

    def test_stytcherror_from_unknown(self) -> None:
        # Test for when we can't even load a StytchErrorDetails object
        with self.assertRaises(StytchError) as e:
            DummyResponse.fatal()
        self.assertTrue(e.exception.details.is_server_error)

    def test_stytcherror(self) -> None:
        # Just check that calling repr/str calls str on
        # the underlying details object
        with self.subTest("repr"):
            mock_details = create_autospec(StytchErrorDetails)
            repr(StytchError(mock_details))
            mock_details.__str__.assert_called_once()
        with self.subTest("str"):
            mock_details = create_autospec(StytchErrorDetails)
            str(StytchError(mock_details))
            mock_details.__str__.assert_called_once()

    def test_stytcherror_fields(self) -> None:
        resp = {
            "status_code": 418,
            "request_id": "request-id-test-fea11c44-5514-4aac-a76b-3ca685e3443a",
            "error_type": "is_a_teapot",
            "error_message": "I'm a teapot!",
            "error_url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418",
        }
        expected = StytchErrorDetails(**resp)

        with self.assertRaises(StytchError) as e:
            DummyResponse.from_json(418, resp)

        self.assertEqual(e.exception.details, expected)
