#!/usr/bin/env python3

import unittest

from codegen.types.http_method import HttpMethod


class TestHttpMethod(unittest.TestCase):
    def test_from_str(self) -> None:
        # Arrange
        tests_with_expected = [
            ("GET", HttpMethod.GET),
            ("POST", HttpMethod.POST),
            ("PUT", HttpMethod.PUT),
            ("DELETE", HttpMethod.DELETE),
        ]
        bad_input = ["_get", "head", "patch"]

        for s, expected in tests_with_expected:
            # Act
            actual = HttpMethod.from_str(s)
            # Assert
            self.assertEqual(expected, actual)

        for s in bad_input:
            # Act and Assert
            with self.assertRaises(ValueError):
                HttpMethod.from_str(s)

    def test_str(self) -> None:
        # Arrange
        tests_with_expected = [
            (HttpMethod.GET, "get"),
            (HttpMethod.POST, "post"),
            (HttpMethod.PUT, "put"),
            (HttpMethod.DELETE, "delete"),
        ]

        for method, expected in tests_with_expected:
            # Act
            actual = str(method)
            # Assert
            self.assertEqual(expected, actual)
