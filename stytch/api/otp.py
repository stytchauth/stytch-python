from typing import Dict, Optional

from .base import _validate_attributes, Base

class OTP(Base):
    def __init__(self, client):
        super().__init__(client)
        self.email = Email(client)
        self.sms = SMS(client)
        self.whatsapp = Whatsapp(client)

    @property
    def otp_url(self):
        return self.get_url("otps")

    def authenticate(
        self,
        method_id: str,
        code: str,
        attributes: Optional[Dict] = None,
        options: Optional[Dict] = None,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
    ):
        attributes = _validate_attributes(attributes)
        options = self._validate_options(options)
        data = {
            "method_id": method_id,
            "code": code,
        }
        if attributes:
            data["attributes"] = attributes
        if options:
            data["options"] = options
        if session_token:
            data["session_token"] = session_token
        if session_duration_minutes:
            data["session_duration_minutes"] = session_duration_minutes

        return self._post(
            "{0}/authenticate".format(
                self.otp_url,
            ),
            data=data,
        )

class SMS(Base):
    @property
    def otp_url(self):
        return self.get_url("otps")

    def send(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/sms/send".format(
                self.otp_url,
            ),
            data=data,
        )

    def login_or_create(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/sms/login_or_create".format(
                self.otp_url,
            ),
            data=data,
        )

class Whatsapp(Base):
    @property
    def otp_url(self):
        return self.get_url("otps")

    def send(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/whatsapp/send".format(
                self.otp_url,
            ),
            data=data,
        )

    def login_or_create(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/whatsapp/login_or_create".format(
                self.otp_url,
            ),
            data=data,
        )

class Email(Base):
    @property
    def otp_url(self):
        return self.get_url("otps")

    def send(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "email": email,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/email/send".format(
                self.otp_url,
            ),
            data=data,
        )

    def login_or_create(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/email/login_or_create".format(
                self.otp_url,
            ),
            data=data,
        )
