[Stytch docs](https://stytch.com/docs/api/password-authenticate)

Authenticate a user with their email address and password. This endpoint verifies that the user has a password currently set, and that the entered password is correct. There are two instances where the endpoint will return a reset_password error even if they enter their previous password:

- The user’s credentials appeared in the HaveIBeenPwned dataset.

  - We force a password reset to ensure that the user is the legitimate owner of the email address, and not a malicious actor abusing the compromised credentials.

- A user that has previously authenticated with email/password uses a passwordless authentication method tied to the same email address (e.g. Magic Links, Google OAuth) for the first time. Any subsequent email/password authentication attempt will result in this error.

  - We force a password reset in this instance in order to safely deduplicate the account by email address, without introducing the risk of a pre-hijack account takeover attack. Imagine a bad actor creates many accounts using passwords and the known email addresses of their victims. If a victim comes to the site and logs in for the first time with an email-based passwordless authentication method then both the victim and the bad actor have credentials to access to the same account. To prevent this, any further email/password login attempts first require a password reset which can only be accomplished by someone with access to the underlying email address.
