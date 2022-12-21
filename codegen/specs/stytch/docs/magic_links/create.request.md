[Stytch docs](https://stytch.com/docs/api/create-magic-link)

Create a magic link token for a user. Access to this endpoint is restricted, to be enabled for it, please send us a note at support@stytch.com.

Parameters:

- `user_id`: The user ID for the magic link token.

- `expiration_minutes`: Set the expiration for the magic token, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

- `attributes`: Provided attributes help with fraud detection. When authenticating a user's magic link token, you can require the IP address and/or the user agent to match that user's attributes when they originated the initial authentication request. To enable this functionality, you can use the options parameter in [AuthenticateMagic](https://stytch.com/docs/api/authenticate-magic-link).
