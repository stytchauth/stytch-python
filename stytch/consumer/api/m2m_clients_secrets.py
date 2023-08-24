# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict

from stytch.consumer.models.m2m_clients_secrets import (
    RotateCancelResponse,
    RotateResponse,
    RotateStartResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Secrets:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def rotate_start(
        self,
        client_id: str,
    ) -> RotateStartResponse:
        """Initiate the rotation of an M2M client secret. After this endpoint is called, both the client's `client_secret` and `next_client_secret` will be valid. To complete the secret rotation flow, update all usages of `client_secret` to `next_client_secret` and call the [Rotate Secret Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret)[Rotate Secret Endpoint](https://stytch.com/docs/api/m2m-rotate-secret) to complete the flow.
        Secret rotation can be cancelled using the [Rotate Cancel Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret-cancel)[Rotate Cancel Endpoint](https://stytch.com/docs/api/m2m-rotate-secret-cancel).

        **Important:** This is the only time you will be able to view the generated `next_client_secret` in the API response. Stytch stores a hash of the `next_client_secret` and cannot recover the value if lost. Be sure to persist the `next_client_secret` in a secure location. If the `next_client_secret` is lost, you will need to trigger a secret rotation flow to receive another one.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for(
            "/v1/m2m/clients/{client_id}/secrets/rotate/start", data
        )
        res = self.sync_client.post(url, data)
        return RotateStartResponse.from_json(res.response.status_code, res.json)

    async def rotate_start_async(
        self,
        client_id: str,
    ) -> RotateStartResponse:
        """Initiate the rotation of an M2M client secret. After this endpoint is called, both the client's `client_secret` and `next_client_secret` will be valid. To complete the secret rotation flow, update all usages of `client_secret` to `next_client_secret` and call the [Rotate Secret Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret)[Rotate Secret Endpoint](https://stytch.com/docs/api/m2m-rotate-secret) to complete the flow.
        Secret rotation can be cancelled using the [Rotate Cancel Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret-cancel)[Rotate Cancel Endpoint](https://stytch.com/docs/api/m2m-rotate-secret-cancel).

        **Important:** This is the only time you will be able to view the generated `next_client_secret` in the API response. Stytch stores a hash of the `next_client_secret` and cannot recover the value if lost. Be sure to persist the `next_client_secret` in a secure location. If the `next_client_secret` is lost, you will need to trigger a secret rotation flow to receive another one.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for(
            "/v1/m2m/clients/{client_id}/secrets/rotate/start", data
        )
        res = await self.async_client.post(url, data)
        return RotateStartResponse.from_json(res.response.status, res.json)

    def rotate_cancel(
        self,
        client_id: str,
    ) -> RotateCancelResponse:
        """Cancel the rotation of an M2M client secret started with the [Start Secret Rotation Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret-start) [Start Secret Rotation Endpoint](https://stytch.com/docs/api/m2m-rotate-secret-start).
        After this endpoint is called, the client's `next_client_secret` is discarded and only the original `client_secret` will be valid.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for(
            "/v1/m2m/clients/{client_id}/secrets/rotate/cancel", data
        )
        res = self.sync_client.post(url, data)
        return RotateCancelResponse.from_json(res.response.status_code, res.json)

    async def rotate_cancel_async(
        self,
        client_id: str,
    ) -> RotateCancelResponse:
        """Cancel the rotation of an M2M client secret started with the [Start Secret Rotation Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret-start) [Start Secret Rotation Endpoint](https://stytch.com/docs/api/m2m-rotate-secret-start).
        After this endpoint is called, the client's `next_client_secret` is discarded and only the original `client_secret` will be valid.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for(
            "/v1/m2m/clients/{client_id}/secrets/rotate/cancel", data
        )
        res = await self.async_client.post(url, data)
        return RotateCancelResponse.from_json(res.response.status, res.json)

    def rotate(
        self,
        client_id: str,
    ) -> RotateResponse:
        """Complete the rotation of an M2M client secret started with the [Start Secret Rotation Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret-start) [Start Secret Rotation Endpoint](https://stytch.com/docs/api/m2m-rotate-secret-start).
        After this endpoint is called, the client's `next_client_secret` becomes its `client_secret` and the previous `client_secret` will no longer be valid.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}/secrets/rotate", data)
        res = self.sync_client.post(url, data)
        return RotateResponse.from_json(res.response.status_code, res.json)

    async def rotate_async(
        self,
        client_id: str,
    ) -> RotateResponse:
        """Complete the rotation of an M2M client secret started with the [Start Secret Rotation Endpoint](https://stytch.com/docs/b2b/api/m2m-rotate-secret-start) [Start Secret Rotation Endpoint](https://stytch.com/docs/api/m2m-rotate-secret-start).
        After this endpoint is called, the client's `next_client_secret` becomes its `client_secret` and the previous `client_secret` will no longer be valid.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}/secrets/rotate", data)
        res = await self.async_client.post(url, data)
        return RotateResponse.from_json(res.response.status, res.json)
