Send either a login or signup magic link to a Member. A new or pending Member will receive a signup Email Magic Link. An active Member will receive a login Email Magic Link.

Parameters:

- `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

- `email_address`: The email of the Member who will receive the Email Magic Link for login or signup.

- `login_redirect_url`: The URL that Member clicks from the login email magic link. This URL should be an endpoint in the backend server that verifies the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

- `signup_redirect_url`: The url the Member clicks from the sign-up email magic link. This URL should be an endpoint in the backend server that verifies the request by querying Stytch's authenticate endpoint and finishes the login. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

- `pkce_code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device. See the PKCE OAuth guide for usage instructions.

- `login_template_id`: Use a custom template for login emails. By default, it will use your default email template The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.

- `signup_template_id`: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.

- `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

  Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

  Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!
