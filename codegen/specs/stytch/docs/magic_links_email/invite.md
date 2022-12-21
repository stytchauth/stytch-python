[Stytch docs](https://stytch.com/docs/api/invite-by-email)

Create a pending user and send an invite magic link to the provided email. The user will be created with a pending status until they click the magic link in the invite email.

Parameters:

- `email`: The email of the user to send the invite magic link to.

- `invite_magic_link_url`: The url the user clicks from the email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and log in the user. If this value is not passed, the default invite redirect URL that you set in your Dashboard is used. If you have not set a default invite redirect URL, an error is returned.

- `invite_expiration_minutes`: Set the expiration for the email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

- `name`: The name of the user. Each field in the name object is optional.

- `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

  Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

  Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

- `attributes`: Provided attributes help with fraud detection.
