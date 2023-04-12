Send a discovery magic link to an email address.

Parameters:

- `email_address`: The email address to send the discovery magic link to.

- `discovery_redirect_url`: The URL that the end user clicks from the discovery Magic Link. This URL should be an endpoint in the backend server that verifies the request by querying Stytch's discovery authenticate endpoint and continues the flow. If this value is not passed, the default discovery redirect URL that you set in your Dashboard is used. If you have not set a default discovery redirect URL, an error is returned.

- `pkce_code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.

- `login_template_id`: Use a custom template for discovery emails. By default, it will use your default email template. The template must be from Stytch's built-in customizations or a custom HTML email for Magic Links - Login.
