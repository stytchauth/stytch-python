#!/usr/bin/env python3

from typing import Optional

from stytch.models.common import ResponseBase, StytchSession


class ResetResponse(ResponseBase):
    user_id: str
    session: Optional[StytchSession]
