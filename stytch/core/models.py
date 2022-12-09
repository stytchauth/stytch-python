#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Name:
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]


@dataclass
class Operand:
    filter_name: str
    filter_value: Any


@dataclass
class SearchQuery:
    operator: str
    operands: List[Operand]
