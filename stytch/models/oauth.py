#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class AuthenticateResponse(ResponseBase):
    user_id: str
    user: Optional[User]
    oauth_user_registration_id: str
    provider_subject: str
    provider_type: str
    provider_values: Optional[Dict[str, Any]]
    reset_sessions: bool
    session: Optional[StytchSession]
    session_jwt: str
    session_token: str


class AttachResponse(ResponseBase):
    oauth_attach_token: str
