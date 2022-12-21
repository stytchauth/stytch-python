[Stytch docs](https://stytch.com/docs/api/session-auth)

Authenticate a session token and retrieve associated session data. If session_duration_minutes is included, update the lifetime of the session to be that many minutes from now. All timestamps are formatted according to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`

This endpoint requires exactly one `session_jwt` or `session_token` as part of the request. If both are included you will receive a `too_many_session_arguments` error.
