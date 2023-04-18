#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class PasswordsstrengthcheckResponse(ResponseBase):
    request_id: str
    valid_password: bool
    score: None
    breached_password: bool
    feedback: None
    strength_policy: str
    breach_detection_on_create: bool
