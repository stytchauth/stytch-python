#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MagiclinkredirectResponse(ResponseBase):
    request_id: str
    redirect_url: str
    html_response_data: None


class MagiclinksredirectcaptchaResponse(ResponseBase):
    request_id: str
    redirect_url: str
