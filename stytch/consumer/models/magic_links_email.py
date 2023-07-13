# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum

from stytch.core.response_base import ResponseBase


class InviteRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class LoginOrCreateRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class SendRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class InviteResponse(ResponseBase):
    """Response type for `Email.invite`.
    Fields:
      - user_id: The unique ID of the affected User.
      - email_id: The unique ID of a specific email address.
    """  # noqa

    user_id: str
    email_id: str


class LoginOrCreateResponse(ResponseBase):
    """Response type for `Email.login_or_create`.
    Fields:
      - user_id: The unique ID of the affected User.
      - email_id: The unique ID of a specific email address.
      - user_created: In `login_or_create` endpoints, this field indicates whether or not a User was just created.
    """  # noqa

    user_id: str
    email_id: str
    user_created: bool


class RevokeInviteResponse(ResponseBase):
    """Response type for `Email.revoke_invite`.
    Fields:
    """  # noqa


class SendResponse(ResponseBase):
    """Response type for `Email.send`.
    Fields:
      - user_id: The unique ID of the affected User.
      - email_id: The unique ID of a specific email address.
    """  # noqa

    user_id: str
    email_id: str
