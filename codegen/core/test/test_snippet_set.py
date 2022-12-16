#!/usr/bin/env python3

from __future__ import annotations

import os
import pathlib
import unittest
from dataclasses import dataclass
from typing import Dict, Type, Union

from codegen.core.snippet_set import (
    SnippetKeyMismatchError,
    SnippetSet,
    UnterminatedSnippetError,
)

RESOURCES_DIR = pathlib.Path(__file__).parent / "resources"
INPUT_EXTENSION = ".snippets_test"
OLD_SNIPPETS_EXTENSION = ".snippets"
SNIPPETS_EXTENSION = ".snippets"
EXPECTED_EXTENSION = ".expected"
ERROR_EXTENSION = ".error"


@dataclass
class SnippetTest:
    input_path: str
    input_lines: str
    expected: Union[str, Type[Exception]]
    old_snippets: Dict[str, str]
    snippets: Dict[str, str]

    @classmethod
    def from_input_filepath(cls, input_path: pathlib.Path) -> SnippetTest:
        snippets_path = input_path.with_suffix(SNIPPETS_EXTENSION)
        old_snippets = {"snippet1": "old_snippet1\n"}
        snippets = {}

        expected_path = input_path.with_suffix(EXPECTED_EXTENSION)

        with open(input_path) as f:
            input_lines = f.read()

        expected: Union[str, Type[Exception]]
        if os.path.exists(expected_path):
            with open(expected_path) as f:
                expected = f.read()
        else:
            error_path = expected_path.with_suffix(ERROR_EXTENSION)
            with open(error_path) as f:
                contents = f.read().strip()
                if contents.strip() == "SnippetKeyMismatchError":
                    expected = SnippetKeyMismatchError
                elif contents.strip() == "UnterminatedSnippetError":
                    expected = UnterminatedSnippetError
                else:
                    raise ValueError(f"Unsupported error type `{contents}`")
        with open(snippets_path) as f:
            snippets = dict(line.split("=") for line in f)
            # A bit hacky, but if we have more than snippet1,
            # we assume they're empty by default
            for snippet in snippets:
                if snippet != "snippet1":
                    old_snippets[snippet] = ""

        return SnippetTest(
            input_path=str(input_path),
            input_lines=input_lines,
            expected=expected,
            old_snippets=old_snippets,
            snippets=snippets,
        )


class TestSnippetSet(unittest.TestCase):
    def setUp(self) -> None:
        self.tests = {
            os.path.basename(p): SnippetTest.from_input_filepath(RESOURCES_DIR / p)
            for p in os.listdir(RESOURCES_DIR)
            if p.endswith(INPUT_EXTENSION)
        }

    def test_len(self) -> None:
        s = SnippetSet({"a": "b", "c": "d"})
        self.assertEqual(2, len(s))

    def test_replace_all(self) -> None:
        for name, test in self.tests.items():
            with self.subTest(name):
                # Arrange
                snippet_set = SnippetSet(snippets=test.snippets)
                if isinstance(test.expected, str):
                    # Act
                    actual = snippet_set.replace_all(test.input_lines)
                    # Assert
                    self.assertEqual(test.expected, actual)
                else:
                    # Act and assert
                    with self.assertRaises(test.expected):
                        snippet_set.replace_all(test.input_lines)

    def test_from_file(self) -> None:
        for name, test in self.tests.items():
            with self.subTest(name):
                if isinstance(test.expected, str):
                    # Act
                    actual = SnippetSet.from_file(test.input_path).snippets
                    # Assert
                    self.assertEqual(test.old_snippets, actual)
                else:
                    # Act and assert
                    with self.assertRaises(test.expected):
                        SnippetSet.from_file(test.input_path)
