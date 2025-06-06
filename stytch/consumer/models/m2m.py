# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Any, Dict, List, Optional

import pydantic

from stytch.core.response_base import ResponseBase


class M2MSearchQueryOperator(str, enum.Enum):
    OR = "OR"
    AND = "AND"


class M2MClient(pydantic.BaseModel):
    """
    Fields:
      - client_id: The ID of the client.
      - client_name: A human-readable name for the client.
      - client_description: A human-readable description for the client.
      - status: The status of the client - either `active` or `inactive`.
      - scopes: An array of scopes assigned to the client.
      - client_secret_last_four: The last four characters of the client secret.
      - trusted_metadata: An arbitrary JSON object for storing application-specific data.
      - next_client_secret_last_four: The last four characters of the `next_client_secret`. Null if no `next_client_secret` exists.
    """  # noqa

    client_id: str
    client_name: str
    client_description: str
    status: str
    scopes: List[str]
    client_secret_last_four: str
    trusted_metadata: Optional[Dict[str, Any]] = None
    next_client_secret_last_four: Optional[str] = None


class M2MClientWithClientSecret(pydantic.BaseModel):
    """
    Fields:
      - client_id: The ID of the client.
      - client_secret: The secret of the client. **Important:** this is the only time you will be able to view the `client_secret`. Be sure to persist the `client_secret` in a secure location. If the `client_secret` is lost, you will need to trigger a secret rotation flow to receive another one.
      - client_name: A human-readable name for the client.
      - client_description: A human-readable description for the client.
      - status: The status of the client - either `active` or `inactive`.
      - scopes: An array of scopes assigned to the client.
      - client_secret_last_four: The last four characters of the client secret.
      - trusted_metadata: An arbitrary JSON object for storing application-specific data.
      - next_client_secret_last_four: The last four characters of the `next_client_secret`. Null if no `next_client_secret` exists.
    """  # noqa

    client_id: str
    client_secret: str
    client_name: str
    client_description: str
    status: str
    scopes: List[str]
    client_secret_last_four: str
    trusted_metadata: Optional[Dict[str, Any]] = None
    next_client_secret_last_four: Optional[str] = None


class M2MClientWithNextClientSecret(pydantic.BaseModel):
    """
    Fields:
      - client_id: The ID of the client.
      - next_client_secret: The newly created secret that's next in rotation for the client. **Important:** this is the only time you will be able to view the `next_client_secret`. Be sure to persist the `next_client_secret` in a secure location. If the `next_client_secret` is lost, you will need to trigger a secret rotation flow to receive another one.
      - client_name: A human-readable name for the client.
      - client_description: A human-readable description for the client.
      - status: The status of the client - either `active` or `inactive`.
      - scopes: An array of scopes assigned to the client.
      - client_secret_last_four: The last four characters of the client secret.
      - trusted_metadata: An arbitrary JSON object for storing application-specific data.
      - next_client_secret_last_four: The last four characters of the `next_client_secret`. Null if no `next_client_secret` exists.
    """  # noqa

    client_id: str
    next_client_secret: str
    client_name: str
    client_description: str
    status: str
    scopes: List[str]
    client_secret_last_four: str
    trusted_metadata: Optional[Dict[str, Any]] = None
    next_client_secret_last_four: Optional[str] = None


class M2MSearchQuery(pydantic.BaseModel):
    """
    Fields:
      - operator: The action to perform on the operands. The accepted value are:

      `AND` – all the operand values provided must match.

      `OR` – the operator will return any matches to at least one of the operand values you supply.
      - operands: An array of operand objects that contains all of the filters and values to apply to your search search query.
    """  # noqa

    operator: M2MSearchQueryOperator
    operands: List[Dict[str, Any]]


class ResultsMetadata(pydantic.BaseModel):
    """
    Fields:
      - total: The total number of results returned by your search query. If totals have been disabled for your Stytch Workspace to improve search performance, the value will always be -1.
      - next_cursor: The `next_cursor` string is returned when your search result contains more than one page of results. This value is passed into your next search call in the `cursor` field.
    """  # noqa

    total: int
    next_cursor: Optional[str] = None


# MANUAL(GetTokenResponse)(TYPES)
# ADDIMPORT: from stytch.core.response_base import ResponseBase
class GetTokenResponse(ResponseBase):
    """Response type for `M2M.token`.
    Fields:
      - access_token: The access token granted to the client. Access tokens are JWTs signed with the project's JWKs.
      - token_type: The type of the returned access token. Today, this value will always be equal to "bearer"
      - expires_in: The lifetime in seconds of the access token. For example, the value 3600 denotes that the access token will expire in one hour from the time the response was generated.
    """  # noqa

    access_token: str
    token_type: str
    expires_in: int


# ENDMANUAL(GetTokenResponse)


# MANUAL(M2MJWTClaims)(TYPES)
# ADDIMPORT: from typing import Any, Dict, List, Optional
class M2MJWTClaims(pydantic.BaseModel):
    """Response type for `Sessions.authenticate_m2m_jwt_local`.
    Fields:
      - client_id: The subject (client_id) that the JWT is intended for.
      - scopes: A list of scopes granted, separated by spaces.
      - custom_claims: A dict of custom claims of the JWT.
    """  # noqa

    client_id: str
    scopes: List[str]
    custom_claims: Optional[Dict[str, Any]] = None


# ENDMANUAL(M2MJWTClaims)
