#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class SendResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/send-otp-by-sms)"""  # noqa

    user_id: str
    phone_id: str


class LoginOrCreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/log-in-or-create-user-by-sms)"""  # noqa

    user_id: str
    phone_id: str
    user_created: bool
