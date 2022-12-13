#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Argument:
    name: str
    arg_type: str
    map_with: Optional[str] = None
    map_with_method: Optional[str] = None
    include_if_null: bool = False

    def generate_in_params(self) -> str:
        return f"{self.name}: {self.arg_type}"

    def generate_in_dict_inline(self) -> str:
        value = self.name
        if self.map_with:
            value = f"{self.map_with}({self.name})"
        elif self.map_with_method:
            value = f"{self.name}.{self.map_with_method}"
        return f'"{self.name}": {value},'

    def generate_in_dict_assignment(self, dict_name: str) -> str:
        value = self.name
        if self.map_with:
            value = f"{self.map_with}({self.name})"
        elif self.map_with_method:
            value = f"{self.name}.{self.map_with_method}"
        return f'{dict_name}["{self.name}"] = {value}'

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
