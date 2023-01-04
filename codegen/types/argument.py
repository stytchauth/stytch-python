#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Argument:
    name: str
    arg_type: str
    map_with: Optional[str] = None
    map_with_method: Optional[str] = None
    map_pydantic: bool = False
    include_if_null: bool = False

    def generate_in_params(self) -> str:
        return f"{self.name}: {self.arg_type}"

    def generate_in_dict_inline(self) -> str:
        value = self.name
        if self.map_with:
            value = f"{self.map_with}({self.name})"
        elif self.map_with_method:
            value = f"{self.name}.{self.map_with_method}"
        elif self.map_pydantic:
            cond = f"isinstance({self.name}, pydantic.BaseModel)"
            value = f"{self.name}.dict() if {cond} else {self.name}"
        return f'"{self.name}": {value},'

    def generate_in_dict_assignment(self, dict_name: str) -> str:
        value = self.name
        if self.map_with:
            value = f"{self.map_with}({self.name})"
        elif self.map_with_method:
            value = f"{self.name}.{self.map_with_method}"
        elif self.map_pydantic:
            cond = f"isinstance({self.name}, pydantic.BaseModel)"
            value = f"{self.name}.dict() if {cond} else {self.name}"
        return f'{dict_name}["{self.name}"] = {value}'

    @property
    def nullable(self) -> bool:
        return self.arg_type.startswith("Optional[")

    @property
    def always_include(self) -> bool:
        # Always include it if it's not nullable or set to include if null
        return not self.nullable or self.include_if_null

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Argument:
        return cls(**data)
