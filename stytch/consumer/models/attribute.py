# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Optional

import pydantic


class Attributes(pydantic.BaseModel):
    """
    Fields:
      - ip_address: The IP address of the user.
      - user_agent: The user agent of the User.
    """  # noqa

    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
