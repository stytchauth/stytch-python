#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class ResetStartResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-email-reset-start)"""  # noqa

    user_id: str
    email_id: str


class ResetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-email-reset)"""  # noqa

    user_id: str
