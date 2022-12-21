#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class SendResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/whatsapp-send)"""  # noqa

    user_id: str
    phone_id: str


class LoginOrCreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/whatsapp-login-or-create)"""  # noqa

    user_id: str
    phone_id: str
    user_created: bool
