Reset the member's password and authenticate them. This endpoint checks that the password reset token is valid, hasn’t expired, or already been used.

The provided password needs to meet our password strength requirements, which can be checked in advance with the password strength endpoint. If the token and password are accepted, the password is securely stored for future authentication and the user is authenticated.

Parameters:

- `password_reset_token`: The password reset token to authenticate.

- `password`: The password to authenticate

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

- `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
  Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes

- `code_verifier`: A base64url encoded one time secret used to validate that the request starts and ends on the same device.