from typing import Any, Dict, List, Optional

import pydantic

from stytch.core.response_base import ResponseBase


class AccessTokenJWTResponse(ResponseBase):
    """Response type for `IDP.introspect_idp_access_token`.
    Fields:
      - active: Whether or not this token is active.
      - sub: Subject of this JWT.
      - scope: A space-delimited string of scopes this JWT is granted.
      - aud: Audience of this JWT. Usually the user or member ID, and any custom audience, if present.
      - exp: Expiration of this access token, in Unix time.
      - iat: The time this access token was issued.
      - iss: The issuer of this access token.
      - nbf: The time before which the JWT must not be accepted for processing.
    """  # noqa

    active: bool
    sub: Optional[str] = None
    scope: Optional[str] = None
    aud: Optional[List[str]] = []
    exp: Optional[int] = None
    iat: Optional[int] = None
    iss: Optional[str] = None
    nbf: Optional[int] = None


class AccessTokenJWTClaims(pydantic.BaseModel):
    """Response type for `IDP.introspect_idp_access_token`.
    Fields:
      - subject: The subject (either user_id or member_id) that the JWT is intended for.
      - scope: A space-delimited string of scopes this JWT is granted.
      - custom_claims: A dict of custom claims of the JWT.
      - audience: Audience of this JWT. Usually the user or member ID, and any custom audience, if present.
      - expires_at: Expiration of this access token, in Unix time.
      - issued_at: The time this access token was issued.
      - issuer: The issuer of this access token.
      - not_before: The time before which the JWT must not be accepted for processing.
    """  # noqa

    subject: str
    scope: Optional[str]
    custom_claims: Optional[Dict[str, Any]] = None
    audience: Optional[List[str]]
    expires_at: Optional[int]
    issued_at: Optional[int]
    issuer: Optional[str]
    not_before: Optional[int]
