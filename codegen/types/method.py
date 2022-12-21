#!/usr/bin/env python3

from __future__ import annotations

import os
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from codegen.types.argument import Argument
from codegen.types.http_method import HttpMethod
from codegen.types.response_type import ResponseType
from codegen.types.templates import get_template

API_DOC_SUFFIX = ".md"
RESPONSE_DOC_SUFFIX = ".response.md"


class InvalidMethodSpecError(ValueError):
    pass


@dataclass
class Method:
    name: str
    api_path: Optional[str]
    args: List[Argument]
    response_type: Optional[ResponseType] = None
    method: Optional[HttpMethod] = None
    eval_api_path: bool = False
    manual_implementation: bool = False
    docstring: Optional[str] = None

    @property
    def params_or_json(self) -> str:
        if self.method is HttpMethod.GET:
            return "params"
        elif self.method is HttpMethod.DELETE:
            return "SHOULD_NEVER_BE_CALLED"
        return "json"

    @property
    def is_delete_method(self) -> bool:
        return self.method is HttpMethod.DELETE

    def get_docs_if_available(self, docs_dir: Optional[pathlib.Path]) -> None:
        if docs_dir is None:
            return

        api_docpath = (docs_dir / self.name).with_suffix(API_DOC_SUFFIX)
        response_docpath = api_docpath.with_suffix(RESPONSE_DOC_SUFFIX)

        if os.path.exists(api_docpath):
            with open(api_docpath) as f:
                self.docstring = f.read().strip()
        if self.response_type is not None and os.path.exists(response_docpath):
            with open(response_docpath) as f:
                self.response_type.docstring = f.read().strip()

    def generate(self) -> str:
        template = get_template("method.tmpl")
        return template.render(this=self)

    @classmethod
    def return_type_name(cls, name: str) -> str:
        name_to_title = "".join(part.title() for part in name.split("_"))
        return f"{name_to_title}Response"

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
        docstring: Optional[str] = None,
        response_docstring: Optional[str] = None,
    ) -> Method:
        name = data["name"]
        args = [Argument.from_dict(a) for a in data["args"]]
        response_type = None
        if "response_type" in data:
            response_type = ResponseType.from_dict(
                name=cls.return_type_name(name),
                d=data["response_type"],
                docstring=response_docstring,
            )

        api_path = name
        eval_api_path = data.get("eval_api_path", False)
        if "api_path" in data:
            api_path = data["api_path"]
        elif data.get("use_base_path_as_api_path", False):
            # We use None and set eval_api_path to True because
            # we'll call self.api_base.with_sub_url(self.sub_url, None)
            # which will omit the last part of the sub-route. This is
            # useful for create methods that route to their parent path
            # (passwords.create is POST /passwords, not /passwords/create).
            api_path = None
            eval_api_path = True

        manual_implementation = data.get("manual_implementation", False)
        http_method = data.get("method")

        if http_method is None and not manual_implementation:
            raise InvalidMethodSpecError(
                f"No http method for {name}, but manual_implementation=False"
            )

        if http_method is not None:
            http_method = HttpMethod.from_str(http_method)

        if response_type is None:
            if http_method is not HttpMethod.DELETE and not manual_implementation:
                raise InvalidMethodSpecError(
                    f"Can only omit response_type for {name} "
                    "if HttpMethod is DELETE or manual_implementation=True"
                )

        return cls(
            name=name,
            args=args,
            response_type=response_type,
            method=http_method,
            api_path=api_path,
            manual_implementation=manual_implementation,
            eval_api_path=eval_api_path,
            docstring=docstring,
        )
