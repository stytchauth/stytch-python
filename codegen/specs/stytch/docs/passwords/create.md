[Stytch docs](https://stytch.com/docs/api/password-create)

Create a new user with a password and an authenticated session for the user if requested. If a user with this email already exists in the project, this API will return an error.

Existing passwordless users who wish to create a password need to go through the reset password flow.

This endpoint will return an error if the password provided does not meet our strength requirements, which you can check beforehand with the password strength endpoint.
