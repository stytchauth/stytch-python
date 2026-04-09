#!/usr/bin/env python3

from __future__ import annotations

import asyncio
import unittest

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
