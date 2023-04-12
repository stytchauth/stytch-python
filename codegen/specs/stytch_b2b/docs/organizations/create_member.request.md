Creates a Member. An `organization_id` and `email_address` are required.

Parameters:

- `organization_id`: The UUID of the Organization that the Member should be created within.

- `email_address`: The email address of the Member.

- `name`: The name of the Member.

- `trusted_metadata`: An arbitrary JSON object for storing application-specific or identity-provider-specific data.

- `untrusted_metadata`: The untrusted_metadata field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end Members directly via the SDK, and cannot be used to store critical information. See the [Metadata reference](https://stytch.com/docs/b2b/api/metadata) for complete field behavior details.

- `create_member_as_pending`: Flag for whether to save a Member as `pending` or `active` in Stytch. It defaults to false. If true, new Members will be created with status `pending` in Stytch's backend. Their status will remain `pending` and they will continue to receive signup email templates for every Email Magic Link until that Member authenticates and becomes `active`. If false, new Members will be created with status `active`.

- `is_breakglass`: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](https://stytch.com/docs/b2b/api/organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
