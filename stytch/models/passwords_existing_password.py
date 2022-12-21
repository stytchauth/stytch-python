#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class ResetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-existing-password-reset)"""  # noqa

    user_id: str
