#!/usr/bin/env python3

import asyncio
import json
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

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = requests.get(url, params=params, headers=final_headers, auth=self.auth)
        return self._response_from_request(resp)

    def post(
        self,
        url: str,
        json: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = requests.post(url, json=json, headers=final_headers, auth=self.auth)
        return self._response_from_request(resp)

    def post_form(
        self,
        url: str,
        form: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = requests.post(url, data=form, headers=final_headers, auth=self.auth)
        return self._response_from_request(resp)

    def put(
        self,
        url: str,
        json: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = requests.put(url, json=json, headers=final_headers, auth=self.auth)
        return self._response_from_request(resp)

    def delete(
        self, url: str, headers: Optional[Dict[str, str]] = None
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = requests.delete(url, headers=final_headers, auth=self.auth)
        return self._response_from_request(resp)


class AsyncClient(ClientBase):
    def __init__(
        self,
        project_id: str,
        secret: str,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        super().__init__(project_id, secret)
        self.auth = aiohttp.BasicAuth(project_id, secret)
        self._external_session = session is not None
        self.__session = session

    @property
    def _session(self) -> aiohttp.ClientSession:
        if self.__session is None:
            self.__session = aiohttp.ClientSession()
        return self.__session

    def __del__(self) -> None:
        if self._external_session or self.__session is None:
            return

        # If we're responsible for the session, close it now
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                loop.create_task(self._session.close())
            else:
                loop.run_until_complete(self._session.close())
        except Exception:
            pass

    @classmethod
    async def _response_from_request(
        cls, r: aiohttp.ClientResponse
    ) -> ResponseWithJson:
        try:
            resp_json = await r.json()
        except Exception:
            resp_json = {}
        return ResponseWithJson(response=r, json=resp_json)

    async def _response_from_post_form_request(
        cls, r: aiohttp.ClientResponse
    ) -> ResponseWithJson:
        try:
            content = await r.content.read()
            resp_json = json.loads(content.decode())
        except Exception as e:
            resp_json = {}
        return ResponseWithJson(response=r, json=resp_json)

    async def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = await self._session.get(
            url, params=params, headers=final_headers, auth=self.auth
        )
        return await self._response_from_request(resp)

    async def post(
        self,
        url: str,
        json: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = await self._session.post(
            url, json=json, headers=final_headers, auth=self.auth
        )
        return await self._response_from_request(resp)

    async def post_form(
        self,
        url: str,
        form: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = await self._session.post(
            url, data=form, headers=final_headers, auth=self.auth
        )
        return await self._response_from_post_form_request(resp)

    async def put(
        self,
        url: str,
        json: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]] = None,
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = await self._session.put(
            url, json=json, headers=final_headers, auth=self.auth
        )
        return await self._response_from_request(resp)

    async def delete(
        self, url: str, headers: Optional[Dict[str, str]] = None
    ) -> ResponseWithJson:
        final_headers = self.headers.copy()
        final_headers.update(headers or {})
        resp = await self._session.delete(url, headers=final_headers, auth=self.auth)
        return await self._response_from_request(resp)
