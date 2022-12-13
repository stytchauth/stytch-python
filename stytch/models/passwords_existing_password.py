#!/usr/bin/env python3


from stytch.models.common import (
    ResponseBase,
)


class ResetResponse(ResponseBase):
    status_code: int
    request_id: str
    user_id: str
