# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
from typing import Optional

from stytch.consumer.models.fraud import Fingerprints, Metadata, Properties, Verdict
from stytch.core.response_base import ResponseBase


class LookupResponse(ResponseBase):
    """Response type for `Fingerprint.lookup`.
    Fields:
      - telemetry_id: The telemetry ID associated with the fingerprint getting looked up.
      - fingerprints: A Stytch fingerprint consists of the following identifiers:
      - verdict: The metadata associated with each fingerprint
      - external_metadata: External identifiers that you wish to associate with the given telemetry ID. You will be able to search for fingerprint results by these identifiers in the DFP analytics dashboard. External metadata fields may not exceed 65 characters. They may only contain alphanumerics and the characters `_` `-` `+` `.` or `@`.
      - created_at: The time when the fingerprint was taken. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - expires_at: The timestamp when the fingerprint expires. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - properties: Additional information about the user's browser and network.
    """  # noqa

    telemetry_id: str
    fingerprints: Fingerprints
    verdict: Verdict
    external_metadata: Metadata
    created_at: datetime.datetime
    expires_at: datetime.datetime
    properties: Optional[Properties] = None
