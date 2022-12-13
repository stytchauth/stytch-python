#!/usr/bin/env python3


from stytch.models.common import (
    ResponseBase,
)


class SendResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str


class LoginOrCreateResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
    email_id: str
    user_created: bool
