Adds an existing password to a member's email that doesn't have a password yet. We support migrating members from passwords stored with bcrypt, scrypt, argon2, MD-5, and SHA-1. This endpoint has a rate limit of 10 requests per second.

Parameters:

- `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

- `email_address`: The email of the Member

- `hash`: The password hash. For a Scrypt hash, the hash needs to be a base64 encoded string.

- `hash_type`: The password hash used. Currently bcrypt, scrypt, argon2i, argon2id, md_5, and sha_1 are supported.

- `scrypt_config`: Required parameters if the scrypt is not provided in a PHC encoded form.

- `argon_2_config`: Required parameters if the argon2 hex form, as opposed to the encoded form, is supplied.

- `md_5_config`: Optional parameters for MD-5 hash types.

- `sha_1_config`: Optional parameters for SHA-1 hash types.