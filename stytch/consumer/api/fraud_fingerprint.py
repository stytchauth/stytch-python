# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.consumer.models.fraud import Metadata
from stytch.consumer.models.fraud_fingerprint import LookupResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Fingerprint:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def lookup(
        self,
        telemetry_id: str,
        external_metadata: Optional[Union[Metadata, Dict[str, Any]]] = None,
    ) -> LookupResponse:
        """Lookup the associated fingerprint for the `telemetry_id` returned from the `GetTelemetryID` function. Learn more about the different fingerprint types and verdicts in our [DFP guide](https://stytch.com/docs/fraud/guides/device-fingerprinting/overview).

        Make a decision based on the returned `verdict`:
        * `ALLOW` - This is a known valid device grouping or device profile that is part of the default `ALLOW` listed set of known devices by Stytch. This grouping is made up of  verified device profiles that match the characteristics of known/authentic traffic origins.
        * `BLOCK` - This is a known bad or malicious device profile that is undesirable and should be blocked from completing the privileged action in question.
        * `CHALLENGE` - This is an unknown or potentially malicious device that should be put through increased friction such as 2FA or other forms of extended user verification before allowing the privileged action to proceed.

        If the `telemetry_id` is not found, we will return a 404 `telemetry_id_not_found` [error](https://stytch.com/docs/fraud/api/errors/404#telemetry_id_not_found). We recommend treating 404 errors as a `BLOCK`, since it could be a sign of an attacker trying to bypass DFP protections by generating fake telemetry IDs.

        Fields:
          - telemetry_id: The telemetry ID associated with the fingerprint getting looked up.
          - external_metadata: External identifiers that you wish to associate with the given telemetry ID. You will be able to search for fingerprint results by these identifiers in the DFP analytics dashboard. External metadata fields may not exceed 65 characters. They may only contain alphanumerics and the characters `_` `-` `+` `.` or `@`.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "telemetry_id": telemetry_id,
        }
        if external_metadata is not None:
            data["external_metadata"] = (
                external_metadata
                if isinstance(external_metadata, dict)
                else external_metadata.dict()
            )

        url = self.api_base.url_for("/v1/fingerprint/lookup", data)
        res = self.sync_client.post(url, data, headers)
        return LookupResponse.from_json(res.response.status_code, res.json)

    async def lookup_async(
        self,
        telemetry_id: str,
        external_metadata: Optional[Metadata] = None,
    ) -> LookupResponse:
        """Lookup the associated fingerprint for the `telemetry_id` returned from the `GetTelemetryID` function. Learn more about the different fingerprint types and verdicts in our [DFP guide](https://stytch.com/docs/fraud/guides/device-fingerprinting/overview).

        Make a decision based on the returned `verdict`:
        * `ALLOW` - This is a known valid device grouping or device profile that is part of the default `ALLOW` listed set of known devices by Stytch. This grouping is made up of  verified device profiles that match the characteristics of known/authentic traffic origins.
        * `BLOCK` - This is a known bad or malicious device profile that is undesirable and should be blocked from completing the privileged action in question.
        * `CHALLENGE` - This is an unknown or potentially malicious device that should be put through increased friction such as 2FA or other forms of extended user verification before allowing the privileged action to proceed.

        If the `telemetry_id` is not found, we will return a 404 `telemetry_id_not_found` [error](https://stytch.com/docs/fraud/api/errors/404#telemetry_id_not_found). We recommend treating 404 errors as a `BLOCK`, since it could be a sign of an attacker trying to bypass DFP protections by generating fake telemetry IDs.

        Fields:
          - telemetry_id: The telemetry ID associated with the fingerprint getting looked up.
          - external_metadata: External identifiers that you wish to associate with the given telemetry ID. You will be able to search for fingerprint results by these identifiers in the DFP analytics dashboard. External metadata fields may not exceed 65 characters. They may only contain alphanumerics and the characters `_` `-` `+` `.` or `@`.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "telemetry_id": telemetry_id,
        }
        if external_metadata is not None:
            data["external_metadata"] = (
                external_metadata
                if isinstance(external_metadata, dict)
                else external_metadata.dict()
            )

        url = self.api_base.url_for("/v1/fingerprint/lookup", data)
        res = await self.async_client.post(url, data, headers)
        return LookupResponse.from_json(res.response.status, res.json)