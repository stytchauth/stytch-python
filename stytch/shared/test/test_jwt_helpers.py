import unittest, time
import jwt
from jwt import algorithms
from stytch.shared import jwt_helpers

PROJECT_ID = "project-test-123"
BASE_URL = "https://custom.example.com/"
BASE_URL_CUSTOM_ISSUER = "https://custom.example.com"
DEFAULT_ISSUER = f"stytch.com/{PROJECT_ID}"

def _generate_rsa_key():
    from cryptography.hazmat.primitives.asymmetric import rsa
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

PRIVATE_KEY, PUBLIC_KEY = _generate_rsa_key()

def _generate_token(issuer: str):
    now = int(time.time())
    payload = {
        "aud": PROJECT_ID,
        "iss": issuer,
        "sub": "user-123",
        "exp": now + 300,
        "iat": now,
        "nbf": now,
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")


class FakeJWKClient:
    def __init__(self, public_key):
        self._public_key = public_key

    def get_signing_key_from_jwt(self, _):
        class _Key:
            key = self._public_key

        return _Key()


class TestJWTLocalIssuer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jwks = FakeJWKClient(PUBLIC_KEY)

    def test_default_issuer_allowed(self):
        token = _generate_token(DEFAULT_ISSUER)
        claims = jwt_helpers.authenticate_jwt_local(
            jwks_client=self.jwks,
            project_id=PROJECT_ID,
            jwt=token,
            base_url=BASE_URL,
        )
        self.assertIsNotNone(claims)

    def test_custom_issuer_allowed(self):
        token = _generate_token(BASE_URL_CUSTOM_ISSUER)
        claims = jwt_helpers.authenticate_jwt_local(
            jwks_client=self.jwks,
            project_id=PROJECT_ID,
            jwt=token,
            base_url=BASE_URL,
        )
        self.assertIsNotNone(claims)

    def test_invalid_issuer_rejected(self):
        token = _generate_token("invalid.com/xyz")
        claims = jwt_helpers.authenticate_jwt_local(
            jwks_client=self.jwks,
            project_id=PROJECT_ID,
            jwt=token,
            base_url=BASE_URL,
        )
        self.assertIsNone(claims) 
