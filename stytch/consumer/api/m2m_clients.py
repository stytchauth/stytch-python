# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional

from stytch.consumer.api.m2m_clients_secrets import Secrets
from stytch.consumer.models.m2m import M2MSearchQuery
from stytch.consumer.models.m2m_clients import (
    CreateResponse,
    DeleteResponse,
    GetResponse,
    SearchResponse,
    UpdateRequestStatus,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Clients:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.secrets = Secrets(api_base, sync_client, async_client)

    def get(
        self,
        client_id: str,
    ) -> GetResponse:
        """Gets information about an existing M2M Client.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}", data)
        res = self.sync_client.get(url, data)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        client_id: str,
    ) -> GetResponse:
        """Gets information about an existing M2M Client.

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}", data)
        res = await self.async_client.get(url, data)
        return GetResponse.from_json(res.response.status, res.json)

    def search(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[M2MSearchQuery] = None,
    ) -> SearchResponse:
        """Search for M2M Clients within your Stytch Project. Submit an empty `query` in the request to return all M2M Clients.

        The following search filters are supported today:
        - `client_id`: Pass in a list of client IDs to get many clients in a single request
        - `client_name`: Search for clients by exact match on client name
        - `scopes`: Search for clients assigned a specific scope

        Fields:
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all results with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {}
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/m2m/clients/search", data)
        res = self.sync_client.post(url, data)
        return SearchResponse.from_json(res.response.status_code, res.json)

    async def search_async(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[M2MSearchQuery] = None,
    ) -> SearchResponse:
        """Search for M2M Clients within your Stytch Project. Submit an empty `query` in the request to return all M2M Clients.

        The following search filters are supported today:
        - `client_id`: Pass in a list of client IDs to get many clients in a single request
        - `client_name`: Search for clients by exact match on client name
        - `scopes`: Search for clients assigned a specific scope

        Fields:
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all results with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {}
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/m2m/clients/search", data)
        res = await self.async_client.post(url, data)
        return SearchResponse.from_json(res.response.status, res.json)

    def update(
        self,
        client_id: str,
        client_name: Optional[str] = None,
        client_description: Optional[str] = None,
        status: Optional[UpdateRequestStatus] = None,
        scopes: Optional[List[str]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateResponse:
        """Updates an existing M2M Client. You can use this endpoint to activate or deactivate a M2M Client by changing its `status`. A deactivated M2M Client will not be allowed to perform future token exchange flows until it is reactivated.

        **Important:** Deactivating a M2M Client will not invalidate any existing JWTs issued to the client, only prevent it from receiving new ones.
        To protect more-sensitive routes, pass a lower `max_token_age` value when[authenticating the token](https://stytch.com/docs/b2b/api/authenticate-m2m-token)[authenticating the token](https://stytch.com/docs/api/authenticate-m2m-token).

        Fields:
          - client_id: The ID of the client.
          - client_name: A human-readable name for the client.
          - client_description: A human-readable description for the client.
          - status: The status of the client - either `active` or `inactive`.
          - scopes: An array of scopes assigned to the client.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }
        if client_name is not None:
            data["client_name"] = client_name
        if client_description is not None:
            data["client_description"] = client_description
        if status is not None:
            data["status"] = status.value
        if scopes is not None:
            data["scopes"] = scopes
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}", data)
        res = self.sync_client.put(url, data)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        client_id: str,
        client_name: Optional[str] = None,
        client_description: Optional[str] = None,
        status: Optional[UpdateRequestStatus] = None,
        scopes: Optional[List[str]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> UpdateResponse:
        """Updates an existing M2M Client. You can use this endpoint to activate or deactivate a M2M Client by changing its `status`. A deactivated M2M Client will not be allowed to perform future token exchange flows until it is reactivated.

        **Important:** Deactivating a M2M Client will not invalidate any existing JWTs issued to the client, only prevent it from receiving new ones.
        To protect more-sensitive routes, pass a lower `max_token_age` value when[authenticating the token](https://stytch.com/docs/b2b/api/authenticate-m2m-token)[authenticating the token](https://stytch.com/docs/api/authenticate-m2m-token).

        Fields:
          - client_id: The ID of the client.
          - client_name: A human-readable name for the client.
          - client_description: A human-readable description for the client.
          - status: The status of the client - either `active` or `inactive`.
          - scopes: An array of scopes assigned to the client.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }
        if client_name is not None:
            data["client_name"] = client_name
        if client_description is not None:
            data["client_description"] = client_description
        if status is not None:
            data["status"] = status.value
        if scopes is not None:
            data["scopes"] = scopes
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}", data)
        res = await self.async_client.put(url, data)
        return UpdateResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        client_id: str,
    ) -> DeleteResponse:
        """Deletes the M2M Client.

        **Important:** Deleting a M2M Client will not invalidate any existing JWTs issued to the client, only prevent it from receiving new ones.
        To protect more-sensitive routes, pass a lower `max_token_age` value when[authenticating the token](https://stytch.com/docs/b2b/api/authenticate-m2m-token)[authenticating the token](https://stytch.com/docs/api/authenticate-m2m-token).

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}", data)
        res = self.sync_client.delete(url)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
        self,
        client_id: str,
    ) -> DeleteResponse:
        """Deletes the M2M Client.

        **Important:** Deleting a M2M Client will not invalidate any existing JWTs issued to the client, only prevent it from receiving new ones.
        To protect more-sensitive routes, pass a lower `max_token_age` value when[authenticating the token](https://stytch.com/docs/b2b/api/authenticate-m2m-token)[authenticating the token](https://stytch.com/docs/api/authenticate-m2m-token).

        Fields:
          - client_id: The ID of the client.
        """  # noqa
        data: Dict[str, Any] = {
            "client_id": client_id,
        }

        url = self.api_base.url_for("/v1/m2m/clients/{client_id}", data)
        res = await self.async_client.delete(url)
        return DeleteResponse.from_json(res.response.status, res.json)

    def create(
        self,
        scopes: List[str],
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        client_name: Optional[str] = None,
        client_description: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """Creates a new M2M Client. On initial client creation, you may pass in a custom `client_id` or `client_secret` to import an existing M2M client. If you do not pass in a custom `client_id` or `client_secret`, one will be generated automatically. The `client_id` must be unique among all clients in your project.

        **Important:** This is the only time you will be able to view the generated `client_secret` in the API response. Stytch stores a hash of the `client_secret` and cannot recover the value if lost. Be sure to persist the `client_secret` in a secure location. If the `client_secret` is lost, you will need to trigger a secret rotation flow to receive another one.

        Fields:
          - scopes: An array of scopes assigned to the client.
          - client_id: If provided, the ID of the client to create. If not provided, Stytch will generate this value for you. The `client_id` must be unique within your project.
          - client_secret: If provided, the stored secret of the client to create. If not provided, Stytch will generate this value for you. If provided, the `client_secret` must be at least 8 characters long and pass entropy requirements.
          - client_name: A human-readable name for the client.
          - client_description: A human-readable description for the client.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {
            "scopes": scopes,
        }
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if client_name is not None:
            data["client_name"] = client_name
        if client_description is not None:
            data["client_description"] = client_description
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata

        url = self.api_base.url_for("/v1/m2m/clients", data)
        res = self.sync_client.post(url, data)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        scopes: List[str],
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        client_name: Optional[str] = None,
        client_description: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> CreateResponse:
        """Creates a new M2M Client. On initial client creation, you may pass in a custom `client_id` or `client_secret` to import an existing M2M client. If you do not pass in a custom `client_id` or `client_secret`, one will be generated automatically. The `client_id` must be unique among all clients in your project.

        **Important:** This is the only time you will be able to view the generated `client_secret` in the API response. Stytch stores a hash of the `client_secret` and cannot recover the value if lost. Be sure to persist the `client_secret` in a secure location. If the `client_secret` is lost, you will need to trigger a secret rotation flow to receive another one.

        Fields:
          - scopes: An array of scopes assigned to the client.
          - client_id: If provided, the ID of the client to create. If not provided, Stytch will generate this value for you. The `client_id` must be unique within your project.
          - client_secret: If provided, the stored secret of the client to create. If not provided, Stytch will generate this value for you. If provided, the `client_secret` must be at least 8 characters long and pass entropy requirements.
          - client_name: A human-readable name for the client.
          - client_description: A human-readable description for the client.
          - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
        """  # noqa
        data: Dict[str, Any] = {
            "scopes": scopes,
        }
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if client_name is not None:
            data["client_name"] = client_name
        if client_description is not None:
            data["client_description"] = client_description
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata

        url = self.api_base.url_for("/v1/m2m/clients", data)
        res = await self.async_client.post(url, data)
        return CreateResponse.from_json(res.response.status, res.json)