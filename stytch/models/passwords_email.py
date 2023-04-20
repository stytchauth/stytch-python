#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class PasswordssessionresetResponse(ResponseBase):
    request_id: str
    user_id: str
    session: Optional[StytchSession]
    user: User
