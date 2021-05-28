# v2.0.0 (unreleased)

Breaking changes:
* Removed `Client.MagicLinks`. Use `Client.magic_links` instead.
* Removed `Client.OTP`. Use `Client.otp` instead.
* Removed `Client.Users`. Use `Client.users` instead.
* Removed `Client.magic_links.send`. Use `Client.magic_links.send_by_email` instead.
* Removed `magic_link_url` parameter in `Client.magic_links.invite_by_email`. Use `login_magic_link_url` and `signup_magic_link_url` instead.
* Removed `expiration_minutes` parameter in `Client.magic_links.invite_by_email`. Use `login_expiration_minutes` and `signup_expiration_minutes` instead.

# v1.4.0 (unreleased)

Additions:
* Add `create_user_as_pending` argument to `Client.users.create`

Deprecations:
* `Client.MagicLinks`: Use `Client.magic_links` instead.
* `Client.OTP`: Use `Client.otp` instead.
* `Client.Users`: Use `Client.users` instead.
* `Client.magic_links.send`: Use `Client.magic_links.send_by_email` instead.
* `magic_link_url` parameter in `Client.magic_links.send_by_email`: Use `login_magic_link_url` and `signup_magic_link_url` instead.
* `expiration_minutes` parameter in `Client.magic_links.send_by_email`: Use `login_expiration_minutes` and `signup_expiration_minutes` instead.

# v1.3.5 and earlier

See the [GitHub releases](https://github.com/stytchauth/stytch-python/releases) for release notes.
