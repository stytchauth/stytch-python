from typing import Any, Dict, List, Optional

from .base import Base

class CryptoWallets(Base):
    @property
    def crypto_wallet_url(self):
        return self.get_url("crypto_wallets")

    def authenticate_start(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ):
        data = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
        }
        if user_id:
            data["user_id"] = user_id
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt

        return self._post(
            "{0}/authenticate/start".format(
                self.crypto_wallet_url,
            ),
            data=data,
        )

    def authenticate(
        self,
        crypto_wallet_address: str,
        crypto_wallet_type: str,
        signature: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ):
        data: Dict[str, Any] = {
            "crypto_wallet_address": crypto_wallet_address,
            "crypto_wallet_type": crypto_wallet_type,
            "signature": signature,
        }
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims:
            data["session_custom_claims"] = session_custom_claims

        return self._post(
            "{0}/authenticate".format(
                self.crypto_wallet_url,
            ),
            data=data,
        )
