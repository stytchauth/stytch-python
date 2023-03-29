Response fields beyond those defined in `ResponseBase`:

- `member_session`: The B2BStytchSession object.

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

- `organization_id`: Globally unique UUID that identifies a specific Organization in the Stytch API. The organization_id is critical to perform operations on an Organization so be sure to preserve this value.

- `member`: The Member object.

- `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

- `member_email_id`: Globally unique UUID that identifies a member's email

- `organization`: The Organization object.
