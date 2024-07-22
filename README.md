# Stytch Python Library

The Stytch Python library makes it easy to use the Stytch user infrastructure API in Python applications.

It pairs well with the Stytch [Web SDK](https://www.npmjs.com/package/@stytch/vanilla-js) or your own custom authentication flow.

## Requirements

The Stytch Python library supports Python 3.8+

## Installation

```
pip install stytch
```

## Usage

You can find your API credentials in the [Stytch Dashboard](https://stytch.com/dashboard/api-keys).

This client library supports all Stytch's live products:

## B2C

- [x] [Email Magic Links](https://stytch.com/docs/api/send-by-email)
- [x] [Embeddable Magic Links](https://stytch.com/docs/guides/magic-links/embeddable-magic-links/api)
- [x] [OAuth logins](https://stytch.com/docs/guides/oauth/idp-overview)
- [x] [SMS passcodes](https://stytch.com/docs/api/send-otp-by-sms)
- [x] [WhatsApp passcodes](https://stytch.com/docs/api/whatsapp-send)
- [x] [Email passcodes](https://stytch.com/docs/api/send-otp-by-email)
- [x] [Session Management](https://stytch.com/docs/guides/sessions/using-sessions)
- [x] [WebAuthn](https://stytch.com/docs/guides/webauthn/api)
- [x] [Time-based one-time passcodes (TOTPs)](https://stytch.com/docs/guides/totp/api)
- [x] [Crypto wallets](https://stytch.com/docs/guides/web3/api)
- [x] [Passwords](https://stytch.com/docs/guides/passwords/api)

## B2B

- [x] [Organizations](https://stytch.com/docs/b2b/api/organization-object)
- [x] [Members](https://stytch.com/docs/b2b/api/member-object)
- [x] [Email Magic Links](https://stytch.com/docs/b2b/api/send-login-signup-email)
- [x] [OAuth logins](https://stytch.com/docs/b2b/api/oauth-google-start)
- [x] [Session Management](https://stytch.com/docs/b2b/api/session-object)
- [x] [Single-Sign On](https://stytch.com/docs/b2b/api/sso-authenticate-start)
- [x] [Discovery](https://stytch.com/docs/b2b/api/discovered-organization-object)
- [x] [Passwords](https://stytch.com/docs/b2b/api/passwords-authenticate)

### Example B2C usage

Create an API client:

```python
import stytch

client = stytch.Client(
    project_id="project-live-c60c0abe-c25a-4472-a9ed-320c6667d317",
    secret="secret-live-80JASucyk7z_G8Z-7dVwZVGXL5NT_qGAQ2I=",
)
```

Send a magic link by email:

```python
login_or_create_resp = client.magic_links.email.login_or_create(
    email="sandbox@stytch.com",
    login_magic_link_url="https://example.com/authenticate",
    signup_magic_link_url="https://example.com/authenticate",
)
# Responses are fully-typed `pydantic` objects
print(login_or_create_resp)
```

Authenticate the token from the magic link:

```python
auth_resp = client.magic_links.authenticate(
    token="DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94=",
)
print(auth_resp)
```

## Async support

Every endpoint supports an `async` version which you can use by appending `_async` to the method name. You can use the
same `Client` object for `sync` and `async` methods. The above example of sending and authenticating an magic link can
be rewritten as:

```python
login_or_create_resp = await client.magic_links.email.login_or_create_async(
    email="sandbox@stytch.com",
    login_magic_link_url="https://example.com/authenticate",
    signup_magic_link_url="https://example.com/authenticate",
)
print(login_or_create_resp)

auth_resp = await client.magic_links.authenticate(
    token="DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94=",
)
print(resp)
```

### Example B2B usage

Create an API client:

Python:

```python
import stytch

client = stytch.B2BClient(
    project_id="project-live-c60c0abe-c25a-4472-a9ed-320c6667d317",
    secret="secret-live-80JASucyk7z_G8Z-7dVwZVGXL5NT_qGAQ2I=",
)
```

Create an organization

```python
response = client.organizations.create(
    organization_name="Acme Co",
    organization_slug="acme-co",
    email_allowed_domains=["acme.co"]
)
```

Log the first user into the organization

```python
response = client.magic_links.email.login_or_signup(
    organization_id="ORGANIZATION_ID_FROM_RESPONSE",
    email_address="admin@acme.co",
    login_redirect_url="https://example.com/authenticate",
    signup_redirect_url="https://example.com/authenticate"
)
```

## Handling Errors

Structured errors from the Stytch API will raise `StytchError` exceptions. You can view the details of the error through
the `.details` property of the `StytchError` exception.

```python
from stytch.core.response_base import StytchError

try:
    auth_resp = await client.magic_links.authenticate_async(token="token")
except StytchError as error:
    # Handle Stytch errors here
    if error.details.error_type == "invalid_token":
        print("Whoops! Try again?")
except Exception as error:
    # Handle other errors here
    pass
```

Learn more about errors in the [docs](https://stytch.com/docs/api/errors).

## Documentation

See example requests and responses for all the endpoints in the [Stytch API Reference](https://stytch.com/docs/api).

Follow one of the [integration guides](https://stytch.com/docs/home#guides) or start with one of our [example apps](https://stytch.com/docs/home#example-apps).

## Support

If you've found a bug, [open an issue](https://github.com/stytchauth/stytch-python/issues/new)!

If you have questions or want help troubleshooting, join us in [Slack](https://stytch.com/docs/resources/support/overview) or email support@stytch.com.

If you've found a security vulnerability, please follow our [responsible disclosure instructions](https://stytch.com/docs/resources/security-and-trust/security#:~:text=Responsible%20disclosure%20program).

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md)

## Code of Conduct

Everyone interacting in the Stytch project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](CODE_OF_CONDUCT.md).
