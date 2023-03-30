This API allows you to check whether the user’s provided password is valid, and to provide feedback to the user on how to increase the strength of their password.

This endpoint adapts to your Project's password strength configuration. If you're using zxcvbn, the default, your passwords are considered valid if the strength score is >= 3. If you're using LUDS, your passwords are considered valid if they meet the requirements that you've set with Stytch. Reach out to support@stytch.com if you'd like to change your password strength configuration.

Parameters

- `password`: The password to be strength tested

- `email_address`: The email associated with the password. If the email address is included, it will be factored into strength evaluation via our password breach checks. If you do not include the email, it is possible that the strength check response will evaluate as valid – but the password will fail with a weak_password error when used in the Create password endpoint due to a breach check failure.
