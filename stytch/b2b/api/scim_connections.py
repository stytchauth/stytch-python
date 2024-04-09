# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from stytch.b2b.models.scim import SCIMGroupImplicitRoleAssignments
from stytch.b2b.models.scim_connections import (
    CreateRequestIdp,
    CreateResponse,
    DeleteResponse,
    GetResponse,
    RotateCancelResponse,
    RotateCompleteResponse,
    RotateStartResponse,
    UpdateRequestIdp,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Connections:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def update(
        self,
        organization_id: str,
        connection_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[Union[UpdateRequestIdp, str]] = None,
        scim_group_implicit_role_assignments: Optional[
            List[SCIMGroupImplicitRoleAssignments]
        ] = None,
    ) -> UpdateResponse:
        """Update a SCIM Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
          - scim_group_implicit_role_assignments: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if identity_provider is not None:
            data["identity_provider"] = identity_provider
        if scim_group_implicit_role_assignments is not None:
            data["scim_group_implicit_role_assignments"] = [
                item.dict() for item in scim_group_implicit_role_assignments
            ]

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}", data
        )
        res = self.sync_client.put(url, data, headers)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        organization_id: str,
        connection_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[UpdateRequestIdp] = None,
        scim_group_implicit_role_assignments: Optional[
            List[SCIMGroupImplicitRoleAssignments]
        ] = None,
    ) -> UpdateResponse:
        """Update a SCIM Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
          - scim_group_implicit_role_assignments: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if identity_provider is not None:
            data["identity_provider"] = identity_provider
        if scim_group_implicit_role_assignments is not None:
            data["scim_group_implicit_role_assignments"] = [
                item.dict() for item in scim_group_implicit_role_assignments
            ]

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}", data
        )
        res = await self.async_client.put(url, data, headers)
        return UpdateResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        organization_id: str,
        connection_id: str,
    ) -> DeleteResponse:
        """Deletes a SCIM Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}", data
        )
        res = self.sync_client.delete(url, headers)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
        self,
        organization_id: str,
        connection_id: str,
    ) -> DeleteResponse:
        """Deletes a SCIM Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}", data
        )
        res = await self.async_client.delete(url, headers)
        return DeleteResponse.from_json(res.response.status, res.json)

    def rotate_start(
        self,
        organization_id: str,
        connection_id: str,
    ) -> RotateStartResponse:
        """Start a SCIM token rotation. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}/rotate/start",
            data,
        )
        res = self.sync_client.post(url, data, headers)
        return RotateStartResponse.from_json(res.response.status_code, res.json)

    async def rotate_start_async(
        self,
        organization_id: str,
        connection_id: str,
    ) -> RotateStartResponse:
        """Start a SCIM token rotation. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}/rotate/start",
            data,
        )
        res = await self.async_client.post(url, data, headers)
        return RotateStartResponse.from_json(res.response.status, res.json)

    def rotate_complete(
        self,
        organization_id: str,
        connection_id: str,
    ) -> RotateCompleteResponse:
        """Completes a SCIM token rotation. This will complete the current token rotation process and update the active token to be the new token supplied in the [start SCIM token rotation](https://stytch.com/docs/b2b/api/scim-rotate-token-start) response. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}/rotate/complete",
            data,
        )
        res = self.sync_client.post(url, data, headers)
        return RotateCompleteResponse.from_json(res.response.status_code, res.json)

    async def rotate_complete_async(
        self,
        organization_id: str,
        connection_id: str,
    ) -> RotateCompleteResponse:
        """Completes a SCIM token rotation. This will complete the current token rotation process and update the active token to be the new token supplied in the [start SCIM token rotation](https://stytch.com/docs/b2b/api/scim-rotate-token-start) response. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}/rotate/complete",
            data,
        )
        res = await self.async_client.post(url, data, headers)
        return RotateCompleteResponse.from_json(res.response.status, res.json)

    def rotate_cancel(
        self,
        organization_id: str,
        connection_id: str,
    ) -> RotateCancelResponse:
        """Cancel a SCIM token rotation. This will cancel the current token rotation process, keeping the original token active. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}/rotate/cancel",
            data,
        )
        res = self.sync_client.post(url, data, headers)
        return RotateCancelResponse.from_json(res.response.status_code, res.json)

    async def rotate_cancel_async(
        self,
        organization_id: str,
        connection_id: str,
    ) -> RotateCancelResponse:
        """Cancel a SCIM token rotation. This will cancel the current token rotation process, keeping the original token active. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connections/{connection_id}/rotate/cancel",
            data,
        )
        res = await self.async_client.post(url, data, headers)
        return RotateCancelResponse.from_json(res.response.status, res.json)

    def create(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[Union[CreateRequestIdp, str]] = None,
    ) -> CreateResponse:
        """Create a new SCIM Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if identity_provider is not None:
            data["identity_provider"] = identity_provider

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connections", data)
        res = self.sync_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[CreateRequestIdp] = None,
    ) -> CreateResponse:
        """Create a new SCIM Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if identity_provider is not None:
            data["identity_provider"] = identity_provider

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connections", data)
        res = await self.async_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status, res.json)

    def get(
        self,
        organization_id: str,
    ) -> GetResponse:
        """Get SCIM Connections. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connections", data)
        res = self.sync_client.get(url, data, headers)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        organization_id: str,
    ) -> GetResponse:
        """Get SCIM Connections. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connections", data)
        res = await self.async_client.get(url, data, headers)
        return GetResponse.from_json(res.response.status, res.json)