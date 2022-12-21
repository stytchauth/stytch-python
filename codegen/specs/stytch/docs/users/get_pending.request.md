[Stytch docs](https://stytch.com/docs/api/get-pending-users)

Fetch all users with a pending status. Users will show up here if they are added via the `invite_by_email` endpoint or via `login_or_create` where `create_as_pending = true` and have yet to create their account by clicking on the magic link in the email. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
