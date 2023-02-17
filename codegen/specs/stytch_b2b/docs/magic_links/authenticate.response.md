Response fields beyond those defined in `ResponseBase`:

- `member_id`: Globally unique UUID that identifies a specific Member. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

- `method_id`: The email_id or phone_id involved in the given authentication.

- `reset_sessions`: Indicates if all Sessions linked to the Member need to be reset. You should check this field if you aren't using Stytch's Session product. If you are using Stytch's Session product, we revoke the Member’s other Sessions for you.

- `organization_id`: Globally unique UUID that identifies a specific Organization in the Stytch API. The organization_id is critical to perform operations on an Organization so be sure to preserve this value.

- `member`: The Member object.

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session`: The B2BStytchSession object.
