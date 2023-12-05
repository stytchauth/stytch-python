# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional

import jwt

from stytch.consumer.api.m2m_clients import Clients
from stytch.consumer.models.m2m import GetTokenResponse, M2MJWTClaims
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.shared import jwt_helpers


class M2M:
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
        self.clients = Clients(
            api_base=api_base,
            sync_client=sync_client,
            async_client=async_client,
        )

    # MANUAL(m2m.token)(SERVICE_METHOD)
    # ADDIMPORT: from typing import Any, Dict, List, Optional
    # ADDIMPORT: from stytch.consumer.models.m2m import GetTokenResponse
    def token(
        self,
        client_id: str,
        client_secret: str,
        scopes: Optional[List[str]] = None,
    ) -> GetTokenResponse:
        """Retrieves an access token for the given M2M Client.
        Access tokens are JWTs signed with the project's JWKs, and are valid for one hour after issuance.
        M2M Access tokens contain a standard set of claims as well as any custom claims generated from templates.

        Fields:
          - client_id: The ID of the client.
          - client_secret: The secret of the client.
          - scopes: An array of scopes requested. If omitted, all scopes assigned to the client will be returned.
        """  # noqa

        data: Dict[str, Any] = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if scopes is not None:
            data["scope"] = " ".join(scopes)

        url = self.api_base.url_for(f"/v1/public/{self.project_id}/oauth2/token", data)
        res = self.sync_client.post(url, data)
        return GetTokenResponse.from_json(res.response.status_code, res.json)

    async def token_async(
        self,
        client_id: str,
        client_secret: str,
        scopes: Optional[List[str]] = None,
    ) -> GetTokenResponse:
        """Retrieves an access token for the given M2M Client.
        Access tokens are JWTs signed with the project's JWKs, and are valid for one hour after issuance.
        M2M Access tokens contain a standard set of claims as well as any custom claims generated from templates.

        Fields:
          - client_id: The ID of the client.
          - client_secret: The secret of the client.
          - scopes: An array scopes requested. If omitted, all scopes assigned to the client will be returned.
        """  # noqa

        data: Dict[str, Any] = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if scopes is not None:
            data["scope"] = " ".join(scopes)

        url = self.api_base.url_for(f"/v1/public/{self.project_id}/oauth2/token", data)
        res = await self.async_client.post(url, data)
        return GetTokenResponse.from_json(res.response.status_code, res.json)

    # ENDMANUAL(m2m.token)

    # MANUAL(m2m.authenticate_token)(SERVICE_METHOD)
    # ADDIMPORT: from typing import List, Optional
    # ADDIMPORT: from stytch.shared import jwt_helpers
    # ADDIMPORT: from stytch.consumer.models.m2m import M2MJWTClaims
    def authenticate_token(
        self,
        access_token: str,
        required_scopes: Optional[List[str]] = None,
        max_token_age: Optional[int] = None,
    ) -> Optional[M2MJWTClaims]:
        """Validates a M2M JWT locally.
        Note: There is no async version of this since we make no network calls.

        Fields:
          - access_token: The ID of the client.
          - required_scopes: A list of scopes the token must have to be valid.
          - max_token_age: The maximum possible lifetime in seconds for the token to be valid.
        """  # noqa

        _scope_claim = "scope"
        generic_claims = jwt_helpers.authenticate_jwt_local(
            project_id=self.project_id,
            jwks_client=self.jwks_client,
            jwt=access_token,
            max_token_age_seconds=max_token_age,
        )
        if generic_claims is None:
            return None

        scope = generic_claims.untyped_claims[_scope_claim]
        scopes = [s for s in scope.split(" ") if len(s) > 0]
        required_scopes = required_scopes or []
        missing_scopes = [scope for scope in required_scopes if scope not in scopes]
        if len(missing_scopes) != 0:
            return None

        custom_claims = {
            k: v for k, v in generic_claims.untyped_claims.items() if k != _scope_claim
        }
        return M2MJWTClaims(
            client_id=generic_claims.reserved_claims["sub"],
            scopes=scopes,
            custom_claims=custom_claims,
        )

    # ENDMANUAL(m2m.authenticate_token)
