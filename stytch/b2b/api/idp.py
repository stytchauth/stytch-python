from __future__ import annotations

from typing import Any, Dict, Optional

import jwt

from stytch.b2b.models.sessions import AuthorizationCheck
from stytch.consumer.models.idp import IDPTokenClaims, IDPTokenResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.shared import jwt_helpers, rbac_local
from stytch.shared.policy_cache import PolicyCache


class IDP:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
        jwks_client: jwt.PyJWKClient,
        project_id: str,
        policy_cache: PolicyCache,
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
            "https://stytch.com/organization",
        ]
        self.policy_cache = policy_cache

    def introspect_token_network(
        self,
        token: str,
        client_id: str,
        client_secret: Optional[str] = None,
        token_type_hint: str = "access_token",
        authorization_check: Optional[AuthorizationCheck] = None,
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
        if not jwtResponse.active:
            return None
        custom_claims = {
            k: v for k, v in res.json.items() if k not in self.non_custom_claim_keys
        }
        organization_claim = res.json["https://stytch.com/organization"]
        organization_id = organization_claim["organization_id"]
        scope = jwtResponse.scope

        if authorization_check is not None:
            rbac_local.perform_scope_authorization_check(
                policy=self.policy_cache.get(),
                token_scopes=scope.split(),
                authorization_check=authorization_check,
                subject_org_id=organization_id,
            )

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
            organization_claim=organization_claim,
        )

    async def introspect_token_network_async(
        self,
        token: str,
        client_id: str,
        client_secret: Optional[str] = None,
        token_type_hint: str = "access_token",
        authorization_check: Optional[AuthorizationCheck] = None,
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
        if not jwtResponse.active:
            return None
        custom_claims = {
            k: v for k, v in res.json.items() if k not in self.non_custom_claim_keys
        }
        organization_claim = res.json["https://stytch.com/organization"]
        organization_id = organization_claim["organization_id"]
        scope = jwtResponse.scope

        if authorization_check is not None:
            rbac_local.perform_scope_authorization_check(
                policy=self.policy_cache.get(),
                token_scopes=scope.split(),
                authorization_check=authorization_check,
                subject_org_id=organization_id,
            )

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
            organization_claim=organization_claim,
        )

    def introspect_access_token_local(
        self,
        access_token: str,
        authorization_check: Optional[AuthorizationCheck] = None,
    ) -> Optional[IDPTokenClaims]:
        """Introspects a token JWT from an authorization code response.
        Access tokens are JWTs signed with the project's JWKs. Refresh tokens are opaque tokens.
        Access tokens contain a standard set of claims as well as any custom claims generated from templates.

        Fields:
          - access_token: The access token (or refresh token) to introspect.
          - client_id: The ID of the client.
        """
        _scope_claim = "scope"
        _organization_claim = "https://stytch.com/organization"
        generic_claims = jwt_helpers.authenticate_jwt_local(
            project_id=self.project_id,
            jwks_client=self.jwks_client,
            jwt=access_token,
        )
        if generic_claims is None:
            return None

        custom_claims = {
            k: v
            for k, v in generic_claims.untyped_claims.items()
            if k not in [_scope_claim, _organization_claim]
        }

        scope = generic_claims.untyped_claims[_scope_claim]
        org_claim = generic_claims.untyped_claims[_organization_claim]

        if authorization_check is not None:
            rbac_local.perform_scope_authorization_check(
                policy=self.policy_cache.get(),
                token_scopes=scope.split(),
                authorization_check=authorization_check,
                subject_org_id=org_claim["organization_id"],
            )

        return IDPTokenClaims(
            subject=generic_claims.reserved_claims["sub"],
            scope=scope,
            custom_claims=custom_claims,
            audience=generic_claims.reserved_claims["aud"],
            expires_at=generic_claims.reserved_claims["exp"],
            issued_at=generic_claims.reserved_claims["iat"],
            issuer=generic_claims.reserved_claims["iss"],
            not_before=generic_claims.reserved_claims["nbf"],
            token_type="access_token",
            organization_claim=org_claim,
        )
