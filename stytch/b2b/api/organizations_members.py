# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional

from stytch.b2b.models.organizations import SearchQuery
from stytch.b2b.models.organizations_members import (
    CreateResponse,
    DeletePasswordResponse,
    DeletePhoneNumberResponse,
    DeleteResponse,
    GetResponse,
    SearchResponse,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Members:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def update(
        self,
        organization_id: str,
        member_id: str,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        is_breakglass: Optional[bool] = None,
        phone_number: Optional[str] = None,
        mfa_enrolled: Optional[bool] = None,
    ) -> UpdateResponse:
        """Updates a Member specified by `organization_id` and `member_id`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - name: The name of the Member.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - is_breakglass: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
          - phone_number: (no documentation yet)
          - mfa_enrolled: (no documentation yet)
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if is_breakglass is not None:
            data["is_breakglass"] = is_breakglass
        if phone_number is not None:
            data["phone_number"] = phone_number
        if mfa_enrolled is not None:
            data["mfa_enrolled"] = mfa_enrolled

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}", data
        )
        res = self.sync_client.put(url, data)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        organization_id: str,
        member_id: str,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        is_breakglass: Optional[bool] = None,
        phone_number: Optional[str] = None,
        mfa_enrolled: Optional[bool] = None,
    ) -> UpdateResponse:
        """Updates a Member specified by `organization_id` and `member_id`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - name: The name of the Member.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - is_breakglass: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
          - phone_number: (no documentation yet)
          - mfa_enrolled: (no documentation yet)
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if is_breakglass is not None:
            data["is_breakglass"] = is_breakglass
        if phone_number is not None:
            data["phone_number"] = phone_number
        if mfa_enrolled is not None:
            data["mfa_enrolled"] = mfa_enrolled

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}", data
        )
        res = await self.async_client.put(url, data)
        return UpdateResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        organization_id: str,
        member_id: str,
    ) -> DeleteResponse:
        """Deletes a Member specified by `organization_id` and `member_id`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}", data
        )
        res = self.sync_client.delete(url)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
        self,
        organization_id: str,
        member_id: str,
    ) -> DeleteResponse:
        """Deletes a Member specified by `organization_id` and `member_id`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}", data
        )
        res = await self.async_client.delete(url)
        return DeleteResponse.from_json(res.response.status, res.json)

    def delete_phone_number(
        self,
        organization_id: str,
        member_id: str,
    ) -> DeletePhoneNumberResponse:
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/phone_numbers/{member_id}",
            data,
        )
        res = self.sync_client.delete(url)
        return DeletePhoneNumberResponse.from_json(res.response.status_code, res.json)

    async def delete_phone_number_async(
        self,
        organization_id: str,
        member_id: str,
    ) -> DeletePhoneNumberResponse:
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/phone_numbers/{member_id}",
            data,
        )
        res = await self.async_client.delete(url)
        return DeletePhoneNumberResponse.from_json(res.response.status, res.json)

    def search(
        self,
        organization_ids: List[str],
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchQuery] = None,
    ) -> SearchResponse:
        """Search for Members within specified Organizations. An array with at least one `organization_id` is required. Submitting an empty `query` returns all Members within the specified Organizations.

        *All fuzzy search filters require a minimum of three characters.

        Fields:
          - organization_ids: An array of organization_ids. At least one value is required.
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all Organizations with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_ids": organization_ids,
        }
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/b2b/organizations/members/search", data)
        res = self.sync_client.post(url, data)
        return SearchResponse.from_json(res.response.status_code, res.json)

    async def search_async(
        self,
        organization_ids: List[str],
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchQuery] = None,
    ) -> SearchResponse:
        """Search for Members within specified Organizations. An array with at least one `organization_id` is required. Submitting an empty `query` returns all Members within the specified Organizations.

        *All fuzzy search filters require a minimum of three characters.

        Fields:
          - organization_ids: An array of organization_ids. At least one value is required.
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all Organizations with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_ids": organization_ids,
        }
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/b2b/organizations/members/search", data)
        res = await self.async_client.post(url, data)
        return SearchResponse.from_json(res.response.status, res.json)

    def delete_password(
        self,
        organization_id: str,
        member_password_id: str,
    ) -> DeletePasswordResponse:
        """Delete a Member's password.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_password_id: Globally unique UUID that identifies a Member's password.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_password_id": member_password_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/passwords/{member_password_id}",
            data,
        )
        res = self.sync_client.delete(url)
        return DeletePasswordResponse.from_json(res.response.status_code, res.json)

    async def delete_password_async(
        self,
        organization_id: str,
        member_password_id: str,
    ) -> DeletePasswordResponse:
        """Delete a Member's password.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_password_id: Globally unique UUID that identifies a Member's password.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_password_id": member_password_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/passwords/{member_password_id}",
            data,
        )
        res = await self.async_client.delete(url)
        return DeletePasswordResponse.from_json(res.response.status, res.json)

    def create(
        self,
        organization_id: str,
        email_address: str,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        create_member_as_pending: Optional[bool] = None,
        is_breakglass: Optional[bool] = None,
        phone_number: Optional[str] = None,
        mfa_enrolled: Optional[bool] = None,
    ) -> CreateResponse:
        """Creates a Member. An `organization_id` and `email_address` are required.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - name: The name of the Member.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - create_member_as_pending: Flag for whether or not to save a Member as `pending` or `active` in Stytch. It defaults to false. If true, new Members will be created with status `pending` in Stytch's backend. Their status will remain `pending` and they will continue to receive signup email templates for every Email Magic Link until that Member authenticates and becomes `active`. If false, new Members will be created with status `active`.
          - is_breakglass: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
          - phone_number: (no documentation yet)
          - mfa_enrolled: (no documentation yet)
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
        }
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if create_member_as_pending is not None:
            data["create_member_as_pending"] = create_member_as_pending
        if is_breakglass is not None:
            data["is_breakglass"] = is_breakglass
        if phone_number is not None:
            data["phone_number"] = phone_number
        if mfa_enrolled is not None:
            data["mfa_enrolled"] = mfa_enrolled

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members", data
        )
        res = self.sync_client.post(url, data)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        organization_id: str,
        email_address: str,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        create_member_as_pending: Optional[bool] = None,
        is_breakglass: Optional[bool] = None,
        phone_number: Optional[str] = None,
        mfa_enrolled: Optional[bool] = None,
    ) -> CreateResponse:
        """Creates a Member. An `organization_id` and `email_address` are required.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - name: The name of the Member.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - create_member_as_pending: Flag for whether or not to save a Member as `pending` or `active` in Stytch. It defaults to false. If true, new Members will be created with status `pending` in Stytch's backend. Their status will remain `pending` and they will continue to receive signup email templates for every Email Magic Link until that Member authenticates and becomes `active`. If false, new Members will be created with status `active`.
          - is_breakglass: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
          - phone_number: (no documentation yet)
          - mfa_enrolled: (no documentation yet)
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
        }
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if create_member_as_pending is not None:
            data["create_member_as_pending"] = create_member_as_pending
        if is_breakglass is not None:
            data["is_breakglass"] = is_breakglass
        if phone_number is not None:
            data["phone_number"] = phone_number
        if mfa_enrolled is not None:
            data["mfa_enrolled"] = mfa_enrolled

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members", data
        )
        res = await self.async_client.post(url, data)
        return CreateResponse.from_json(res.response.status, res.json)

    def get(
        self,
        organization_id: str,
        member_id: Optional[str] = None,
        email_address: Optional[str] = None,
    ) -> GetResponse:
        """Get a Member by `member_id` or `email_address`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - email_address: The email address of the Member.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if member_id is not None:
            data["member_id"] = member_id
        if email_address is not None:
            data["email_address"] = email_address

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/member", data
        )
        res = self.sync_client.get(url, data)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        organization_id: str,
        member_id: Optional[str] = None,
        email_address: Optional[str] = None,
    ) -> GetResponse:
        """Get a Member by `member_id` or `email_address`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - email_address: The email address of the Member.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if member_id is not None:
            data["member_id"] = member_id
        if email_address is not None:
            data["email_address"] = email_address

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/member", data
        )
        res = await self.async_client.get(url, data)
        return GetResponse.from_json(res.response.status, res.json)
