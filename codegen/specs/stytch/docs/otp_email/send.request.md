[Stytch docs](https://stytch.com/docs/api/send-otp-by-email)

Send a one-time passcode to a user using their email. If you'd like to create a user and send them a passcode with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email-otp).

Note that sending another OTP code before the first has expired will invalidate the first code.

## Add an email to an existing user

This endpoint also allows you to add a new email to an existing Stytch User. Including a `user_id`, `session_token`, or `session_jwt` in the request will add the email to the pre-existing Stytch User upon successful authentication.

Adding a new email address to an existing Stytch User requires the user to be present and validate the email address via OTP. This requirement is in place to prevent account takeover attacks.
