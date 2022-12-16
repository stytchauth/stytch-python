#!/usr/bin/env python3

import unittest
from unittest.mock import mock_open, patch

import yaml

from codegen.types.api import Api


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.api = Api(
            classname="OAuth",
            methods=[],
            sub_apis=[],
            additional_imports=[],
            filename="oauth",
            sub_url="oauth",
        )

    def test_filename_base(self) -> None:
        # Arrange
        tests_with_expected = [
            ("hello", "hello"),
            ("hello.world", "world"),
            ("a.b.c.def", "def"),
        ]
        for filename, expected in tests_with_expected:
            # Arrange more
            self.api.filename = filename
            # Act
            actual = self.api.filename_base
            # Assert
            self.assertEqual(expected, actual)

    def test_from_dict(self) -> None:
        # Arrange
        d = {
            "classname": "OAuth",
            "methods": [],
            "sub_apis": [],
            "additional_imports": [],
            "filename": "oauth",
            "sub_url": "oauth",
        }
        with self.subTest("all_present"):
            # Act
            actual = Api.from_dict(d)
            # Assert
            self.assertEqual(self.api, actual)
        with self.subTest("infer_filename"):
            # Arrange more
            this_data = d.copy()
            del this_data["filename"]
            self.api.filename = "o_auth"
            # Act
            actual = Api.from_dict(this_data)
            # Assert
            self.assertEqual(self.api, actual)
        with self.subTest("minimal"):
            # Arrange more
            this_data = d.copy()
            del this_data["sub_apis"]
            del this_data["additional_imports"]
            del this_data["filename"]
            del this_data["sub_url"]
            self.api.sub_url = "o_auth"
            self.api.filename = "o_auth"
            # Act
            actual = Api.from_dict(this_data)
            # Assert
            self.assertEqual(self.api, actual)

    def test_from_yml(self) -> None:
        # Arrange
        d = {
            "classname": "OAuth",
            "methods": [],
            "sub_apis": [],
            "additional_imports": [],
            "filename": "oauth",
            "sub_url": "oauth",
        }
        yaml_data = yaml.dump(d)
        # Act
        with patch("builtins.open", mock_open(read_data=yaml_data)):
            actual = Api.from_yml(yaml_data)
        # Assert
        self.assertEqual(self.api, actual)

    # Tests for logically private methods
    def test__gen_filename_from_classname(self) -> None:
        tests_with_expected = [
            ("simple", "simple"),
            ("Simple2", "simple2"),
            ("getHTTPResponseCode", "get_http_response_code"),
            ("HTTPResponseCodeXYZ", "http_response_code_xyz"),
        ]
        for classname, expected in tests_with_expected:
            # Act
            actual = Api._gen_filename_from_classname(classname)
            # Assert
            self.assertEqual(expected, actual)
