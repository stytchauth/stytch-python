#!/usr/bin/env python3


from stytch.models.common import ResponseBase


class ResetStartResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str


class ResetResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
