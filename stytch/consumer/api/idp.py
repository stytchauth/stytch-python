from __future__ import annotations

from typing import Any, Dict, Optional

import jwt

from stytch.consumer.models.idp import AccessTokenJWTClaims, AccessTokenJWTResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.shared import jwt_helpers


class IDP:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
        jwks_client: jwt.PyJWKClient,
        project_id: str,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.jwks_client = jwks_client
        self.project_id = project_id

    # MANUAL(introspect_idp_access_token)(SERVICE_METHOD)
    # ADDIMPORT: from typing import Optional
    # ADDIMPORT: from stytch.b2b.models.idp import AccessTokenJWTResponse
    def introspect_idp_access_token(
        self,
        access_token: str,
        client_id: str,
        client_secret: Optional[str] = None,
        grant_type: str = "authorization_code",
        token_type_hint: str = "access_token",
    ) -> Optional[AccessTokenJWTClaims]:
        return self.introspect_idp_access_token_local(
            access_token, client_id
        ) or self.introspect_idp_access_token_network(
            access_token, client_id, client_secret, grant_type, token_type_hint
        )

    # ENDMANUAL(introspect_idp_access_token)

    # MANUAL(introspect_idp_access_token_network)(SERVICE_METHOD)
    # ADDIMPORT: from typing import Optional
    # ADDIMPORT: from stytch.b2b.models.idp import AccessTokenJWTClaims, AccessTokenJWTResponse
    # ADDIMPORT: from stytch.shared import jwt_helpers
    # ADDIMPORT: from stytch.shared import rbac_local
    def introspect_idp_access_token_network(
        self,
        access_token: str,
        client_id: str,
        client_secret: Optional[str] = None,
        grant_type: str = "authorization_code",
        token_type_hint: str = "access_token",
    ) -> Optional[AccessTokenJWTClaims]:
        headers: Dict[str, str] = {"Content-Type": "application/x-www-form-urlencoded"}
        data: Dict[str, Any] = {
            "token": access_token,
            "client_id": client_id,
            "grant_type": grant_type,
            "token_type_hint": token_type_hint,
        }
        if client_secret is not None:
            data["client_secret"] = client_secret

        url = self.api_base.url_for(
            f"/v1/public/{self.project_id}/oauth2/introspect", data
        )
        res = self.sync_client.postForm(url, data, headers)
        jwtResponse = AccessTokenJWTResponse.from_json(
            res.response.status_code, res.json
        )
        if not jwtResponse.active:
            return None
        return AccessTokenJWTClaims(
            subject=jwtResponse.sub, scopes=jwtResponse.scope, custom_claims={}
        )

    # ENDMANUAL(introspect_idp_access_token_network)

    # MANUAL(introspect_idp_access_token_local)(SERVICE_METHOD)
    # ADDIMPORT: from typing import Optional
    # ADDIMPORT: from stytch.b2b.models.sessions import AccessTokenJWTClaims
    # ADDIMPORT: from stytch.shared import jwt_helpers
    def introspect_idp_access_token_local(
        self,
        access_token: str,
        client_id: str,
    ) -> Optional[AccessTokenJWTClaims]:
        _scope_claim = "scope"
        generic_claims = jwt_helpers.authenticate_jwt_local(
            project_id=self.project_id,
            jwks_client=self.jwks_client,
            jwt=access_token,
            custom_audience=client_id,
            custom_issuer=f"https://stytch.com/{self.project_id}",
        )
        if generic_claims is None:
            return None

        custom_claims = {
            k: v for k, v in generic_claims.untyped_claims.items() if k != _scope_claim
        }

        return AccessTokenJWTClaims(
            subject=generic_claims.reserved_claims["sub"],
            scopes=generic_claims.untyped_claims[_scope_claim],
            custom_claims=custom_claims,
        )

    # ENDMANUAL(introspect_idp_access_token_local)
