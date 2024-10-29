# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Dict, Optional

import pydantic

from stytch.b2b.models.sso import SAMLConnection
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


class DeleteVerificationCertificateRequestOptions(pydantic.BaseModel):
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


class UpdateByURLRequestOptions(pydantic.BaseModel):
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
    """Response type for `SAML.create_connection`.
    Fields:
      - connection: The `SAML Connection` object affected by this API call. See the [SAML Connection Object](https://stytch.com/docs/b2b/api/saml-connection-object) for complete response field details.
    """  # noqa

    connection: Optional[SAMLConnection] = None


class DeleteVerificationCertificateResponse(ResponseBase):
    """Response type for `SAML.delete_verification_certificate`.
    Fields:
      - certificate_id: The ID of the certificate that was deleted.
    """  # noqa

    certificate_id: str


class UpdateByURLResponse(ResponseBase):
    """Response type for `SAML.update_by_url`.
    Fields:
      - connection: The `SAML Connection` object affected by this API call. See the [SAML Connection Object](https://stytch.com/docs/b2b/api/saml-connection-object) for complete response field details.
    """  # noqa

    connection: Optional[SAMLConnection] = None


class UpdateConnectionResponse(ResponseBase):
    """Response type for `SAML.update_connection`.
    Fields:
      - connection: The `SAML Connection` object affected by this API call. See the [SAML Connection Object](https://stytch.com/docs/b2b/api/saml-connection-object) for complete response field details.
    """  # noqa

    connection: Optional[SAMLConnection] = None
