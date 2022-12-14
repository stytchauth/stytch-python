#!/usr/bin/env python3

from __future__ import annotations

import logging
import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import yaml

from codegen.core.snippet_set import SnippetSet
from codegen.types.method import Method
from codegen.types.templates import get_template


@dataclass
class Api:
    classname: str
    filename: str
    sub_url: str
    methods: List[Method]
    sub_apis: Optional[List[Api]]
    additional_imports: List[str]

    def generate_all(
        self,
        api_dir: str,
        models_dir: str,
        overwrite: bool = False,
        api_path_in_gen: Optional[str] = None,
        models_path_in_gen: Optional[str] = None,
    ) -> None:
        if api_path_in_gen is None:
            api_path_in_gen = api_dir.replace("/", ".")
        if models_path_in_gen is None:
            models_path_in_gen = models_dir.replace("/", ".")

        filename = self.filename + ".py"
        filepath = os.path.join(api_dir, filename)
        file_exists = os.path.exists(filepath)

        snippets = SnippetSet()
        if file_exists and not overwrite:
            snippets = SnippetSet.from_file(filepath)
            logging.debug(f"Found {len(snippets)} snippets")

        with open(filepath, "w") as f:
            f.write(self.generate(snippets, api_path_in_gen, models_path_in_gen))

        model_filepath = os.path.join(models_dir, filename)
        with open(model_filepath, "w") as f:
            f.write(self.generate_responses())

        # Recurse!
        sub_apis = self.sub_apis or []
        logging.debug(f"{self.classname} will generate {len(sub_apis)} sub-APIs")
        for sub_api in sub_apis:
            logging.debug(
                f"Generating sub-API {sub_api.classname} for {self.classname}"
            )
            sub_api.generate_all(
                api_dir=api_dir,
                models_dir=models_dir,
                overwrite=overwrite,
                api_path_in_gen=api_path_in_gen,
                models_path_in_gen=models_path_in_gen,
            )

    def generate(
        self, snippets: SnippetSet, api_path_in_gen: str, models_path_in_gen: str
    ) -> str:
        template = get_template("api.tmpl")
        res = template.render(
            this=self,
            api_path_in_gen=api_path_in_gen,
            models_path_in_gen=models_path_in_gen,
        )
        return snippets.replace_all(res)

    def generate_responses(self) -> str:
        template = get_template("api_responses.tmpl")
        return template.render(this=self)

    @property
    def filename_base(self) -> str:
        return self.filename.split(".")[-1]

    @classmethod
    def _gen_filename_from_classname(cls, classname: str) -> str:
        # https://stackoverflow.com/a/1176023
        filename = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", classname)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", filename).lower()

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Api:
        classname = data["classname"]
        methods = [Method.from_dict(m) for m in data["methods"]]
        sub_apis = [cls.from_dict(d) for d in data.get("sub_apis", [])]
        additional_imports = data.get("additional_imports", [])

        # Default to the class name converted to snake_case if none was given
        filename = data.get("filename")
        if filename is None:
            filename = cls._gen_filename_from_classname(data["classname"])

        # Default to self.filename if sub_url was not given
        sub_url = data.get("sub_url", filename)

        return cls(
            classname=classname,
            filename=filename,
            methods=methods,
            sub_apis=sub_apis,
            sub_url=sub_url,
            additional_imports=additional_imports,
        )

    @classmethod
    def from_yml(cls, filepath: str) -> Api:
        with open(filepath) as f:
            data = yaml.safe_load(f)
            return cls.from_dict(data)
