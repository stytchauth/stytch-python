from typing import Any, List, Dict, Optional

import pydantic

from stytch.core.response_base import ResponseBase

class AccessTokenJWTResponse(ResponseBase):
    """Response type for `Sessions.introspect_idp_access_token`.
    Fields:
      - active: Whether or not this token is active.
      - sub: Subject of this JWT.
      - scope: A space-delimited string of scopes this JWT is granted.
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
    """Response type for `Sessions.introspect_idp_access_token`.
    Fields:
      - subject: The subject (either user_id or member_id) that the JWT is intended for.
      - scope: A space-delimited string of scopes this JWT is granted.
      - custom_claims: A dict of custom claims of the JWT.
    """  # noqa

    subject: str
    scope: Optional[str]
    custom_claims: Optional[Dict[str, Any]] = None
    audience: Optional[List[str]]
    expires_at: Optional[int]
    issued_at: Optional[int]
    issuer: Optional[str]
    not_before: Optional[int]
