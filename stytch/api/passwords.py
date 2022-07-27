from typing import Any, Dict, List, Optional

from .base import Base, _validate_attributes

class Passwords(Base):
    def __init__(self, client):
        super().__init__(client)
        self.email = Email(client)

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
        prepend_salt: Optional[str] = None,
        append_salt: Optional[str] = None,
        argon_2_salt: Optional[str] = None,
        argon_2_iteration_amount: Optional[str] = None,
        argon_2_memory: Optional[str] = None,
        argon_2_threads: Optional[str] = None,
        argon_2_key_length: Optional[str] = None,
    ):
        data: Dict[str, Any] = {
            "email": email,
            "hash": hash,
            "hash_type": hash_type,
        }
        if prepend_salt:
            data["prepend_salt"] = prepend_salt
        if append_salt:
            data["append_salt"] = append_salt
        if argon_2_salt:
            data["argon_2_salt"] = argon_2_salt
        if argon_2_iteration_amount:
            data["argon_2_iteration_amount"] = argon_2_iteration_amount
        if argon_2_memory:
            data["argon_2_memory"] = argon_2_memory
        if argon_2_threads:
            data["argon_2_threads"] = argon_2_threads
        if argon_2_key_length:
            data["argon_2_key_length"] = argon_2_key_length

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