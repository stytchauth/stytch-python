#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class SendResponse(ResponseBase):
    user_id: str
    email_id: str


class LoginOrCreateResponse(ResponseBase):
    user_id: str
    email_id: str
    user_created: bool


class InviteResponse(ResponseBase):
    user_id: str
    email_id: str


class RevokeInviteResponse(ResponseBase):
    pass
