Send an invite email to a new Member to join an Organization. The Member will be created with a pending status until they successfully authenticate.

Parameters:

- `organization_id`: Globally unique UUID that identifies a specific Organization in the Stytch API. The organization_id is critical to perform operations on an Organization so be sure to preserve this value.

- `email_address`: The email address of the Member.

- `invite_redirect_url`: The URL that Members click from the login email magic link. This URL should be an endpoint in the backend server that verifies the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

- `invite_by_member_id`: The member_id of the Member who sent the invite.

- `name`: The name of the invited Member.

- `trusted_metadata`: An arbitrary JSON object for storing application-specific or identity-provider-specific data.

- `untrusted_metadata`: The untrusted_metadata field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end Members directly via the SDK, and cannot be used to store critical information. See the Metadata reference for complete field behavior details.

- `invite_template_id`: Use a custom template for invite emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Invite.
