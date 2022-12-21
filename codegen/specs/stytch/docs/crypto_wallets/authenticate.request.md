[Stytch docs](https://stytch.com/docs/api/crypto-wallet-authenticate)

Complete the authentication of a crypto wallet by passing the signature.

Parameters:

- `crypto_wallet_type`: The type of wallet to authenticate. Currently `ethereum` and `solana` are supported.

- `crypto_wallet_address`: The address to authenticate.

- `signature`: The signature from the message.

- `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims are only created if a session is initialized by providing a value in `session duration minutes`. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value

  Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes

- `session_duration_minutes`: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.

  This value must be a minimum of 5 and a maximum of 129600 minutes (90 days).

  If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

  If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.

- `session_jwt`: Reuse an existing session instead of creating a new one. If you provide us with a `session_jwt`, then we'll update the session represented by this JWT with this crypto wallet factor. If this `session_jwt` belongs to a different user than the one tied to the address, the `session_jwt` will be ignored. This endpoint will error if both `session_token` and `session_jwt` are provided.

- `session_token`: Reuse an existing session instead of creating a new one. If you provide us with a `session_token`, then we'll update the session represented by this session token with this crypto wallet factor. If this `session_token` belongs to a different user than the one tied to the address, the `session_token` will be ignored. This endpoint will error if both session_token and `session_jwt` are provided.
