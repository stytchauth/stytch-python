#!/usr/bin/env python3

from typing import Any, Dict, Optional

import aiohttp
import requests
import requests.auth

from stytch.version import __version__

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": f"Stytch Python v{__version__}",
}


class ClientBase:
    def __init__(self, project_id: str, secret: str) -> None:
        self.headers = HEADERS
        self.project_id = project_id
        self.secret = secret


class SyncClient(ClientBase):
    def __init__(self, project_id: str, secret: str) -> None:
        super().__init__(project_id, secret)
        self.auth = requests.auth.HTTPBasicAuth(project_id, secret)

    def get(self, url: str, params: Optional[Dict[str, Any]]) -> requests.Response:
        return requests.get(url, params=params, headers=self.headers, auth=self.auth)

    def post(self, url: str, json: Optional[Dict[str, Any]]) -> requests.Response:
        return requests.post(url, json=json, headers=self.headers, auth=self.auth)

    def put(self, url: str, json: Optional[Dict[str, Any]]) -> requests.Response:
        return requests.put(url, json=json, headers=self.headers, auth=self.auth)

    def delete(self, url: str) -> requests.Response:
        return requests.delete(url, headers=self.headers, auth=self.auth)


class AsyncClient(ClientBase):
    def __init__(self, project_id: str, secret: str) -> None:
        super().__init__(project_id, secret)
        self.auth = aiohttp.BasicAuth(project_id, secret)

    async def get(
        self, url: str, params: Optional[Dict[str, Any]]
    ) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.get(
                url, params=params, headers=self.headers, auth=self.auth
            )

    async def post(
        self, url: str, json: Optional[Dict[str, Any]]
    ) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.post(
                url, json=json, headers=self.headers, auth=self.auth
            )

    async def put(
        self, url: str, json: Optional[Dict[str, Any]]
    ) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.put(
                url, json=json, headers=self.headers, auth=self.auth
            )

    async def delete(self, url: str) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.delete(url, headers=self.headers, auth=self.auth)
