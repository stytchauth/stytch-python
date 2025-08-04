#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional

import pydantic

from stytch.core.response_base import ResponseBase


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
    
    Currently no additional options are supported, but this follows the library pattern
    for potential future expansion.
    """
    pass


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