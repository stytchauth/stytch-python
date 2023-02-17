Authenticates a Session. You may provide a JWT that needs to be refreshed and is expired according to its exp claim. A new JWT will be returned If both the signature and the underlying Session are still valid.

This endpoint requires only one of either the session_jwt or session_token be included in the request. It will return an error if both are present.

Parameters:

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our session management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

- `sessions_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in session_duration_minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value. Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes
