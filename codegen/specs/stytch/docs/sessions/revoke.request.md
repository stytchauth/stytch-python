[Stytch docs](https://stytch.com/docs/api/session-revoke)

Revoke a session, immediately invalidating all of its session tokens. You can revoke a session in three ways: using its ID, or using one of its session tokens, or one of its JWTs. This endpoint requires exactly one of those to be included in the request. It will return an error if multiple are present.
