#!/usr/bin/env python3

import contextlib
import pathlib
import shutil
import tempfile
import unittest

from codegen.core.snippet_set import SnippetSet
from codegen.types.api import Api

RESOURCES_DIR = pathlib.Path(__file__).parent / "resources"
INPUT_FILEPATH = RESOURCES_DIR / "users.yml"
API_EXPECTED = RESOURCES_DIR / "api.expected"
MODELS_EXPECTED = RESOURCES_DIR / "models.expected"
METHOD_EXPECTED = RESOURCES_DIR / "method.expected"
RESPONSE_TYPE_EXPECTED = RESOURCES_DIR / "response_type.expected"


# This class tests the actual templating logic of the codegen library.
# Yes, this is brittle, but it's important to have some sort of test so
# that we have confidence in the templating behavior, and the tradeoff
# of requiring someone to manually edit the expected templates whenever
# a change is made is a necessary evil to ensure the templates don't
# accidentally break
class TestTemplating(unittest.TestCase):
    def setUp(self) -> None:
        self.api = Api.from_yml(str(INPUT_FILEPATH))
        self.method = self.api.methods[0]
        assert self.method.response_type is not None
        self.response_type = self.method.response_type

    def assertLinesEqual(self, expected: str, actual: str) -> None:
        expected_lines = expected.split("\n")
        actual_lines = actual.split("\n")
        self.assertEqual(len(expected_lines), len(actual_lines))
        for i in range(len(expected_lines)):
            self.assertEqual(
                expected_lines[i], actual_lines[i], msg=f"Failed at line {i + 1}"
            )

    def test_api(self) -> None:
        # Arrange
        empty_snippets = SnippetSet()
        with open(API_EXPECTED) as f:
            api_expected_content = f.read()
        with open(MODELS_EXPECTED) as f:
            models_expected_content = f.read()
        # Act
        api_actual = self.api.generate(
            snippets=empty_snippets, api_path_in_gen="api", models_path_in_gen="models"
        )
        models_actual = self.api.generate_responses()
        # Assert
        self.assertLinesEqual(api_expected_content, api_actual)
        self.assertLinesEqual(models_expected_content, models_actual)

    def test_api_generate_all(self) -> None:
        # Arrange
        with open(API_EXPECTED) as f:
            api_expected_content = f.read()
        with open(MODELS_EXPECTED) as f:
            models_expected_content = f.read()

        # Act
        api_actual = ""
        models_actual = ""
        with contextlib.ExitStack() as stack:
            api_dir = stack.enter_context(tempfile.TemporaryDirectory())
            models_dir = stack.enter_context(tempfile.TemporaryDirectory())
            self.api.generate_all(
                api_dir=api_dir,
                models_dir=models_dir,
                api_path_in_gen="api",
                models_path_in_gen="models",
            )
            with open(pathlib.Path(api_dir) / "users.py") as f:
                api_actual = f.read()
            with open(pathlib.Path(models_dir) / "users.py") as f:
                models_actual = f.read()

        # Assert
        self.assertLinesEqual(api_expected_content, api_actual)
        self.assertLinesEqual(models_expected_content, models_actual)

    def test_method(self) -> None:
        # Arrange
        with open(METHOD_EXPECTED) as f:
            expected = f.read()
        # Act
        actual = self.method.generate()
        # Assert
        self.assertLinesEqual(expected, actual)

    def test_response_type(self) -> None:
        # Arrange
        with open(RESPONSE_TYPE_EXPECTED) as f:
            expected = f.read()
        # Act
        actual = self.response_type.generate()
        # Assert
        self.assertLinesEqual(expected, actual)
