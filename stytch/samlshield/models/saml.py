#!/usr/bin/env python3

from __future__ import annotations

from typing import Dict, Optional

import pydantic

from stytch.core.response_base import ResponseBase
from stytch.shared.method_options import Authorization


class SamlValidateRequest(pydantic.BaseModel):
    """
    Request type for `samlshield.saml.validate`.

    Fields:
        saml_response: The SAML response to validate. This should be the base64 encoded
                      SAML response from the IdP and not the raw XML.
    """

    saml_response: str


class SamlValidateRequestOptions(pydantic.BaseModel):
    """
    Request options for `samlshield.saml.validate`.

    Fields:
      - authorization: Optional authorization object.
    """

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class SamlValidateResponse(ResponseBase):
    """
    Response type for `samlshield.saml.validate`.

    Inherits from ResponseBase which provides:
        status_code: The HTTP status code of the response
        request_id: Globally unique UUID that is returned with every API call

    Fields:
        message: The validation result message (only present on success)
    """

    message: Optional[str] = None
