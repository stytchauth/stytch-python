If an end user does not want to join any already-existing organization, or has no possible organizations to join, this endpoint can be used to create a new Organization and Member.

This operation consumes the Intermediate Session.

This endpoint can also be used to start an initial session for the newly created member and organization.

Parameters:

- `intermediate_session_token`: The Intermediate Session Token to consume to create the new Organization and Member.

- `session_duration_minutes`: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.
  - This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).
  - If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.
  - If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want to use the Stytch session product, you can ignore the session fields in the response.

- `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value.

- `organization_name`: The name of the Organization.

- `organization_slug`: The unique URL slug of the Organization.

- `organization_logo_url`: The image URL of the Organization’s logo.

- `trusted_metadata`: An arbitrary JSON object for storing application-specific data.

- `email_jit_provisioning`: The setting that controls the JIT provisioning of new Members when authenticating via email. The accepted values are:

    - RESTRICTED – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication.
    - NOT_ALLOWED – disable JIT provisioning.

- `email_invites`: The setting that controls how a new Member can be invited to an organization by email. The accepted values are:

    - ALL_ALLOWED – any new Member can be invited to join
    - RESTRICTED – only new Members with verified emails that comply with `email_allowed_domains` can be invited
    - NOT_ALLOWED – disable invites

- `email_allowed_domains`: An array of email domains that allow invitations or JIT provisioning for new Members. This list is enforced when either email_invites or email_jit_provisioning is set to RESTRICTED.

- `sso_jit_provisioning`: The setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:
    - ALL_ALLOWED – any new Member can be provisioned upon authentication
    - RESTRICTED – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication
    - NOT_ALLOWED – disable JIT provisioning

- `auth_methods`: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:
    - ALL_ALLOWED – the default setting which allows all authentication methods to be used.
    - RESTRICTED - only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

- `allowed_auth_methods`: An array of allowed authentication methods. This list is enforced when auth_methods is set to RESTRICTED. The list's accepted values are: `sso`, `magic_link`, and `password`.
