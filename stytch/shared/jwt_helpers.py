from __future__ import annotations

import time
from typing import Any, Dict, Optional

import jwt as pyjwt
import pydantic


class GenericClaims(pydantic.BaseModel):
    reserved_claims: Dict[str, Any]
    untyped_claims: Dict[str, Any]


def authenticate_jwt_local(
    *,
    jwks_client: pyjwt.PyJWKClient,
    project_id: str,
    jwt: str,
    max_token_age_seconds: Optional[int] = None,
    leeway: int = 0,
) -> Optional[GenericClaims]:
    """Parse a JWT and verify the signature locally
    (without calling /authenticate in the API).

    If max_token_age_seconds is set, this will return an error if the JWT was issued
    (based on the "iat" claim) more than maxTokenAge seconds ago.

    If max_token_age_seconds is explicitly set to zero, all tokens will be
    considered too old, even if they are otherwise valid.

    The value for leeway is the maximum allowable difference in seconds when
    comparing timestamps. It defaults to zero.
    """
    jwt_audience = project_id
    jwt_issuer = f"stytch.com/{project_id}"

    now = time.time()

    signing_key = jwks_client.get_signing_key_from_jwt(jwt)

    try:
        # NOTE: The max_token_age_seconds value is applied after decoding.
        payload = pyjwt.decode(
            jwt,
            signing_key.key,
            algorithms=["RS256"],
            options={
                "require": ["aud", "iss", "exp", "iat", "nbf"],
                "verify_signature": True,
                "verify_aud": True,
                "verify_iss": True,
                "verify_exp": True,
                "verify_iat": True,
                "verify_nbf": True,
            },
            audience=jwt_audience,
            issuer=jwt_issuer,
            leeway=leeway,
        )
    except Exception:
        # In the event of a failure to decode, such as an expired token, we should return None
        return None

    if max_token_age_seconds is not None:
        iat = payload["iat"]
        if now - iat >= max_token_age_seconds:
            # JWT was issued too long ago, don't verify
            return None

    # Parse custom claims by taking everything other than the reserved claims
    reserved_claim_keys = [
        "aud",
        "exp",
        "iat",
        "iss",
        "jti",
        "nbf",
        "sub",
    ]
    untyped_claims = {k: v for k, v in payload.items() if k not in reserved_claim_keys}
    reserved_claims = {k: v for k, v in payload.items() if k in reserved_claim_keys}

    return GenericClaims(reserved_claims=reserved_claims, untyped_claims=untyped_claims)
