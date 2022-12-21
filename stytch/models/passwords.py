#!/usr/bin/env python3

from typing import Any, Dict, Optional

from stytch.core.models import ResponseBase, StytchSession, User


class CreateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-create)"""  # noqa

    user_id: str
    email_id: str


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-authenticate)"""  # noqa

    user_id: str
    user: User
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]


class StrengthCheckResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-strength-check)"""  # noqa

    valid_password: bool
    score: int
    breached_password: bool
    feedback: Dict[str, Any]


class MigrateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/password-migrate)"""  # noqa

    user_id: str
    email_id: str
    user_created: bool
