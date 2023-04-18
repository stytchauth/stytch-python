# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.b2b.models.password_service import PasswordsstrengthcheckResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class PasswordService:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "password_service"

    def PasswordsStrengthCheck(
        self,
        password: str,
        email: Optional[str] = None,
    ) -> PasswordsstrengthcheckResponse:
        payload: Dict[str, Any] = {
            "password": password,
        }

        if email is not None:
            payload["email"] = email

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/passwords/strength_check"
        )

        res = self.sync_client.post(url, json=payload)
        return PasswordsstrengthcheckResponse.from_json(
            res.response.status_code, res.json
        )

    async def PasswordsStrengthCheck_async(
        self,
        password: str,
        email: Optional[str] = None,
    ) -> PasswordsstrengthcheckResponse:
        payload: Dict[str, Any] = {
            "password": password,
        }

        if email is not None:
            payload["email"] = email

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/passwords/strength_check"
        )

        res = await self.async_client.post(url, json=payload)
        return PasswordsstrengthcheckResponse.from_json(res.response.status, res.json)
