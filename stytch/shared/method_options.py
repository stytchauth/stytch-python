from typing import Dict, Optional

import pydantic


class Authorization(pydantic.BaseModel):
    # A secret token for a given Stytch Session.
    session_token: Optional[str] = None
    # The JSON Web Token (JWT) for a given Stytch Session.
    session_jwt: Optional[str] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.session_token:
            headers["X-Stytch-Member-Session"] = self.session_token
        if self.session_jwt:
            headers["X-Stytch-Member-SessionJWT"] = self.session_jwt
        return headers
