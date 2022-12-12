#!/usr/bin/env python3


from integration_test.core import IntegrationTest


class CryptoWalletsIntegrationTest(IntegrationTest):
    def test_authenticate_start(self) -> None:
        res = self.client.crypto_wallets.authenticate_start(
            crypto_wallet_type="ethereum",
            crypto_wallet_address="0x6df2dB4Fb3DA35d241901Bd53367770BF03123f1",
        )
        self.assertEqual(res.status_code, 200)

    def test_authenticate(self) -> None:
        res = self.client.crypto_wallets.authenticate(
            crypto_wallet_type="ethereum",
            crypto_wallet_address="0x6df2dB4Fb3DA35d241901Bd53367770BF03123f1",
            signature="0x0c4f82edc3c818b6beff4b89e0682994e5878074609903cecdfb843241728be32f75949e2fbae63dcccdef97c0e3789a26441f7e11456cc1f2ef79b3a436010f1b",
        )
        self.assertEqual(res.status_code, 200)
