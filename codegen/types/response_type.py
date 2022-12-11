#!/usr/bin/env python3

from __future__ import annotations

from typing import Dict

from codegen.types.templates import get_template


class ResponseType:
    def __init__(self, name: str, d: Dict[str, str]) -> None:
        self.name = name
        self.d = d

    def generate(self) -> str:
        template = get_template("response.tmpl")
        return template.render(this=self)
