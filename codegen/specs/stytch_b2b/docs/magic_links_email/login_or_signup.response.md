Response fields beyond those defined in `ResponseBase`:

- `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

- `member_created`: A flag indicating `true` if a new Member object was created and `false` if the Member object already existed.

- `member`: The Member object.

- `organization`: The Organization object.
