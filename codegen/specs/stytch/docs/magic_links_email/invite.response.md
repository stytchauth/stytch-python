[Stytch docs](https://stytch.com/docs/api/invite-by-email)

Response fields beyond those defined in `ResponseBase`:

- `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

- `email_id`: Globally unique UUID that identifies a specific email address in the Stytch API. The `email_id` is used when you need to operate on a specific user's email address, e.g. to delete the email address from the Stytch user.
