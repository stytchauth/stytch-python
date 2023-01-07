[Stytch docs](https://stytch.com/docs/api/session-auth)

NOTE: The response object should always have the user field set (ie, it will not be None), but due to backwards
compatibility with the `sessions.authenticate_jwt` method, the AuthenticateResponse marks it as Optional. The caller
should always check since the field is Optional, but the intention is that it will _not_ be None.
