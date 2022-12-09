import functools
import json

import requests

from stytch.api.error import StytchError


def throw_stytch_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resp: requests.models.Response = func(*args, **kwargs)
        if resp.status_code >= 400:
            assert resp._content is not None
            raise StytchError(**json.loads(resp._content))
        else:
            return resp

    return wrapper
