#!/usr/bin/env python3

from typing import Any, Dict, List

from stytch.core.models import ResponseBase


class MultitenantsessionsjwksResponse(ResponseBase):
    keys: List[Dict[str, Any]]
    request_id: str
