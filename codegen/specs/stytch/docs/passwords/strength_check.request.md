[Stytch docs](https://stytch.com/docs/api/password-strength-check)

This API allows you to check whether or not the user’s provided password is valid, and to provide feedback to the user on how to increase the strength of their password.

Passwords are considered invalid if either of the following is true:
[zxcvbn's](https://github.com/dropbox/zxcvbn) strength score is <= 2.
The password is present in the HaveIBeenPwned dataset.

This endpoint takes email as an optional argument, and if it is passed it will be factored into zxcvbn’s evaluation of the strength of the password. If you do not pass the email, it is possible that the password will evaluate as valid – but will fail with a `weak_password` error when used in the Create password endpoint.

Feedback will be present in the response for any password that does not meet the strength requirements, and mirrors that feedback provided by the zxcvbn library. If you would like to run the library directly in the client to further reduce latency you can find the implementation [here](https://github.com/dropbox/zxcvbn).
