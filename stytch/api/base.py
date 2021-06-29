import json
import requests
from stytch.version import __version__

from typing import Dict, Set

from .decorator import throw_stytch_exception

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
    def __init__(self, client):
        self._requester_base = requests
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Stytch Python v{}'.format(__version__)
        }
        self.client = client
        self.auth = requests.auth.HTTPBasicAuth(
            self.client.project_id, self.client.secret
        )

    def _validate_options(self, options: Dict[str, bool]) -> Dict[str, bool]:
        if not options:
            return options

        default_options = {}
        if options.get("ip_match_required"):
            default_options.update(
                {"ip_match_required": options["ip_match_required"]}
            )
        if options.get("user_agent_match_required"):
            default_options.update(
                {"user_agent_match_required": options["user_agent_match_required"]}
            )

        return default_options

    def _validate_fields(self, accepted_fields: Set[str], fields: Set[str]) -> bool:
        if len(accepted_fields.union(fields)) > len(accepted_fields):
            raise Exception("Unknown arguments applied")

        return True

    def get_url(self, arg: str):
        return "{0}{1}".format(self.client.base_url, arg)

    @throw_stytch_exception
    def _get(self, url: str, query_params: Dict = {}):
        return self._requester_base.get(url, auth=self.auth, headers=self.headers, params=query_params)

    @throw_stytch_exception
    def _post(self, url: str, data: Dict):
        return self._requester_base.post(url, auth=self.auth, headers=self.headers, data=json.dumps(data))

    @throw_stytch_exception
    def _put(self, url: str, data: Dict):
        return self._requester_base.put(url, auth=self.auth, headers=self.headers, data=json.dumps(data))

    @throw_stytch_exception
    def _delete(self, url: str):
        return self._requester_base.delete(url, auth=self.auth, headers=self.headers)
