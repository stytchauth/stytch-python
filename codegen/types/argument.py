#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Argument:
    name: str
    arg_type: str
    map_with: Optional[str] = None
    include_if_null: bool = False

    def generate(self) -> str:
        return f"{self.name}: {self.arg_type}"

    @property
    def nullable(self) -> bool:
        # This could definitely be better
        return "Optional" in self.arg_type

    @property
    def always_include(self) -> bool:
        # Always include it if it's not nullable or set to include if null
        return not self.nullable or self.include_if_null

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> Argument:
        return cls(**data)
