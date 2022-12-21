[Stytch docs](https://stytch.com/docs/api/update-user)

Update a user's name or attributes.

**Note:** In order to add a new email address or phone number to an existing User object, pass the new email address or phone number into the respective `/send` endpoint for the authentication method of your choice. If you specify the existing user's Stytch `user_id` while calling the `/send` endpoint, the new email address or phone number will be added to the existing User object upon successful authentication. We require this process to guard against an account takeover vulnerability.
