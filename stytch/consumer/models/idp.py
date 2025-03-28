from typing import Any, Dict, List, Optional

import pydantic

from stytch.core.response_base import ResponseBase


class IDPTokenResponse(ResponseBase):
    """Response type for `IDP.introspect_token_network`.
    Fields:
      - active: Whether or not this token is active.
      - sub: Subject of this token.
      - scope: A space-delimited string of scopes this token is granted.
      - aud: Audience of this token. Usually the user or member ID, and any custom audience, if present.
      - exp: Expiration of this access token, in Unix time.
      - iat: The time this access token was issued.
      - iss: The issuer of this access token.
      - nbf: The time before which the token must not be accepted for processing.
      - token_type: The type of token. Possible values are `access_token` and `refresh_token`.
    """  # noqa

    active: bool
    sub: Optional[str] = None
    scope: Optional[str] = None
    aud: Optional[List[str]] = []
    exp: Optional[int] = None
    iat: Optional[int] = None
    iss: Optional[str] = None
    nbf: Optional[int] = None
    token_type: Optional[str] = None


class IDPTokenClaims(pydantic.BaseModel):
    """Response type for `IDP.introspect_token_network`.
    Fields:
      - subject: The subject (either user_id or member_id) that the token is intended for.
      - scope: A space-delimited string of scopes this token is granted.
      - custom_claims: A dict of custom claims of the token.
      - audience: Audience of this token. Usually the user or member ID, and any custom audience, if present.
      - expires_at: Expiration of this access token, in Unix time.
      - issued_at: The time this access token was issued.
      - issuer: The issuer of this access token.
      - not_before: The time before which the token must not be accepted for processing.
      - token_type: The type of this token - e.g. 'access_token' or 'refresh_token'.
    """  # noqa

    subject: str
    scope: Optional[str]
    custom_claims: Optional[Dict[str, Any]] = None
    audience: Optional[List[str]]
    expires_at: Optional[int]
    issued_at: Optional[int]
    issuer: Optional[str]
    not_before: Optional[int]
    token_type: Optional[str]
    organization_claim: Optional[Dict[str, Any]] = None
