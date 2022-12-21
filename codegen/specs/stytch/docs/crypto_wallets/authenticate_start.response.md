[Stytch docs](https://stytch.com/docs/api/crypto-wallet-authenticate-start)
Response fields beyond those defined in BaseResponse:

- `user_id`: The user ID belonging to the user you associated with the request. If you did not supply a `user_id`, this will be a newly created user.
- `challenge`: A `challenge` the user must sign as part of a call to `authenticate`
- `user_created`: Whether or not a new user was created as part of this request
