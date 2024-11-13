#!/usr/bin/env python3

from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic


class ResponseError(ValueError):
    ...


class ResponseBase(pydantic.BaseModel):
    status_code: int
    request_id: str

    @classmethod
    def from_json(cls, status_code: int, json: Dict[str, Any]):
        try:
            if status_code >= 400:
                raise ResponseError()
            return cls(**json)
        except ResponseError:
            # We need to be careful in case this one *also* fails
            try:
                details = StytchErrorDetails(**json)
                details.original_json = json
                # Don't raise from here because then we trigger our
                # own fallback exception handling!
            except Exception as e:
                details = StytchErrorDetails.from_unknown(status_code, json)
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
    error_type: Optional[str] = pydantic.Field(
        validation_alias=pydantic.AliasChoices("error_type", "error")
    )
    error_message: str = pydantic.Field(
        validation_alias=pydantic.AliasChoices("error_message", "error_description")
    )
    error_url: Optional[str] = pydantic.Field(
        validation_alias=pydantic.AliasChoices("error_url", "error_uri")
    )
    original_json: Optional[Dict[str, Any]] = None

    @classmethod
    def from_unknown(
        cls, status_code: int, original_json: Optional[Dict[str, Any]] = None
    ) -> StytchErrorDetails:
        message = "An unknown error occurred"
        if 200 <= status_code < 300:
            message = "Failed to parse JSON into target object type"
        return StytchErrorDetails(
            status_code=status_code,
            request_id="",
            error_type=None,
            error_message=message,
            error_url=None,
            original_json=original_json,
        )


class StytchError(Exception):
    def __init__(self, details: StytchErrorDetails) -> None:
        self.details = details

    def __repr__(self) -> str:
        return f"StytchError {{{self.details}}}"

    def __str__(self) -> str:
        return str(self.details)
