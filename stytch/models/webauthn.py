#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession, User


class RegisterStartResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/webauthn-register-start)"""  # noqa

    user_id: str
    public_key_credential_creation_options: str


class RegisterResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/webauthn-register)"""  # noqa

    user_id: str
    webauthn_registration_id: str


class AuthenticateStartResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/webauthn-authenticate-start)"""  # noqa

    user_id: str
    public_key_credential_request_options: str


class AuthenticateResponse(ResponseBase):
    """[Stytch docs](https://stytch.com/docs/api/webauthn-authenticate)"""  # noqa

    user_id: str
    user: User
    webauthn_registration_id: str
    session_jwt: str
    session_token: str
    session: Optional[StytchSession]
