from typing import Any, Dict, Optional

import pydantic

from stytch.core.response_base import ResponseBase


# MANUAL(AccessTokenJWTResponse)(TYPES)
# ADDIMPORT: from typing import Any, Dict, List, Optional
# ADDIMPORT: import pydantic
class AccessTokenJWTResponse(ResponseBase):
    """Response type for `Sessions.introspect_idp_access_token`.
    Fields:
      - active: Whether or not this token is active.
      - sub: Subject of this JWT.
      - scope: Scopes that this JWT is granted.
    """  # noqa

    active: bool
    sub: Optional[str] = None
    scope: Optional[str] = None


# ENDMANUAL(AccessTokenJWTResponse)


# MANUAL(AccessTokenJWTClaims)(TYPES)
# ADDIMPORT: from typing import Any, Dict, List, Optional
# ADDIMPORT: import pydantic
class AccessTokenJWTClaims(pydantic.BaseModel):
    """Response type for `Sessions.introspect_idp_access_token`.
    Fields:
      - subject: The subject (either user_id or member_id) that the JWT is intended for.
      - scopes: A list of scopes granted, separated by spaces.
      - custom_claims: A dict of custom claims of the JWT.
    """  # noqa

    subject: str
    scopes: Optional[str]
    custom_claims: Optional[Dict[str, Any]] = None


# ENDMANUAL(AccessTokenJWTClaims)
