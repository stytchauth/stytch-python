#!/usr/bin/env python3

from __future__ import annotations

import asyncio
import unittest

from stytch.core.http.client import AsyncClient


class NoEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
    def get_event_loop(self):
        raise RuntimeError("No event loop")


class TestAsyncClient(unittest.TestCase):
    def test_session_without_event_loop(self):
        asyncio.set_event_loop_policy(NoEventLoopPolicy())
        client = AsyncClient("project_id", "secret")
        self.assertIsNotNone(client)
