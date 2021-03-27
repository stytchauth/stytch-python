import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="stytch",
    version="1.2.1",
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests>=2.7.0"],
)
