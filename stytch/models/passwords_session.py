#!/usr/bin/env python3

from typing import Optional

from stytch.models.common import ResponseBase, StytchSession


class ResetResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    session: Optional[StytchSession]
