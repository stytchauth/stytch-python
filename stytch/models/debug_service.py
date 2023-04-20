#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class WhoamiResponse(ResponseBase):
    request_id: str
    project_id: str
    name: str
