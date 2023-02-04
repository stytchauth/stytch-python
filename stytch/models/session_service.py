#!/usr/bin/env python3

from typing import Any, Dict, List, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class SessionsgetResponse(ResponseBase):
    request_id: str
    sessions: List[StytchSession]


class SessionsauthenticateResponse(ResponseBase):
    request_id: str
    session: Optional[StytchSession]
    session_token: str
    session_jwt: str
    user: User


class SessionsrevokeResponse(ResponseBase):
    request_id: str


class SessionsjwksResponse(ResponseBase):
    keys: List[Dict[str, Any]]
    request_id: str


class MultitenantsessionsjwksResponse(ResponseBase):
    keys: List[Dict[str, Any]]
    request_id: str
