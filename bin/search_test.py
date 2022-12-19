#!/usr/bin/env python3

import asyncio
import contextlib
import logging
import os
import random
import string
import sys
import time
from typing import Generator, List

import stytch


@contextlib.contextmanager
def report_elapsed() -> Generator[None, None, None]:
    start = time.time()
    try:
        yield
    except Exception as e:
        logging.info(f"Warning: got {e} during timing")
        raise
    finally:
        end = time.time()
        logging.info(f"Elapsed: {(end - start):.2f} seconds")


def sync_search(client: stytch.Client) -> int:
    search_resp = client.users.search()
    return len(search_resp.results)


async def async_search(client: stytch.Client) -> int:
    search_resp = await client.users.search_async()
    return len(search_resp.results)


def create_test_users(client: stytch.Client, n: int) -> List[str]:
    user_ids = []
    for i in range(1, n + 1):
        username = "".join(random.choice(string.ascii_letters) for _ in range(20))
        password = "".join(random.choice(string.printable) for _ in range(24))
        email = f"{username}@example.com"
        resp = client.passwords.create(email=email, password=password)
        user_ids.append(resp.user_id)
        if i % 10 == 0:
            logging.debug(f"Created {i} users")
    return user_ids


def delete_test_users(client: stytch.Client, user_ids: List[str]) -> None:
    for i, user_id in enumerate(user_ids, start=1):
        client.users.delete(user_id)
        if i % 10 == 0:
            logging.debug(f"Deleted {i} users")


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    project_id = os.getenv("STYTCH_PROJECT_ID")
    secret = os.getenv("STYTCH_SECRET")
    if project_id is None or secret is None:
        sys.exit("Missing required env variable")

    client = stytch.Client(project_id, secret, "test")

    logging.info("Deleting existing test users")
    with report_elapsed():
        search = client.users.search()
        logging.info(f"Will delete {len(search.results)} users")
        delete_test_users(client, [user.user_id for user in search.results])

    logging.info("Creating 100 test users")
    with report_elapsed():
        user_ids = create_test_users(client, 100)

    logging.info("Sync search")
    with report_elapsed():
        sync_search(client)

    logging.info("Async search")
    with report_elapsed():
        asyncio.run(async_search(client))

    logging.info("Deleting test users")
    with report_elapsed():
        delete_test_users(client, user_ids)


if __name__ == "__main__":
    main()
