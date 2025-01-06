# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.consumer.models.fraud import RuleAction
from stytch.consumer.models.fraud_rules import SetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Rules:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def set(
        self,
        action: Union[RuleAction, str],
        visitor_id: Optional[str] = None,
        browser_id: Optional[str] = None,
        visitor_fingerprint: Optional[str] = None,
        browser_fingerprint: Optional[str] = None,
        hardware_fingerprint: Optional[str] = None,
        network_fingerprint: Optional[str] = None,
        expires_in_minutes: Optional[int] = None,
        description: Optional[str] = None,
    ) -> SetResponse:
        """Set a rule for a particular `visitor_id`, `browser_id`, `visitor_fingerprint`, `browser_fingerprint`, `hardware_fingerprint`, or `network_fingerprint`. This is helpful in cases where you want to allow or block a specific user or fingerprint. You should be careful when setting rules for `browser_fingerprint`, `hardware_fingerprint`, or `network_fingerprint` as they can be shared across multiple users, and you could affect more users than intended.

        Rules are applied in the order specified above. For example, if an end user has an `ALLOW` rule set for their `visitor_id` but a `BLOCK` rule set for their `hardware_fingerprint`, they will receive an `ALLOW` verdict because the `visitor_id` rule takes precedence.

        Fields:
          - action: The action that should be returned by a fingerprint lookup for that fingerprint or ID with a `RULE_MATCH` reason. The following values are valid: `ALLOW`, `BLOCK`, `CHALLENGE`, or `NONE`. If a `NONE` action is specified, it will clear the stored rule.
          - visitor_id: The visitor ID we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - browser_id: The browser ID we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - visitor_fingerprint: The visitor fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - browser_fingerprint: The browser fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - hardware_fingerprint: The hardware fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - network_fingerprint: The network fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - expires_in_minutes: The number of minutes until this rule expires. If no `expires_in_minutes` is specified, then the rule is kept permanently.
          - description: An optional description for the rule.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "action": action,
        }
        if visitor_id is not None:
            data["visitor_id"] = visitor_id
        if browser_id is not None:
            data["browser_id"] = browser_id
        if visitor_fingerprint is not None:
            data["visitor_fingerprint"] = visitor_fingerprint
        if browser_fingerprint is not None:
            data["browser_fingerprint"] = browser_fingerprint
        if hardware_fingerprint is not None:
            data["hardware_fingerprint"] = hardware_fingerprint
        if network_fingerprint is not None:
            data["network_fingerprint"] = network_fingerprint
        if expires_in_minutes is not None:
            data["expires_in_minutes"] = expires_in_minutes
        if description is not None:
            data["description"] = description

        url = self.api_base.url_for("/v1/rules/set", data)
        res = self.sync_client.post(url, data, headers)
        return SetResponse.from_json(res.response.status_code, res.json)

    async def set_async(
        self,
        action: RuleAction,
        visitor_id: Optional[str] = None,
        browser_id: Optional[str] = None,
        visitor_fingerprint: Optional[str] = None,
        browser_fingerprint: Optional[str] = None,
        hardware_fingerprint: Optional[str] = None,
        network_fingerprint: Optional[str] = None,
        expires_in_minutes: Optional[int] = None,
        description: Optional[str] = None,
    ) -> SetResponse:
        """Set a rule for a particular `visitor_id`, `browser_id`, `visitor_fingerprint`, `browser_fingerprint`, `hardware_fingerprint`, or `network_fingerprint`. This is helpful in cases where you want to allow or block a specific user or fingerprint. You should be careful when setting rules for `browser_fingerprint`, `hardware_fingerprint`, or `network_fingerprint` as they can be shared across multiple users, and you could affect more users than intended.

        Rules are applied in the order specified above. For example, if an end user has an `ALLOW` rule set for their `visitor_id` but a `BLOCK` rule set for their `hardware_fingerprint`, they will receive an `ALLOW` verdict because the `visitor_id` rule takes precedence.

        Fields:
          - action: The action that should be returned by a fingerprint lookup for that fingerprint or ID with a `RULE_MATCH` reason. The following values are valid: `ALLOW`, `BLOCK`, `CHALLENGE`, or `NONE`. If a `NONE` action is specified, it will clear the stored rule.
          - visitor_id: The visitor ID we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - browser_id: The browser ID we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - visitor_fingerprint: The visitor fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - browser_fingerprint: The browser fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - hardware_fingerprint: The hardware fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - network_fingerprint: The network fingerprint we want to set a rule for. Only one fingerprint or ID can be specified in the request.
          - expires_in_minutes: The number of minutes until this rule expires. If no `expires_in_minutes` is specified, then the rule is kept permanently.
          - description: An optional description for the rule.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "action": action,
        }
        if visitor_id is not None:
            data["visitor_id"] = visitor_id
        if browser_id is not None:
            data["browser_id"] = browser_id
        if visitor_fingerprint is not None:
            data["visitor_fingerprint"] = visitor_fingerprint
        if browser_fingerprint is not None:
            data["browser_fingerprint"] = browser_fingerprint
        if hardware_fingerprint is not None:
            data["hardware_fingerprint"] = hardware_fingerprint
        if network_fingerprint is not None:
            data["network_fingerprint"] = network_fingerprint
        if expires_in_minutes is not None:
            data["expires_in_minutes"] = expires_in_minutes
        if description is not None:
            data["description"] = description

        url = self.api_base.url_for("/v1/rules/set", data)
        res = await self.async_client.post(url, data, headers)
        return SetResponse.from_json(res.response.status, res.json)
