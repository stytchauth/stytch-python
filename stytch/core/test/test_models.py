#!/usr/bin/env python3

from __future__ import annotations

import unittest
from unittest.mock import create_autospec, patch

from stytch.core import models


class DummyResponse(models.ResponseBase):
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
        pass

    def test_is_client_error(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(403)
        resp2 = DummyResponse.with_status_code(200)
        # Assert
        self.assertTrue(resp.is_client_error)
        self.assertFalse(resp2.is_client_error)
        pass

    def test_is_server_error(self) -> None:
        # Act
        resp = DummyResponse.with_status_code(500)
        resp2 = DummyResponse.with_status_code(200)
        # Assert
        self.assertTrue(resp.is_server_error)
        self.assertFalse(resp2.is_server_error)

    def test_stytcherror_from_validation_error(self) -> None:
        with self.assertRaises(models.StytchError) as e:
            DummyResponse.error()
        self.assertTrue(e.exception.details.is_client_error)

    def test_stytcherror_from_unknown(self) -> None:
        # Test for when we can't even load a StytchErrorDetails object
        with self.assertRaises(models.StytchError) as e:
            DummyResponse.fatal()
        self.assertTrue(e.exception.details.is_server_error)

    def test_stytcherror(self) -> None:

        # Just check that calling repr/str calls str on
        # the underlying details object
        with self.subTest("repr"):
            mock_details = create_autospec(models.StytchErrorDetails)
            repr(models.StytchError(mock_details))
            mock_details.__str__.assert_called_once()
        with self.subTest("str"):
            mock_details = create_autospec(models.StytchErrorDetails)
            str(models.StytchError(mock_details))
            mock_details.__str__.assert_called_once()
