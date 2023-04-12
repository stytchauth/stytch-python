Revoke a Session and immediately invalidate all its tokens. To revoke a specific Session, pass either the `member_session_id`, `session_token`, or `session_jwt`. To revoke all Sessions for a Member, pass the `member_id`. This endpoint requires exactly one body param to be included in the request. It will return an error if multiple are present.

Parameters:

- `member_session_id`: The UUID of the specific Member Session to revoke.

- `session_token`: The `session_token` of the specific Member Session to revoke.

- `session_jwt`: The JSON Web Token (JWT) of the specific Member Session to revoke.

- `member_id`: The UUID of the Member to revoke all sessions for.
