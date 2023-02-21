Authenticate a Member with a magic link. This endpoint requires a magic link token to validate, making sure it's not expired or previously used. If the Member’s status is invited or pending, they will be updated to active.

Parameters:

- `magic_links_token`: The token to authenticate.

- `pkce_code_verifier`: A base64url encoded one-time secret used to validate that the request starts and ends on the same device.

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

- `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
  Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes
