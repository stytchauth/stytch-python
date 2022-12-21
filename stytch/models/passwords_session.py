#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession


class ResetResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-session-reset)"""  # noqa

    user_id: str
    session: Optional[StytchSession]
