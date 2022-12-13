#!/usr/bin/env python3

from __future__ import annotations

from typing import Any, Dict, Optional

from codegen.types.templates import get_template


class ResponseType:
    EXTENDS_KEY = "__extends"

    def __init__(
        self,
        name: str,
        d: Dict[str, str],
        extends: Optional[str] = None,
    ) -> None:
        self.name = name
        self.d = d
        self.extends = extends

    def generate(self) -> str:
        template = get_template("response.tmpl")
        return template.render(this=self)

    @classmethod
    def from_dict(cls, name: str, d: Dict[str, Any]) -> ResponseType:
        extends = None
        if cls.EXTENDS_KEY in d:
            extends = str(d[cls.EXTENDS_KEY])
            del d[cls.EXTENDS_KEY]

        return ResponseType(name=name, d=d, extends=extends)
