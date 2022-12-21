[Stytch docs](https://stytch.com/docs/api/oauth-authenticate)

Authenticate a user given a token. This endpoint verifies that the user completed the OAuth flow by verifying that the token is valid and hasn't expired. To initiate a Stytch session for the user while authenticating their OAuth token, include `session_duration_minutes`; a session with the identity provider, e.g. Google or Facebook, will always be initiated upon successful authentication.

Parameters:

- `token`: The token to authenticate.

- `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims are only created if a session is initialized by providing a value in `session duration minutes`. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value

  Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes

- `session_duration_minutes`: (Stytch sessions only) Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.

  This argument only sets the lifetime for Stytch sessions, not for IdP sessions. This value must be a minimum of 5 and a maximum of 129600 minutes (90 days).

  If a session_token or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

  If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.

- `session_jwt`: (Stytch sessions only) Reuse an existing session instead of creating a new one. If you provide us with a `session_jwt`, then we'll update the session represented by this JWT with this OAuth factor. If this `session_jwt` belongs to a different user than the OAuth token, the `session_jwt` will be ignored. This endpoint will error if both session_token and `session_jwt` are provided.

- `session_token`: (Stytch sessions only) Reuse an existing session instead of creating a new one. If you provide us with a `session_token`, then we'll update the session represented by this session token with this OAuth factor. If this `session_token` belongs to a different user than the OAuth token, the `session_token` will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.

- `code_verifier`: A base64url encoded one time secret used to validate that the request starts and ends on the same device. See the [PKCE OAuth guide](https://stytch.com/docs/oauth#guides_pkce) for usage instructions.
