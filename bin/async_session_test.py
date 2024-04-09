#!/usr/bin/env python3

import asyncio
import os

import aiohttp
import stytch


async def main() -> None:
    print("=== Test 1: custom session ===")
    session = aiohttp.ClientSession(headers={"async-test": "true"})
    client = stytch.Client(
        project_id=os.environ["STYTCH_PROJECT_ID"],
        secret=os.environ["STYTCH_SECRET"],
        async_session=session,
    )
    resp = await client.users.search_async()
    print(f"First user: {resp.results[0].user_id}")
    await session.close()

    print("\n\n=== Test 2: default session ===")
    client = stytch.Client(
        project_id=os.environ["STYTCH_PROJECT_ID"],
        secret=os.environ["STYTCH_SECRET"],
    )
    resp = await client.users.search_async()
    print(f"First user: {resp.results[0].user_id}")

    print("\n\n=== Testing done ===")


if __name__ == "__main__":
    asyncio.run(main())
