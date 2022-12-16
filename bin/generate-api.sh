#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

cd "$SCRIPT_DIR/.." || exit 1
python -m codegen.generate codegen/specs/stytch/ stytch/api stytch/models
