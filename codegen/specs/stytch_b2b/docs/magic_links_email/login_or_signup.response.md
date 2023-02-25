Response fields beyond those defined in `ResponseBase`:

- `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

- `member_created`: Boolean if a Member already exists with that email.

- `member`: The Member object.
