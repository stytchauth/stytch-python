# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Dict, Optional

import pydantic

from stytch.b2b.models.sso import OIDCConnection
from stytch.core.response_base import ResponseBase
from stytch.shared.method_options import Authorization


class CreateConnectionRequestIdentityProvider(str, enum.Enum):
    CLASSLINK = "classlink"
    CYBERARK = "cyberark"
    DUO = "duo"
    GENERIC = "generic"
    GOOGLEWORKSPACE = "google-workspace"
    JUMPCLOUD = "jumpcloud"
    KEYCLOAK = "keycloak"
    MINIORANGE = "miniorange"
    MICROSOFTENTRA = "microsoft-entra"
    OKTA = "okta"
    ONELOGIN = "onelogin"
    PINGFEDERATE = "pingfederate"
    RIPPLING = "rippling"
    SALESFORCE = "salesforce"
    SHIBBOLETH = "shibboleth"


class UpdateConnectionRequestIdentityProvider(str, enum.Enum):
    CLASSLINK = "classlink"
    CYBERARK = "cyberark"
    DUO = "duo"
    GENERIC = "generic"
    GOOGLEWORKSPACE = "google-workspace"
    JUMPCLOUD = "jumpcloud"
    KEYCLOAK = "keycloak"
    MINIORANGE = "miniorange"
    MICROSOFTENTRA = "microsoft-entra"
    OKTA = "okta"
    ONELOGIN = "onelogin"
    PINGFEDERATE = "pingfederate"
    RIPPLING = "rippling"
    SALESFORCE = "salesforce"
    SHIBBOLETH = "shibboleth"


class CreateConnectionRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class UpdateConnectionRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class CreateConnectionResponse(ResponseBase):
    """Response type for `OIDC.create_connection`.
    Fields:
      - connection: The `OIDC Connection` object affected by this API call. See the [OIDC Connection Object](https://stytch.com/docs/b2b/api/oidc-connection-object) for complete response field details.
    """  # noqa

    connection: Optional[OIDCConnection] = None


class UpdateConnectionResponse(ResponseBase):
    """Response type for `OIDC.update_connection`.
    Fields:
      - connection: The `OIDC Connection` object affected by this API call. See the [OIDC Connection Object](https://stytch.com/docs/b2b/api/oidc-connection-object) for complete response field details.
      - warning: If it is not possible to resolve the well-known metadata document from the OIDC issuer, this field will explain what went wrong if the request is successful otherwise. In other words, even if the overall request succeeds, there could be relevant warnings related to the connection update.
    """  # noqa

    connection: Optional[OIDCConnection] = None
    warning: Optional[str] = None
