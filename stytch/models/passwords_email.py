#!/usr/bin/env python3


from stytch.models.common import ResponseBase


class ResetStartResponse(ResponseBase):
    user_id: str
    email_id: str


class ResetResponse(ResponseBase):
    user_id: str
