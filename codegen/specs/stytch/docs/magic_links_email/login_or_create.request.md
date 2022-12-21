[Stytch docs](https://stytch.com/docs/api/log-in-or-create-user-by-email)

Send either a login or signup magic link to the user based on if the email is associated with a user already. A new or pending user will receive a signup magic link. An active user will receive a login magic link. For more information on how to control the status your users are created in see the `create_user_as_pending` flag.

Parameters:

- `email`: The email of the user to send the invite magic link to.

- `login_magic_link_url`: The url the user clicks from the login email magic link. This should be a url that your app receives and parses and subsequently send an API request to authenticate the magic link and log in the user. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

- `signup_magic_link_url`: The url the user clicks from the sign-up email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and sign-up the user. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

- `login_expiration_minutes`: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

- `signup_expiration_minutes`: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

- `create_user_as_pending`: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false. If true, new users will be created with status pending in Stytch's backend. Their status will remain pending and they will continue to receive sign-up magic links until a magic link is authenticated for that user. If false, new users will be created with status active. They will receive a sign-up magic link for their first magic link but subsequent magic links will use the login email template, even if the user never authenticated their initial magic link.

- `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

  Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

  Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

- `attributes`: Provided attributes help with fraud detection.

- `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
