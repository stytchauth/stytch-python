#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

cd "$SCRIPT_DIR/.." || exit 1
env STYTCH_PYTHON_RUN_INTEGRATION_TESTS=1 coverage run -m unittest && coverage html --omit="*test/*"
