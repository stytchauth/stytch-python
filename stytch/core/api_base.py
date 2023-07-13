#!/usr/bin/env python3

import urllib.parse
from typing import Any, Dict, Optional


class ApiBase:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def url_for(self, route: str, data: Dict[str, Any]) -> str:
        url = urllib.parse.urljoin(self.base_url, route)
        return url.format(**data)

    def route_with_sub_url(self, sub_url: str, route: Optional[str] = None) -> str:
        sub_route = sub_url
        if route is not None:
            sub_route = f"{sub_url}/{route}"
        return urllib.parse.urljoin(self.base_url, sub_route)
