#!/usr/bin/env python3

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from codegen.types.argument import Argument
from codegen.types.http_method import HttpMethod
from codegen.types.templates import get_template


@dataclass
class Method:
    name: str
    api_path: str
    args: List[Argument]
    method: Optional[HttpMethod] = None
    eval_api_path: bool = False
    manual_implementation: bool = False

    @property
    def params_or_data(self) -> str:
        if self.method is HttpMethod.GET:
            return "params"
        return "data"

    @property
    def is_delete_method(self) -> bool:
        return self.method is HttpMethod.DELETE

    def generate(self) -> str:
        template = get_template("method.tmpl")
        return template.render(this=self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Method:
        name = data["name"]
        args = [Argument.from_dict(a) for a in data["args"]]
        api_path = data.get("api_path", name)
        manual_implementation = data.get("manual_implementation", False)
        eval_api_path = data.get("eval_api_path", False)
        http_method = data.get("method")

        if http_method is None and not manual_implementation:
            logging.critical(
                f"No http method for {name}, but manual_implementation=False"
            )
            sys.exit(1)

        if http_method is not None:
            http_method = HttpMethod.from_str(http_method)

        return cls(
            name=name,
            args=args,
            method=http_method,
            api_path=api_path,
            manual_implementation=manual_implementation,
            eval_api_path=eval_api_path,
        )
