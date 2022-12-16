#!/usr/bin/env python3

import pathlib
import re

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

with open("stytch/version.py", "r") as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    assert match is not None
    version = match.group(1)

if not version:
    raise RuntimeError("Cannot find version information")

# This call to setup() does all the work
setup(
    name="stytch",
    version=version,
    description="Stytch python client",
    long_description=README,
    long_description_content_type="text/markdown",
    download_url="https://github.com/stytchauth/stytch-python",
    keywords=[
        "stytch",
        "user",
        "authentication",
    ],
    author="Stytch",
    author_email="hello@stytch.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    packages=find_packages(
        include=["stytch*"],
        exclude=["*.test", "*.tests", "*.test.*", "*.tests.*"],
    ),
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.8.3",
        "requests>=2.7.0",
        "pydantic>=1.10.2",
        "pyjwt[crypto]>=2.4.0",
    ],
)
