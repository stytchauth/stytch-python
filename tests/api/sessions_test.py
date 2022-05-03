import requests
import json
import jwt
from jwt.utils import to_base64url_uint
from unittest import mock
import time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from testutil import FakeClient, FakeResponse

from stytch.api.sessions import Sessions


def iso(t: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def rsa_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def make_jwt(project_id, key_id, private_key, now, expires_at):
    headers = {
        "kid": key_id,
    }

    # The IDs here belong to the live sandbox project.
    claims = {
        "https://stytch.com/session": {
            "started_at": iso(now),
            "last_accessed_at": iso(now),
            "expires_at": iso(expires_at) if expires_at else None,
            "attributes": {"user_agent": "", "ip_address": ""},
            "authentication_factors": [
                {
                    "delivery_method": "email",
                    "email_factor": {
                        "email_address": "sandbox@stytch.com",
                        "email_id": "email-live-cca9d7d0-11b6-4167-9385-d7e0c9a77418",
                    },
                    "last_authenticated_at": iso(now),
                    "type": "magic_link",
                },
            ],
            "id": "session-live-e26a0ccb-0dc0-4edb-a4bb-e70210f43555",
        },
        "sub": "user-live-fde03dd1-fff7-4b3c-9b31-ead3fbc224de",
        "iat": int(now),
        "nbf": int(now),
        "exp": int(now) + 5 * 60,  # five minutes
        "iss": "stytch.com/{}".format(project_id),
        "aud": [project_id],
    }

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    return jwt.encode(claims, pem, algorithm="RS256", headers=headers)


class LocalJWKSClient:
    def __init__(self, keyset):
        self.keyset = keyset

    def get_signing_key_from_jwt(self, token):
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
        return self.keyset[kid]


def make_jwks_client(key_id, public_key):
    public_numbers = public_key.public_numbers()
    jwk = jwt.PyJWK(
        {
            "kty": "RSA",
            "alg": "RS256",
            "n": to_base64url_uint(public_numbers.n),
            "e": to_base64url_uint(public_numbers.e),
        }
    )
    return LocalJWKSClient({key_id: jwk})


class TestSessions:
    def test_authenticate(self):
        client = FakeClient()
        response = FakeResponse(status_code=200)

        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            sessions = Sessions(client, None)
            sessions._requester_base = requests

            _ = sessions.authenticate(
                session_token="mZAYn5aLEqKUlZ_Ad9U_fWr38GaAQ1oFAhT8ds245v7Q",
                session_duration_minutes=60,
                session_jwt="fake_jwt",
            )

        mock_post.assert_called_once_with(
            "https://localhost:8080/sessions/authenticate",
            data='{"session_token": "mZAYn5aLEqKUlZ_Ad9U_fWr38GaAQ1oFAhT8ds245v7Q", "session_jwt": "fake_jwt", "session_duration_minutes": 60}',
            auth=client.auth,
            headers=mock.ANY,
        )

    def test_authenticate_jwt(self):
        project_id = "project-test-00000000-0000-0000-0000-000000000000"
        now = time.time()

        client = FakeClient(project_id=project_id)

        key_id = "key0"
        private_key = rsa_key()
        jwt = make_jwt(project_id, key_id, private_key, now, now + 3600)
        jwks_client = make_jwks_client(key_id, private_key.public_key())

        response = FakeResponse(status_code=200)
        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            sessions = Sessions(client, jwks_client)
            sessions._requester_base = requests

            # Force remote authentication even though the token is locally valid.
            _ = sessions.authenticate_jwt(
                session_jwt=jwt,
                max_token_age_seconds=0,
            )

        mock_post.assert_called_once_with(
            "https://localhost:8080/sessions/authenticate",
            data=json.dumps({"session_jwt": jwt}),
            auth=client.auth,
            headers=mock.ANY,
        )

    def test_authenticate_jwt_local(self):
        project_id = "project-test-00000000-0000-0000-0000-000000000000"
        now = time.time()

        client = FakeClient(project_id=project_id)

        key_id = "key0"
        private_key = rsa_key()
        jwt = make_jwt(project_id, key_id, private_key, now, now + 3600)
        jwks_client = make_jwks_client(key_id, private_key.public_key())

        response = FakeResponse(status_code=200)
        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            sessions = Sessions(client, jwks_client)
            sessions._requester_base = requests

            session = sessions.authenticate_jwt_local(
                session_jwt=jwt,
                max_token_age_seconds=300,
            )

            assert (
                session["user_id"] == "user-live-fde03dd1-fff7-4b3c-9b31-ead3fbc224de"
            )
            assert session["expires_at"] == iso(int(now) + 3600)
            assert (
                session["session_id"]
                == "session-live-e26a0ccb-0dc0-4edb-a4bb-e70210f43555"
            )
            assert session["attributes"] == {"user_agent": "", "ip_address": ""}
            factors = session["authentication_factors"]
            assert len(factors) == 1

            _ = sessions.authenticate_jwt(
                session_jwt=jwt,
                max_token_age_seconds=300,
            )

        mock_post.assert_not_called()

    def test_authenticate_jwt_local_old_format(self):
        project_id = "project-test-00000000-0000-0000-0000-000000000000"
        now = time.time()

        client = FakeClient(project_id=project_id)

        key_id = "key0"
        private_key = rsa_key()
        jwt = make_jwt(project_id, key_id, private_key, now, None)
        jwks_client = make_jwks_client(key_id, private_key.public_key())

        response = FakeResponse(status_code=200)
        with mock.patch.object(requests, "post", return_value=response) as mock_post:
            sessions = Sessions(client, jwks_client)
            sessions._requester_base = requests

            session = sessions.authenticate_jwt_local(
                session_jwt=jwt,
                max_token_age_seconds=300,
            )

            assert (
                session["user_id"] == "user-live-fde03dd1-fff7-4b3c-9b31-ead3fbc224de"
            )
            assert session["expires_at"] == iso(int(now) + 300)
            assert (
                session["session_id"]
                == "session-live-e26a0ccb-0dc0-4edb-a4bb-e70210f43555"
            )
            assert session["attributes"] == {"user_agent": "", "ip_address": ""}
            factors = session["authentication_factors"]
            assert len(factors) == 1

            _ = sessions.authenticate_jwt(
                session_jwt=jwt,
                max_token_age_seconds=300,
            )

        mock_post.assert_not_called()
