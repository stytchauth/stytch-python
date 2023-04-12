Authenticates the discovery Magic Link token and exchanges it for an Intermediate Session Token. Intermediate Session Tokens can be used for various [Discovery](https://stytch.com/docs/b2b/api/discovery-overview) login flows and are valid for 10 minutes.

Parameters:

- `discovery_magic_links_token`: The Discovery Email Magic Link token to authenticate.

- `pkce_code_verifier`: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
