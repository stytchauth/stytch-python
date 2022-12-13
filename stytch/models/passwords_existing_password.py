#!/usr/bin/env python3


from stytch.models.common import ResponseBase


class ResetResponse(ResponseBase):
    user_id: str
