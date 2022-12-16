#!/usr/bin/env python3

import unittest
from dataclasses import dataclass

from codegen.types.argument import Argument


@dataclass
class ArgumentTestCase:
    arg: Argument
    in_params: str
    in_dict_inline: str
    in_dict_assignment: str


class TestArgument(unittest.TestCase):
    def setUp(self) -> None:
        self.dictname = "payload"
        self.testcases = {
            "basic_required": ArgumentTestCase(
                arg=Argument(name="arg", arg_type="int"),
                in_params="arg: int",
                in_dict_inline='"arg": arg,',
                in_dict_assignment='payload["arg"] = arg',
            ),
            "basic_optional": ArgumentTestCase(
                arg=Argument(name="arg2", arg_type="Optional[str]"),
                in_params="arg2: Optional[str]",
                in_dict_inline='"arg2": arg2,',
                in_dict_assignment='payload["arg2"] = arg2',
            ),
            "mapped_argument": ArgumentTestCase(
                arg=Argument(name="arg3", arg_type="float", map_with="math.sqrt"),
                in_params="arg3: float",
                in_dict_inline='"arg3": math.sqrt(arg3),',
                in_dict_assignment='payload["arg3"] = math.sqrt(arg3)',
            ),
            "map_method": ArgumentTestCase(
                arg=Argument(name="arg4", arg_type="str", map_with_method="upper()"),
                in_params="arg4: str",
                in_dict_inline='"arg4": arg4.upper(),',
                in_dict_assignment='payload["arg4"] = arg4.upper()',
            ),
            "include_if_null": ArgumentTestCase(
                arg=Argument(
                    name="arg5",
                    arg_type="Optional[str] = None",
                    include_if_null=True,
                ),
                in_params="arg5: Optional[str] = None",
                in_dict_inline='"arg5": arg5,',
                in_dict_assignment='payload["arg5"] = arg5',
            ),
        }

    def test_generate_in_params(self) -> None:
        for name, testcase in self.testcases.items():
            with self.subTest(name):
                # Act
                actual = testcase.arg.generate_in_params()
                # Assert
                self.assertEqual(testcase.in_params, actual)

    def test_generate_in_dict_inline(self) -> None:
        for name, testcase in self.testcases.items():
            with self.subTest(name):
                # Act
                actual = testcase.arg.generate_in_dict_inline()
                # Assert
                self.assertEqual(testcase.in_dict_inline, actual)

    def test_generate_in_dict_assignment(self) -> None:
        for name, testcase in self.testcases.items():
            with self.subTest(name):
                # Act
                actual = testcase.arg.generate_in_dict_assignment(self.dictname)
                # Assert
                self.assertEqual(testcase.in_dict_assignment, actual)

    def test_nullable(self) -> None:
        self.assertTrue(self.testcases["basic_optional"].arg.nullable)
        self.assertFalse(self.testcases["basic_required"].arg.nullable)

    def test_always_include(self) -> None:
        self.assertTrue(self.testcases["basic_required"].arg.always_include)
        self.assertFalse(self.testcases["basic_optional"].arg.always_include)
        self.assertTrue(self.testcases["include_if_null"].arg.always_include)

    def test_from_dict(self) -> None:
        # Arrange
        expected = Argument(
            name="arg",
            arg_type="Optional[str] = None",
            include_if_null=False,
        )
        # Act
        actual = Argument.from_dict({"name": "arg", "arg_type": "Optional[str] = None"})
        # Assert
        self.assertEqual(expected, actual)
