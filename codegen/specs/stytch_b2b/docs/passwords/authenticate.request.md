[Stytch docs](https://stytch.com/docs/b2b/api/passwords-authenticate)

Authenticate a member with their email address and password. This endpoint verifies that the member has a password currently set, and that the entered password is correct. There are two instances where the endpoint will return a reset_password error even if they enter their previous password:

- The member’s credentials appeared in the HaveIBeenPwned dataset.

  - We force a password reset to ensure that the member is the legitimate owner of the email address, and not a malicious actor abusing the compromised credentials.

- A member that has previously authenticated with email/password uses a passwordless authentication method tied to the same email address (e.g. Magic Links, Google OAuth) for the first time. Any subsequent email/password authentication attempt will result in this error.

  - We force a password reset in this instance in order to safely deduplicate the account by email address, without introducing the risk of a pre-hijack account takeover attack. Imagine a bad actor creates many accounts using passwords and the known email addresses of their victims. If a victim comes to the site and logs in for the first time with an email-based passwordless authentication method then both the victim and the bad actor have credentials to access to the same account. To prevent this, any further email/password login attempts first require a password reset which can only be accomplished by someone with access to the underlying email address.

Parameters:

- `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

- `email_address`: The email of the Member

- `password`: The password to authenticate

- `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

- `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

- `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
  Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes