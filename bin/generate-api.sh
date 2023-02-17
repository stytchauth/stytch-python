#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

cd "$SCRIPT_DIR/.." || exit 1
python -m codegen.generate codegen/specs/stytch/ stytch/api stytch/models --docs_dir=codegen/specs/stytch/docs
python -m codegen.generate codegen/specs/stytch_b2b/ stytch/b2b/api stytch/b2b/models --docs_dir=codegen/specs/stytch_b2b/docs
