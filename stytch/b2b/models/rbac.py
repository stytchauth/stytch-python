# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import List, Optional

import pydantic

from stytch.core.response_base import ResponseBase


class PolicyResource(pydantic.BaseModel):
    """
    Fields:
      - resource_id: A unique identifier of the RBAC Resource, provided by the developer and intended to be human-readable.

      A `resource_id` is not allowed to start with `stytch`, which is a special prefix used for Stytch default Resources with reserved  `resource_id`s. These include:

      * `stytch.organization`
      * `stytch.member`
      * `stytch.sso`
      * `stytch.self`

      Check out the [guide on Stytch default Resources](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


      - description: The description of the RBAC Resource.
      - actions: A list of all possible actions for a provided Resource.

      Reserved `actions` that are predefined by Stytch include:

      * `*`
      * For the `stytch.organization` Resource:
        * `update.info.name`
        * `update.info.slug`
        * `update.info.untrusted_metadata`
        * `update.info.email_jit_provisioning`
        * `update.info.logo_url`
        * `update.info.email_invites`
        * `update.info.allowed_domains`
        * `update.info.default_sso_connection`
        * `update.info.sso_jit_provisioning`
        * `update.info.mfa_policy`
        * `update.info.implicit_roles`
        * `delete`
      * For the `stytch.member` Resource:
        * `create`
        * `update.info.name`
        * `update.info.untrusted_metadata`
        * `update.info.mfa-phone`
        * `update.info.delete.mfa-phone`
        * `update.settings.is-breakglass`
        * `update.settings.mfa_enrolled`
        * `update.settings.roles`
        * `search`
        * `delete`
      * For the `stytch.sso` Resource:
        * `create`
        * `update`
        * `delete`
      * For the `stytch.self` Resource:
        * `update.info.name`
        * `update.info.untrusted_metadata`
        * `update.info.mfa-phone`
        * `update.info.delete.mfa-phone`
        * `update.info.delete.password`
        * `update.settings.mfa_enrolled`
        * `delete`

    """  # noqa

    resource_id: str
    description: str
    actions: List[str]


class PolicyRolePermission(pydantic.BaseModel):
    """
    Fields:
      - resource_id: A unique identifier of the RBAC Resource, provided by the developer and intended to be human-readable.

      A `resource_id` is not allowed to start with `stytch`, which is a special prefix used for Stytch default Resources with reserved  `resource_id`s. These include:

      * `stytch.organization`
      * `stytch.member`
      * `stytch.sso`
      * `stytch.self`

      Check out the [guide on Stytch default Resources](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


      - actions: A list of permitted actions the Role is authorized to take with the provided Resource. You can use `*` as a wildcard to grant a Role permission to use all possible actions related to the Resource.
    """  # noqa

    resource_id: str
    actions: List[str]


class PolicyRole(pydantic.BaseModel):
    """
    Fields:
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-default) for a more detailed explanation.


      - description: The description of the RBAC Role.
      - permissions: A list of permissions that link a [Resource](https://stytch.com/docs/b2b/api/rbac-resource-object) to a list of actions.
    """  # noqa

    role_id: str
    description: str
    permissions: List[PolicyRolePermission]


class Policy(pydantic.BaseModel):
    """
    Fields:
      - roles: An array of [Role objects](https://stytch.com/docs/b2b/api/rbac-role-object).
      - resources: An array of [Resource objects](https://stytch.com/docs/b2b/api/rbac-resource-object).
    """  # noqa

    roles: List[PolicyRole]
    resources: List[PolicyResource]


class PolicyResponse(ResponseBase):
    """Response type for `RBAC.policy`.
    Fields:
      - policy: The RBAC Policy document that contains all defined Roles and Resources – which are managed in the [Dashboard](https://stytch.com/docs/dashboard/rbac). Read more about these entities and how they work in our [RBAC overview](https://stytch.com/docs/b2b/guides/rbac/overview).
    """  # noqa

    policy: Optional[Policy] = None
