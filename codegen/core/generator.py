#!/usr/bin/env python3

import logging
import os
from typing import List

from codegen.types.api import Api


class Generator:
    def __init__(self, input_path: str) -> None:
        self.specs = self.get_yml_files(input_path)

    def generate_all(
        self, api_dir: str, models_dir: str, overwrite: bool = False
    ) -> None:
        for spec in self.specs:
            logging.info(f"Generating API from {spec}")
            api = Api.from_yml(spec)
            api.generate_all(
                api_dir=api_dir, models_dir=models_dir, overwrite=overwrite
            )

    @classmethod
    def get_yml_files(cls, input_path: str) -> List[str]:
        if os.path.isdir(input_path):
            return [
                os.path.join(input_path, fn)
                for fn in os.listdir(input_path)
                if fn.endswith(".yml")
            ]
        else:
            return [input_path]
