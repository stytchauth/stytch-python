from typing import Any, Dict, List, Optional

from .base import Base, _validate_attributes

class Passwords(Base):
    def __init__(self, client):
        super().__init__(client)
        self.email = Email(client)
        self.existing_password = ExistingPassword(client)
        self.session = Session(client)

    @property
    def password_url(self):
        return self.get_url("passwords")

    def create(
        self,
        email: str,
        password: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ):
        data: Dict[str, Any] = {
            "email": email,
            "password": password,
        }
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims:
            data["session_custom_claims"] = session_custom_claims

        return self._post(self.password_url, data=data)

    def authenticate(
        self,
        email: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ):
        data: Dict[str, Any] = {
            "email": email,
            "password": password,
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
                self.password_url,
            ),
            data=data,
        )

    def strength_check(
        self,
        password: str,
        email: Optional[str] = None,
    ):
        data: Dict[str, Any] = {
            "password": password,
        }
        if email:
            data["email"] = email

        return self._post(
            "{0}/strength_check".format(
                self.password_url,
            ),
            data=data,
        )

    def migrate(
        self,
        email: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
    ):
        data: Dict[str, Any] = {
            "email": email,
            "hash": hash,
            "hash_type": hash_type,
        }
        if md_5_config:
            data["md_5_config"] = md_5_config
        if argon_2_config:
            data["argon_2_config"] = argon_2_config
        if sha_1_config:
            data["sha_1_config"] = sha_1_config
        if scrypt_config:
            data["scrypt_config"] = scrypt_config

        return self._post(
            "{0}/migrate".format(
                self.password_url,
            ),
            data=data,
        )

class Email(Base):
    @property
    def password_url(self):
        return self.get_url("passwords/email")

    def reset_start(
        self,
        email: str,
        login_redirect_url: Optional[str] = None,
        reset_password_redirect_url: Optional[str] = None,
        reset_password_expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        code_challenge: Optional[str] = None,
        locale: Optional[str] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        data: Dict[str, Any] = {
            "email": email,
        }
        if login_redirect_url:
            data["login_redirect_url"] = login_redirect_url
        if reset_password_redirect_url:
            data["reset_password_redirect_url"] = reset_password_redirect_url
        if reset_password_expiration_minutes:
            data["reset_password_expiration_minutes"] = reset_password_expiration_minutes
        if attributes:
            data["attributes"] = attributes
        if code_challenge:
            data["code_challenge"] = code_challenge
        if locale:
            data["locale"] = locale

        return self._post(
            "{0}/reset/start".format(
                self.password_url,
            ),
            data=data,
        )

    def reset(
        self,
        token: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        attributes: Optional[Dict] = None,
        options: Optional[Dict] = None,
        code_verifier: Optional[str] = None,
    ):
        if attributes:
            attributes = _validate_attributes(attributes)

        data: Dict[str, Any] = {
            "token": token,
            "password": password,
        }
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims:
            data["session_custom_claims"] = session_custom_claims
        if attributes:
            data["attributes"] = attributes
        if options:
            data["options"] = options
        if code_verifier:
            data["code_verifier"] = code_verifier

        return self._post(
            "{0}/reset".format(
                self.password_url,
            ),
            data=data,
        )

class ExistingPassword(Base):
    @property
    def password_url(self):
        return self.get_url("passwords/existing_password")

    def reset(
            self,
            email: str,
            existing_password: str,
            new_password: str,
            session_token: Optional[str] = None,
            session_jwt: Optional[str] = None,
            session_duration_minutes: Optional[int] = None,
            session_custom_claims: Optional[Dict[str, Any]] = None,
    ):
        data: Dict[str, Any] = {
            "email": email,
            "new_password": new_password,
            "existing_password": existing_password,
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
            "{0}/reset".format(
                self.password_url,
            ),
            data=data,
        )

class Session(Base):
    @property
    def password_url(self):
        return self.get_url("passwords/session")

    def reset(
            self,
            password: str,
            session_token: Optional[str] = None,
            session_jwt: Optional[str] = None,
    ):
        data: Dict[str, Any] = {
            "password": password,
        }
        if session_token:
            data["session_token"] = session_token
        if session_jwt:
            data["session_jwt"] = session_jwt

        return self._post(
            "{0}/reset".format(
                self.password_url,
            ),
            data=data,
        )
