#!/usr/bin/env python3

import urllib.parse


class ApiBase:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def with_sub_url(self, sub_url: str) -> str:
        return urllib.parse.urljoin(self.base_url, sub_url)
