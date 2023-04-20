#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class PasswordsstrengthcheckResponse(ResponseBase):
    request_id: str
    valid_password: bool
    score: TODO
    breached_password: bool
    feedback: TODO
    strength_policy: str
    breach_detection_on_create: bool
