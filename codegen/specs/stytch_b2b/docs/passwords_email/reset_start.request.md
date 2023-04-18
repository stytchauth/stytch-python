[Stytch docs](https://stytch.com/docs/api/password-email-reset-start)

Initiates a password reset for the email address provided. This will trigger an email to be sent to the address, containing a magic link that will allow them to set a new password and authenticate.

Parameters:

- `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

- `email_address`: The email of the Member

- `reset_password_redirect_url`: The URL that the Member clicks from the reset password link

- `login_redirect_url`: The URL that the Member clicks from the reset without password link

- `reset_password_template_id`: Use a custom template for reset password emails.

- `locale`: Used to determine which language to use when sending the member an email. 

- `reset_password_expiration_minutes`: Sets a time limit after which the email link to reset the member's password will no longer be valid.

- `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.