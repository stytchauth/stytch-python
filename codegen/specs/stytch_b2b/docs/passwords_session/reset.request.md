Reset the member's password using their existing session. The endpoint will error if the session does not an authentication factor that has been issued within the last 5 minutes.

Parameters:

- `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

- `password`: The new password for the user.

- `session_token`: The session token for the user whose password will be reset. This endpoint will error if both session_token and session_jwt are provided.

- `session_jwt`: The session JWT for the user whose password will be reset. This endpoint will error if both session_token and session_jwt are provided.