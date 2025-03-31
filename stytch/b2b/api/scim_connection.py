# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from stytch.b2b.models.scim import SCIMGroupImplicitRoleAssignments
from stytch.b2b.models.scim_connection import (
    CreateRequestIdentityProvider,
    CreateRequestOptions,
    CreateResponse,
    DeleteRequestOptions,
    DeleteResponse,
    GetGroupsRequestOptions,
    GetGroupsResponse,
    GetRequestOptions,
    GetResponse,
    RotateCancelRequestOptions,
    RotateCancelResponse,
    RotateCompleteRequestOptions,
    RotateCompleteResponse,
    RotateStartRequestOptions,
    RotateStartResponse,
    UpdateRequestIdentityProvider,
    UpdateRequestOptions,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Connection:
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
        identity_provider: Optional[Union[UpdateRequestIdentityProvider, str]] = None,
        scim_group_implicit_role_assignments: Optional[
            List[Union[SCIMGroupImplicitRoleAssignments, Dict[str, Any]]]
        ] = None,
        method_options: Optional[UpdateRequestOptions] = None,
    ) -> UpdateResponse:
        """Update a SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
          - scim_group_implicit_role_assignments: An array of SCIM group implicit role assignments. Each object in the array must contain a `group_id` and a `role_id`.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
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
                item if isinstance(item, dict) else item.dict()
                for item in scim_group_implicit_role_assignments
            ]

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}", data
        )
        res = self.sync_client.put(url, data, headers)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        organization_id: str,
        connection_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[UpdateRequestIdentityProvider] = None,
        scim_group_implicit_role_assignments: Optional[
            List[SCIMGroupImplicitRoleAssignments]
        ] = None,
        method_options: Optional[UpdateRequestOptions] = None,
    ) -> UpdateResponse:
        """Update a SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
          - scim_group_implicit_role_assignments: An array of SCIM group implicit role assignments. Each object in the array must contain a `group_id` and a `role_id`.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
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
                item if isinstance(item, dict) else item.dict()
                for item in scim_group_implicit_role_assignments
            ]

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}", data
        )
        res = await self.async_client.put(url, data, headers)
        return UpdateResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[DeleteRequestOptions] = None,
    ) -> DeleteResponse:
        """Deletes a SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}", data
        )
        res = self.sync_client.delete(url, headers)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[DeleteRequestOptions] = None,
    ) -> DeleteResponse:
        """Deletes a SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}", data
        )
        res = await self.async_client.delete(url, headers)
        return DeleteResponse.from_json(res.response.status, res.json)

    def rotate_start(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[RotateStartRequestOptions] = None,
    ) -> RotateStartResponse:
        """Start a SCIM token rotation.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}/rotate/start",
            data,
        )
        res = self.sync_client.post(url, data, headers)
        return RotateStartResponse.from_json(res.response.status_code, res.json)

    async def rotate_start_async(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[RotateStartRequestOptions] = None,
    ) -> RotateStartResponse:
        """Start a SCIM token rotation.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}/rotate/start",
            data,
        )
        res = await self.async_client.post(url, data, headers)
        return RotateStartResponse.from_json(res.response.status, res.json)

    def rotate_complete(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[RotateCompleteRequestOptions] = None,
    ) -> RotateCompleteResponse:
        """Completes a SCIM token rotation. This will complete the current token rotation process and update the active token to be the new token supplied in the [start SCIM token rotation](https://stytch.com/docs/b2b/api/scim-rotate-token-start) response.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}/rotate/complete",
            data,
        )
        res = self.sync_client.post(url, data, headers)
        return RotateCompleteResponse.from_json(res.response.status_code, res.json)

    async def rotate_complete_async(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[RotateCompleteRequestOptions] = None,
    ) -> RotateCompleteResponse:
        """Completes a SCIM token rotation. This will complete the current token rotation process and update the active token to be the new token supplied in the [start SCIM token rotation](https://stytch.com/docs/b2b/api/scim-rotate-token-start) response.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}/rotate/complete",
            data,
        )
        res = await self.async_client.post(url, data, headers)
        return RotateCompleteResponse.from_json(res.response.status, res.json)

    def rotate_cancel(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[RotateCancelRequestOptions] = None,
    ) -> RotateCancelResponse:
        """Cancel a SCIM token rotation. This will cancel the current token rotation process, keeping the original token active.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}/rotate/cancel",
            data,
        )
        res = self.sync_client.post(url, data, headers)
        return RotateCancelResponse.from_json(res.response.status_code, res.json)

    async def rotate_cancel_async(
        self,
        organization_id: str,
        connection_id: str,
        method_options: Optional[RotateCancelRequestOptions] = None,
    ) -> RotateCancelResponse:
        """Cancel a SCIM token rotation. This will cancel the current token rotation process, keeping the original token active.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}/rotate/cancel",
            data,
        )
        res = await self.async_client.post(url, data, headers)
        return RotateCancelResponse.from_json(res.response.status, res.json)

    def get_groups(
        self,
        organization_id: str,
        connection_id: str,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        method_options: Optional[GetGroupsRequestOptions] = None,
    ) -> GetGroupsResponse:
        """Gets a paginated list of all SCIM Groups associated with a given Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}", data
        )
        res = self.sync_client.get(url, data, headers)
        return GetGroupsResponse.from_json(res.response.status_code, res.json)

    async def get_groups_async(
        self,
        organization_id: str,
        connection_id: str,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        method_options: Optional[GetGroupsRequestOptions] = None,
    ) -> GetGroupsResponse:
        """Gets a paginated list of all SCIM Groups associated with a given Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - connection_id: The ID of the SCIM connection.
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit

        url = self.api_base.url_for(
            "/v1/b2b/scim/{organization_id}/connection/{connection_id}", data
        )
        res = await self.async_client.get(url, data, headers)
        return GetGroupsResponse.from_json(res.response.status, res.json)

    def create(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[Union[CreateRequestIdentityProvider, str]] = None,
        method_options: Optional[CreateRequestOptions] = None,
    ) -> CreateResponse:
        """Create a new SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if identity_provider is not None:
            data["identity_provider"] = identity_provider

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connection", data)
        res = self.sync_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
        identity_provider: Optional[CreateRequestIdentityProvider] = None,
        method_options: Optional[CreateRequestOptions] = None,
    ) -> CreateResponse:
        """Create a new SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
          - display_name: A human-readable display name for the connection.
          - identity_provider: (no documentation yet)
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if identity_provider is not None:
            data["identity_provider"] = identity_provider

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connection", data)
        res = await self.async_client.post(url, data, headers)
        return CreateResponse.from_json(res.response.status, res.json)

    def get(
        self,
        organization_id: str,
        method_options: Optional[GetRequestOptions] = None,
    ) -> GetResponse:
        """Get SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connection", data)
        res = self.sync_client.get(url, data, headers)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        organization_id: str,
        method_options: Optional[GetRequestOptions] = None,
    ) -> GetResponse:
        """Get SCIM Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value. You may also use the organization_slug here as a convenience.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/scim/{organization_id}/connection", data)
        res = await self.async_client.get(url, data, headers)
        return GetResponse.from_json(res.response.status, res.json)
