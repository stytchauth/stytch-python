[Stytch docs](https://stytch.com/docs/api/password-email-reset)

Reset the user’s password and authenticate them. This endpoint checks that the magic link `token` is valid, hasn’t expired, or already been used – and can optionally require additional security settings, such as the IP address and user agent matching the initial reset request.

The provided password needs to meet our password strength requirements, which can be checked in advance with the password strength endpoint. If the token and password are accepted, the password is securely stored for future authentication and the user is authenticated.
