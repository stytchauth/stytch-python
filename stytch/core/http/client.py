#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any, Dict, Generic, Optional, TypeVar

import aiohttp
import requests
import requests.auth

from stytch.version import __version__

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": f"Stytch Python v{__version__}",
}

T = TypeVar("T")


@dataclass
class ResponseWithJson(Generic[T]):
    response: T
    json: Dict[str, Any]


class ClientBase:
    def __init__(self, project_id: str, secret: str) -> None:
        self.headers = HEADERS
        self.project_id = project_id
        self.secret = secret


class SyncClient(ClientBase):
    def __init__(self, project_id: str, secret: str) -> None:
        super().__init__(project_id, secret)
        self.auth = requests.auth.HTTPBasicAuth(project_id, secret)

    @classmethod
    def _response_from_request(cls, r: requests.Response) -> ResponseWithJson:
        try:
            resp_json = r.json()
        except Exception:
            resp_json = {}
        return ResponseWithJson(response=r, json=resp_json)

    def get(self, url: str, params: Optional[Dict[str, Any]]) -> ResponseWithJson:
        resp = requests.get(url, params=params, headers=self.headers, auth=self.auth)
        return self._response_from_request(resp)

    def post(self, url: str, json: Optional[Dict[str, Any]]) -> ResponseWithJson:
        resp = requests.post(url, json=json, headers=self.headers, auth=self.auth)
        return self._response_from_request(resp)

    def put(self, url: str, json: Optional[Dict[str, Any]]) -> ResponseWithJson:
        resp = requests.put(url, json=json, headers=self.headers, auth=self.auth)
        return self._response_from_request(resp)

    def delete(self, url: str) -> ResponseWithJson:
        resp = requests.delete(url, headers=self.headers, auth=self.auth)
        return self._response_from_request(resp)


class AsyncClient(ClientBase):
    def __init__(self, project_id: str, secret: str) -> None:
        super().__init__(project_id, secret)
        self.auth = aiohttp.BasicAuth(project_id, secret)

    @classmethod
    async def _response_from_request(
        cls, r: aiohttp.ClientResponse
    ) -> ResponseWithJson:
        try:
            resp_json = await r.json()
        except Exception:
            resp_json = {}
        return ResponseWithJson(response=r, json=resp_json)

    async def get(self, url: str, params: Optional[Dict[str, Any]]) -> ResponseWithJson:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(
                url, params=params, headers=self.headers, auth=self.auth
            )
            return await self._response_from_request(resp)

    async def post(self, url: str, json: Optional[Dict[str, Any]]) -> ResponseWithJson:
        async with aiohttp.ClientSession() as session:
            resp = await session.post(
                url, json=json, headers=self.headers, auth=self.auth
            )
            return await self._response_from_request(resp)

    async def put(self, url: str, json: Optional[Dict[str, Any]]) -> ResponseWithJson:
        async with aiohttp.ClientSession() as session:
            resp = await session.put(
                url, json=json, headers=self.headers, auth=self.auth
            )
            return await self._response_from_request(resp)

    async def delete(self, url: str) -> ResponseWithJson:
        async with aiohttp.ClientSession() as session:
            resp = await session.delete(url, headers=self.headers, auth=self.auth)
            return await self._response_from_request(resp)
