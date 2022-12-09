#!/usr/bin/env python3

from __future__ import annotations

from enum import Enum, auto


class HttpMethod(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()

    def __str__(self) -> str:
        return self.name.lower()

    @classmethod
    def from_str(cls, s: str) -> HttpMethod:
        if s == "GET":
            return cls.GET
        elif s == "POST":
            return cls.POST
        elif s == "PUT":
            return cls.PUT
        elif s == "DELETE":
            return cls.DELETE
        else:
            raise ValueError(f"Unknown HttpMethod: {s}")
