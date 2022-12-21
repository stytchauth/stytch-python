[Stytch docs](https://stytch.com/docs/api/whatsapp-send)

Send a one-time passcode to a user's WhatsApp using their phone number. If you'd like to create a user and send them a passcode with one request, use our [log in or create endpoint](https://stytch.com/docs/api/whatsapp-login-or-create).

Note that sending another OTP code before the first has expired will invalidate the first code.

## Add a phone number to an existing user

This endpoint also allows you to add a new phone number to an existing Stytch User. Including a `user_id`, `session_token`, or `session_jwt` in the request will add the phone number to the pre-existing Stytch User upon successful authentication.

Adding a new phone number to an existing Stytch User requires the user to be present and validate the phone number via OTP. This requirement is in place to prevent account takeover attacks.
