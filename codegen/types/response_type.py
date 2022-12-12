#!/usr/bin/env python3

from __future__ import annotations

from typing import Any, Dict, Optional

from codegen.types.templates import get_template


class ResponseType:
    OMIT_REQUEST_ID_KEY = "__omit_request_id"
    EXTENDS_KEY = "__extends"

    def __init__(
        self,
        name: str,
        d: Dict[str, str],
        omit_request_id: bool = False,
        extends: Optional[str] = None,
    ) -> None:
        self.name = name
        self.d = d
        self.omit_request_id = omit_request_id
        self.extends = extends

    def generate(self) -> str:
        template = get_template("response.tmpl")
        return template.render(this=self)

    @classmethod
    def from_dict(cls, name: str, d: Dict[str, Any]) -> ResponseType:
        omit_request_id = False
        if cls.OMIT_REQUEST_ID_KEY in d:
            omit_request_id = bool(d[cls.OMIT_REQUEST_ID_KEY])
            del d[cls.OMIT_REQUEST_ID_KEY]

        extends = None
        if cls.EXTENDS_KEY in d:
            extends = str(d[cls.EXTENDS_KEY])
            del d[cls.EXTENDS_KEY]

        return ResponseType(
            name=name, d=d, omit_request_id=omit_request_id, extends=extends
        )
