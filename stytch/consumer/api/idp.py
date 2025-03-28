from __future__ import annotations

from typing import Any, Dict, Optional

import jwt

from stytch.consumer.models.idp import IDPTokenClaims, IDPTokenResponse
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
        self.non_custom_claim_keys = [
            "aud",
            "exp",
            "iat",
            "iss",
            "jti",
            "nbf",
            "sub",
            "active",
            "client_id",
            "request_id",
            "scope",
            "status_code",
            "token_type",
        ]

    def introspect_token_network(
        self,
        token: str,
        client_id: str,
        client_secret: Optional[str] = None,
        token_type_hint: str = "access_token",
    ) -> Optional[IDPTokenClaims]:
        """Introspects a token JWT from an authorization code response.
        Access tokens are JWTs signed with the project's JWKs. Refresh tokens are opaque tokens.
        Access tokens contain a standard set of claims as well as any custom claims generated from templates.

        Fields:
          - token: The access token (or refresh token) to introspect.
          - client_id: The ID of the client.
          - client_secret: The secret of the client.
          - token_type_hint: A hint on what the token contains. Valid fields are 'access_token' and 'refresh_token'.
        """
        headers: Dict[str, str] = {"Content-Type": "application/x-www-form-urlencoded"}
        data: Dict[str, Any] = {
            "token": token,
            "client_id": client_id,
            "token_type_hint": token_type_hint,
        }
        if client_secret is not None:
            data["client_secret"] = client_secret

        url = self.api_base.url_for(
            f"/v1/public/{self.project_id}/oauth2/introspect", data
        )
        res = self.sync_client.post_form(url, data, headers)
        jwtResponse = IDPTokenResponse.from_json(res.response.status_code, res.json)
        custom_claims = {
            k: v for k, v in res.json.items() if k not in self.non_custom_claim_keys
        }
        if not jwtResponse.active:
            return None

        return IDPTokenClaims(
            subject=jwtResponse.sub,
            scope=jwtResponse.scope,
            audience=jwtResponse.aud,
            expires_at=jwtResponse.exp,
            issued_at=jwtResponse.iat,
            issuer=jwtResponse.iss,
            not_before=jwtResponse.nbf,
            token_type=jwtResponse.token_type,
            custom_claims=custom_claims,
        )

    async def introspect_token_network_async(
        self,
        token: str,
        client_id: str,
        client_secret: Optional[str] = None,
        token_type_hint: str = "access_token",
    ) -> Optional[IDPTokenClaims]:
        """Introspects a token JWT from an authorization code response.
        Access tokens are JWTs signed with the project's JWKs. Refresh tokens are opaque tokens.
        Access tokens contain a standard set of claims as well as any custom claims generated from templates.

        Fields:
          - token: The access token (or refresh token) to introspect.
          - client_id: The ID of the client.
          - client_secret: The secret of the client.
          - token_type_hint: A hint on what the token contains. Valid fields are 'access_token' and 'refresh_token'.
        """
        headers: Dict[str, str] = {"Content-Type": "application/x-www-form-urlencoded"}
        data: Dict[str, Any] = {
            "token": token,
            "client_id": client_id,
            "token_type_hint": token_type_hint,
        }
        if client_secret is not None:
            data["client_secret"] = client_secret

        url = self.api_base.url_for(
            f"/v1/public/{self.project_id}/oauth2/introspect", data
        )
        res = await self.async_client.post_form(url, data, headers)
        jwtResponse = IDPTokenResponse.from_json(res.response.status, res.json)
        custom_claims = {
            k: v for k, v in res.json.items() if k not in self.non_custom_claim_keys
        }
        if not jwtResponse.active:
            return None

        return IDPTokenClaims(
            subject=jwtResponse.sub,
            scope=jwtResponse.scope,
            audience=jwtResponse.aud,
            expires_at=jwtResponse.exp,
            issued_at=jwtResponse.iat,
            issuer=jwtResponse.iss,
            not_before=jwtResponse.nbf,
            token_type=jwtResponse.token_type,
            custom_claims=custom_claims,
        )

    def introspect_access_token_local(
        self,
        access_token: str,
    ) -> Optional[IDPTokenClaims]:
        """Introspects a token JWT from an authorization code response.
        Access tokens are JWTs signed with the project's JWKs. Refresh tokens are opaque tokens.
        Access tokens contain a standard set of claims as well as any custom claims generated from templates.

        Fields:
          - access_token: The access token (or refresh token) to introspect.
          - client_id: The ID of the client.
        """
        _scope_claim = "scope"
        generic_claims = jwt_helpers.authenticate_jwt_local(
            project_id=self.project_id,
            jwks_client=self.jwks_client,
            jwt=access_token,
        )
        if generic_claims is None:
            return None

        custom_claims = {
            k: v for k, v in generic_claims.untyped_claims.items() if k != _scope_claim
        }

        return IDPTokenClaims(
            subject=generic_claims.reserved_claims["sub"],
            scope=generic_claims.untyped_claims[_scope_claim],
            custom_claims=custom_claims,
            audience=generic_claims.reserved_claims["aud"],
            expires_at=generic_claims.reserved_claims["exp"],
            issued_at=generic_claims.reserved_claims["iat"],
            issuer=generic_claims.reserved_claims["iss"],
            not_before=generic_claims.reserved_claims["nbf"],
            token_type="access_token",
        )
