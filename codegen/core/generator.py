#!/usr/bin/env python3

import logging
import os
import subprocess
from typing import List

from codegen.types.api import Api


class Generator:
    def __init__(
        self, input_path: str, api_dir: str, models_dir: str, overwrite: bool = False
    ) -> None:
        self.specs = self.get_yml_files(input_path)
        self.api_dir = api_dir
        self.models_dir = models_dir
        self.overwrite = overwrite

    def generate_all(self) -> None:
        for spec in self.specs:
            logging.info(f"Generating API from {spec}")
            api = Api.from_yml(spec)
            api.generate_all(
                api_dir=self.api_dir,
                models_dir=self.models_dir,
                overwrite=self.overwrite,
            )

    def run_formatters(self) -> None:
        logging.debug("Running next formatter => autoflake")
        subprocess.Popen(
            [
                "autoflake",
                "--in-place",
                "--remove-all-unused-imports",
                "-r",
                self.api_dir,
            ]
        ).wait()
        subprocess.Popen(
            [
                "autoflake",
                "--in-place",
                "--remove-all-unused-imports",
                "-r",
                self.models_dir,
            ]
        ).wait()

        logging.debug("Running next formatter => isort")
        subprocess.Popen(["isort", "--profile", "black", self.api_dir]).wait()
        subprocess.Popen(["isort", "--profile", "black", self.models_dir]).wait()

        logging.debug("Running next formatter => black")
        subprocess.Popen(["black", self.api_dir]).wait()
        subprocess.Popen(["black", self.models_dir]).wait()

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
