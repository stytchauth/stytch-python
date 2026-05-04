#!/usr/bin/env python3

from __future__ import annotations

import asyncio
import unittest

import aiohttp
import requests

from stytch.core.http.client import AsyncClient, SyncClient


class NoEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
    def get_event_loop(self):
        raise RuntimeError("No event loop")


class TestSyncClient(unittest.TestCase):
    def test_external_session_is_used(self):
        session = requests.Session()
        client = SyncClient("project_id", "secret", session=session)
        self.assertIs(client._session, session)

    def test_no_external_session_creates_one(self):
        client = SyncClient("project_id", "secret")
        self.assertIsInstance(client._session, requests.Session)


class TestAsyncClient(unittest.TestCase):
    def test_session_without_event_loop(self):
        asyncio.set_event_loop_policy(NoEventLoopPolicy())
        client = AsyncClient("project_id", "secret")
        self.assertIsNotNone(client)


class TestAsyncClientClose(unittest.IsolatedAsyncioTestCase):
    async def test_close_owned_session(self):
        client = AsyncClient("project_id", "secret")
        session = client._session  # force session creation and capture reference
        await client.close()
        self.assertTrue(session.closed)

    async def test_close_external_session_is_noop(self):
        async with aiohttp.ClientSession() as external:
            client = AsyncClient("project_id", "secret", session=external)
            await client.close()
            self.assertFalse(external.closed)

    async def test_close_before_session_created_is_noop(self):
        client = AsyncClient("project_id", "secret")
        # no session accessed — should not raise
        await client.close()
