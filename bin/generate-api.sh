#!/usr/bin/env bash

SCRIPT_DIR=`echo "$0" | sed 's|[^/]*$||'`

cd "$SCRIPT_DIR/.." || exit 1

python3 -m codegen.generate codegen/specs/stytch/ stytch/api stytch/models --docs_dir=codegen/specs/stytch/docs
python3 -m codegen.generate codegen/specs/stytch_b2b/ stytch/b2b/api stytch/b2b/models --docs_dir=codegen/specs/stytch_b2b/docs
