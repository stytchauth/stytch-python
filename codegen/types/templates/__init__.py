#!/usr/bin/env python3

import os

from jinja2 import Environment, FileSystemLoader, Template


def get_template(name: str) -> Template:
    env = Environment(
        loader=FileSystemLoader(os.path.dirname(__file__)),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template(name)
