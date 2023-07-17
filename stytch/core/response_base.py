#!/usr/bin/env python3

from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic


class ResponseBase(pydantic.BaseModel):
    status_code: int
    request_id: str

    @classmethod
    def from_json(cls, status_code: int, json: Dict[str, Any]):
        try:
            if status_code >= 400:
                raise pydantic.ValidationError([], cls)
            return cls(**json)
        except pydantic.ValidationError:
            # We need to be careful in case this one *also* fails
            try:
                details = StytchErrorDetails(**json)
                # Don't raise from here because then we trigger our
                # own fallback exception handling!
            except Exception as e:
                details = StytchErrorDetails.from_unknown(status_code)
                raise StytchError(details) from e
            raise StytchError(details) from None

    @property
    def is_informational(self) -> bool:
        return 100 <= self.status_code < 200

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    @property
    def is_redirection(self) -> bool:
        return 300 <= self.status_code < 400

    @property
    def is_client_error(self) -> bool:
        return 400 <= self.status_code < 500

    @property
    def is_server_error(self) -> bool:
        return 500 <= self.status_code < 600


class StytchErrorDetails(ResponseBase):
    error_type: Optional[str]
    error_message: str
    error_url: Optional[str]

    @classmethod
    def from_unknown(cls, status_code: int) -> StytchErrorDetails:
        return StytchErrorDetails(
            status_code=status_code,
            request_id="",
            error_type=None,
            error_message="An unknown error occurred",
            error_url=None,
        )


class StytchError(Exception):
    def __init__(self, details: StytchErrorDetails) -> None:
        self.details = details

    def __repr__(self) -> str:
        return f"StytchError {{{self.details}}}"

    def __str__(self) -> str:
        return str(self.details)
