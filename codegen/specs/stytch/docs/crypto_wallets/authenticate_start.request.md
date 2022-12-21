[Stytch docs](https://stytch.com/docs/api/crypto-wallet-authenticate-start)

Initiate the authentication of a crypto wallet. After calling this endpoint, the user will need to sign a message containing only the returned `challenge` field.

Parameters:

- `crypto_wallet_type`: The type of wallet to authenticate. Currently `ethereum` and `solana` are supported. Wallets for any EVM-compatible chains (such as Polygon or BSC) are also supported and are grouped under the `ethereum` type.

- `crypto_wallet_address`: The address to authenticate.

- `user_id`: The `user_id` belonging to the user you wish to associate the address with. If no form of user association is provided and the address is not associated with an existing Stytch user in your Project, a new user will be created.

- `session_token`: The `session_token` belonging to the user you wish to associate the address with. If no form of user association is provided and the address is not associated with an existing Stytch user in your Project, a new user will be created.

- `session_jwt`: The `session_jwt` belonging to the user you wish to associate the address with. If no form of user association is provided and the address is not associated with an existing Stytch user in your Project, a new user will be created.
