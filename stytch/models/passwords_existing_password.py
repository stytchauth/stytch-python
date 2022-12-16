#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class ResetResponse(ResponseBase):
    user_id: str
