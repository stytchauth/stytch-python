Revoke a Session and immediately invalidate all its tokens. To revoke a specific Session, pass either the member_session_id, session_token, or session_jwt. To revoke all Sessions for a Member, pass the member_id. This endpoint requires exactly one body param to be included in the request. It will return an error if multiple are present.

Parameters:

- `member_session_id`: Globally unique UUID that identifies a specific Member’s Session.

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session management guide.

- `member_id`: Globally unique UUID that identifies a specific Member. The member_id is critical to perform operations on a Member, so be sure to preserve this value.
