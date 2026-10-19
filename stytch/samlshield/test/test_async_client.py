from __future__ import annotations

import datetime
import ipaddress
import ssl
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

import aiohttp
from aiohttp import web
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

from stytch.samlshield.client import SamlShieldClient


class TestSamlShieldAsyncTransport(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.received: list[tuple[str | None, str | None, dict[str, Any]]] = []

        async def validate(request: web.Request) -> web.Response:
            self.received.append(
                (
                    request.headers.get("Authorization"),
                    request.headers.get("Content-Type"),
                    dict(await request.post()),
                )
            )
            return web.json_response(
                {"status_code": 200, "request_id": "request-test", "message": "valid"}
            )

        self.temp_dir = tempfile.TemporaryDirectory()
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
        now = datetime.datetime.now(datetime.timezone.utc)
        certificate = (
            x509.CertificateBuilder()
            .subject_name(name)
            .issuer_name(name)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now - datetime.timedelta(minutes=1))
            .not_valid_after(now + datetime.timedelta(days=1))
            .add_extension(
                x509.SubjectAlternativeName(
                    [x509.IPAddress(ipaddress.ip_address("127.0.0.1"))]
                ),
                critical=False,
            )
            .sign(key, hashes.SHA256())
        )
        cert_path = Path(self.temp_dir.name) / "cert.pem"
        key_path = Path(self.temp_dir.name) / "key.pem"
        cert_path.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))
        key_path.write_bytes(
            key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            )
        )
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(cert_path, key_path)
        app = web.Application()
        app.router.add_post("/v1/saml/validate", validate)
        self.runner = web.AppRunner(app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, "127.0.0.1", 0, ssl_context=context)
        await self.site.start()
        port = self.runner.addresses[0][1]
        self.base_url = f"https://127.0.0.1:{port}"

    async def asyncTearDown(self) -> None:
        await self.runner.cleanup()
        self.temp_dir.cleanup()

    async def test_public_validate_async_uses_bearer_form_and_timeout(self) -> None:
        await self._validate(37, 37)

    async def test_public_validate_async_uses_default_timeout(self) -> None:
        await self._validate(None, 600)

    async def test_public_validate_async_can_reuse_the_external_session(self) -> None:
        await self._validate(37, 37, calls=2)

    async def _validate(
        self, timeout: int | None, expected: int, calls: int = 1
    ) -> None:
        # Trust only the locally generated test certificate for this session.
        context = ssl.create_default_context(
            cafile=str(Path(self.temp_dir.name) / "cert.pem")
        )
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=context)
        ) as session:
            client = SamlShieldClient(
                public_token="public-test",
                timeout=timeout,
                async_session=session,
                custom_base_url=self.base_url,
            )
            with patch.object(session, "post", wraps=session.post) as post:
                for _ in range(calls):
                    result = await client.saml.validate_async(saml_response="a+b/c=")
                    self.assertEqual(result.message, "valid")
                self.assertEqual(post.call_count, calls)
                for call in post.call_args_list:
                    self.assertNotIn("auth", call.kwargs)
                    self.assertEqual(call.kwargs["timeout"].total, expected)
            await client.async_client.close()
            self.assertFalse(session.closed)
        self.assertEqual(
            self.received,
            [
                (
                    "Bearer public-test",
                    "application/x-www-form-urlencoded",
                    {"SAMLResponse": "a+b/c="},
                )
            ]
            * calls,
        )
