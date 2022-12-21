[Stytch docs](https://stytch.com/docs/api/authenticate-otp)

Authenticate a user given a method ID and a code. This endpoint verifies that the code is valid, hasn't expired or been previously used, and any optional security settings such as IP match or user agent match are satisfied. A given `method_id` may only have a single active OTP code at any given time, if a user requests another OTP code before the first one has expired, the first one will be invalidated.
