Creates a new Organization. It requires a name and a unique slug.

See the [Organization authentication settings resource](https://stytch.com/docs/b2b/api/org-auth-settings) to learn more about fields like `email_jit_provisioning`, `email_allowed_domains`, `sso_jit_provisioning`, etc., and their behaviors.

Parameters:

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
