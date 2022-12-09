#!/usr/bin/env python3

from __future__ import annotations

import logging
import re
from typing import Dict, Optional

BEGIN_SNIPPET_REGEX = re.compile(r"# MANUAL\((.*)\)")
END_SNIPPET_REGEX = re.compile(r"# ENDMANUAL\((.*)\)")


class SnippetKeyMismatchError(ValueError):
    def __init__(self, begin_key: str, end_key: str) -> None:
        message = f"Begin key ('{begin_key}') does not match end key ('{end_key}')"
        super().__init__(message)


class UnterminatedSnippetError(ValueError):
    def __init__(self, key: str) -> None:
        message = f"Did not find an end marker for key ('{key}')"
        super().__init__(message)


class SnippetSet:
    def __init__(self, snippets: Optional[Dict[str, str]] = None) -> None:
        self.snippets = snippets or {}

    def replace_all(self, s: str) -> str:
        res = ""
        cur_key = ""
        in_snippet = False
        did_replacement = False

        for line in s.splitlines(keepends=True):
            if match := BEGIN_SNIPPET_REGEX.search(line):
                # Keep the begin/end markers
                res += line

                in_snippet = True
                cur_key = match.group(1)
                logging.debug(f"Found snippet in replace_all: {cur_key}")
                if cur_key in self.snippets:
                    logging.debug(f"Replacing '{cur_key}' with saved snippet")
                    res += self.snippets[cur_key]
                    did_replacement = True
            elif match := END_SNIPPET_REGEX.search(line):
                # Keep the begin/end markers
                res += line

                in_snippet = False
                if match.group(1) != cur_key:
                    raise SnippetKeyMismatchError(
                        begin_key=cur_key, end_key=match.group(1)
                    )
            elif not in_snippet or not did_replacement:
                # If we're not in a snippet or didn't have a replacement,
                # just append the line like normal
                res += line
        if in_snippet:
            raise UnterminatedSnippetError(key=cur_key)
        return res

    def __len__(self) -> int:
        return len(self.snippets)

    @classmethod
    def from_file(cls, filepath: str) -> SnippetSet:
        res = {}

        with open(filepath) as f:
            cur_key = ""
            cur_value = ""
            in_snippet = False

            for line in f:
                if match := BEGIN_SNIPPET_REGEX.search(line):
                    in_snippet = True
                    cur_key = match.group(1)
                    cur_value = ""
                    logging.debug(f"Found snippet in from_file: {cur_key}")
                elif match := END_SNIPPET_REGEX.search(line):
                    in_snippet = False
                    res[cur_key] = cur_value
                    if match.group(1) != cur_key:
                        raise SnippetKeyMismatchError(
                            begin_key=cur_key, end_key=match.group(1)
                        )
                elif in_snippet:
                    cur_value += line

        if in_snippet:
            raise UnterminatedSnippetError(key=cur_key)
        return SnippetSet(res)
