Exchange an Intermediate Session for a fully realized Member Session in a desired Organization. This operation consumes the Intermediate Session.

This endpoint can be used to accept invites and create new members via domain matching.

Parameters:

- `intermediate_session_token`: The Intermediate Session Token to consume to create the new Member.

- `organization_id`: The UUID of the Organization to create the new Member and Member Session in.

- `session_duration_minutes`: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.
    - This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).
    - If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.
    - If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want to use the Stytch session product, you can ignore the session fields in the response.

- `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value.
