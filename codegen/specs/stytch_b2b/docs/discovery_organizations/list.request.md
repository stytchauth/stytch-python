List all possible organization relationships connected to a Member Session or Intermediate Session.

When a Member Session is passed in, relationships with a type of `active_member`, `pending_member`, or `invited_member` will be returned, and any membership can be assumed by calling the [Exchange Session](https://stytch.com/docs/b2b/api/exchange-session) endpoint.

When an Intermediate Session is passed in, all relationship types - `active_member`, `pending_member`, `invited_member`, and `eligible_to_join_by_email_domain` - will be returned, and any membership can be assumed by calling the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) endpoint.

This endpoint requires either an `intermediate_session_token`, `session_jwt` or `session_token` be included in the request. It will return an error if multiple are present.

This operation does not consume the Intermediate Session or Session Token passed in.

Parameters:

- `intermediate_session_token`: The intermediate session token.

- `session_token`: A secret token for a given Stytch Session.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session.
