#!/usr/bin/env python3


from stytch.models.common import ResponseBase


class SendResponse(ResponseBase):
    user_id: str
    email_id: str


class LoginOrCreateResponse(ResponseBase):
    user_id: str
    email_id: str
    user_created: bool
