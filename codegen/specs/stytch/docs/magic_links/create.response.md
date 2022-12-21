[Stytch docs](https://stytch.com/docs/api/create-magic-link)

Response fields beyond those defined in `ResponseBase`:

- `user_id`: Globally unique UUID that identifies a specific user in the Stytch API. The `user_id` critical to perform operations on a user in our API, like Get user, Delete user, etc, so be sure to preserve this value.

- `token`: The magic link token that you'll include in your contact method of choice, e.g. email or SMS. Check out our [Embeddable magic link guide](https://stytch.com/docs/api/magic-links#embeddable-magic-links_embeddable-overview) for more detail on where to include the token.
