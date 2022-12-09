import json
from typing import TYPE_CHECKING, Any, Dict, Optional, Set

import requests
from requests.auth import HTTPBasicAuth

from stytch.api.decorator import throw_stytch_exception
from stytch.version import __version__

if TYPE_CHECKING:
    from stytch.client import Client


def _validate_attributes(attributes: Dict[str, str]) -> Dict[str, str]:
    if not attributes:
        return attributes
    default_attributes = {}

    if attributes.get("ip_address"):
        default_attributes.update({"ip_address": attributes["ip_address"]})
    if attributes.get("user_agent"):
        default_attributes.update({"user_agent": attributes["user_agent"]})

    return default_attributes


class Base:
    def __init__(self, client: "Client") -> None:
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Stytch Python v{}".format(__version__),
        }
        self.client = client
        self.auth = HTTPBasicAuth(self.client.project_id, self.client.secret)

    def _validate_options(self, options: Dict[str, bool]) -> Dict[str, bool]:
        if not options:
            return options

        default_options = {}
        if options.get("ip_match_required"):
            default_options.update({"ip_match_required": options["ip_match_required"]})
        if options.get("user_agent_match_required"):
            default_options.update(
                {"user_agent_match_required": options["user_agent_match_required"]}
            )

        return default_options

    def _validate_fields(self, accepted_fields: Set[str], fields: Set[str]) -> bool:
        if len(accepted_fields.union(fields)) > len(accepted_fields):
            raise Exception("Unknown arguments applied")

        return True

    def get_url(self, arg: str) -> str:
        return "{0}{1}".format(self.client.base_url, arg)

    @throw_stytch_exception
    def _get(
        self, url: str, query_params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        query_params = query_params or {}
        return requests.get(
            url, auth=self.auth, headers=self.headers, params=query_params
        )

    @throw_stytch_exception
    def _post(self, url: str, data: Dict[str, Any]) -> requests.Response:
        return requests.post(
            url, auth=self.auth, headers=self.headers, data=json.dumps(data)
        )

    @throw_stytch_exception
    def _put(self, url: str, data: Dict[str, Any]) -> requests.Response:
        return requests.put(
            url, auth=self.auth, headers=self.headers, data=json.dumps(data)
        )

    @throw_stytch_exception
    def _delete(self, url: str) -> requests.Response:
        return requests.delete(url, auth=self.auth, headers=self.headers)
