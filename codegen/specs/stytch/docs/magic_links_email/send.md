[Stytch docs](https://stytch.com/docs/api/send-by-email)

Send a magic link to an existing Stytch user using their email address. If you'd like to create a user and send them a magic link by email with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email).

Parameters:

- `email`: The email of the user to send the invite magic link to.

- `login_magic_link_url`: The url the user clicks from the login email magic link. This should be a url that your app receives and parses and subsequently send an API request to authenticate the magic link and log in the user. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

- `signup_magic_link_url`: The url the user clicks from the sign-up email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and sign-up the user. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

- `login_expiration_minutes`: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

- `signup_expiration_minutes`: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

- `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

  Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

  Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

- `attributes`: Provided attributes help with fraud detection.

- `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.

- `user_id`: The `user_id` of the user to associate the email with. This parameter allows you to associate a new email address with an existing Stytch User.

  Only include a `user_id` if the user in question already has an active and valid session at the time of the send operation; without this safety check a malicious user may use this as an account takeover vector.

- `session_token`: The `session_token` belonging to the user that you wish to associate the email with.

- `session_jwt`: The `session_jwt` belonging to the user that you wish to associate the email with.
