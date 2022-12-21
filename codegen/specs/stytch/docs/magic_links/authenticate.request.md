[Stytch docs](https://stytch.com/docs/api/authenticate-magic-link)

Authenticate a user given a magic link. This endpoint verifies that the magic link `token` is valid, hasn't expired or been previously used, and any optional security settings such as IP match or user agent match are satisfied.

Parameters:

- `token`: The token to authenticate.

- `options`: Specify optional security settings

- `attributes`: Provided attributes help with fraud detection. You can require the IP address and/or the user agent to match the request used to send the magic link using the options parameter.

- `session_duration_minutes`: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.

  This value must be a minimum of 5 and a maximum of 129600 minutes (90 days).

  If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

  If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.

- `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims are only created if a session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value

  Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes

- `session_jwt`: Reuse an existing session instead of creating a new one. If you provide us with a `session_jwt`, then we'll update the session represented by this JWT with this magic link factor. If this `session_jwt` belongs to a different user than the magic token, the `session_jwt` will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.

- `session_token`: Reuse an existing session instead of creating a new one. If you provide us with a `session_token`, then we'll update the session represented by this session token with this magic link factor. If this `session_token` belongs to a different user than the magic token, the `session_token` will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.

- `code_verifier`: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
