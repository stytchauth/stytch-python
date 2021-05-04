from typing import Dict, Optional

from .base import Base

class OTP(Base):
    @property
    def otp_url(self):
        return self.get_url("otp")

    def send_by_sms(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = self._validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/send_by_sms".format(
                self.otp_url,
            ),
            data=data,
        )

    def login_or_create_by_sms(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False
    ):
        attributes = self._validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes
        if create_user_as_pending:
            data["create_user_as_pending"] = create_user_as_pending

        return self._post(
            "{0}/login_or_create".format(
                self.otp_url,
            ),
            data=data,
        )

    def authenticate(
        self,
        method_id: str,
        code: str,
        attributes: Optional[Dict] = None,
        options: Optional[Dict] = None
    ):
        attributes = self._validate_attributes(attributes)
        options = self._validate_options(options)
        data = {
            "method_id": method_id,
            "code": code,
        }
        if attributes:
            data["attributes"] = attributes
        if options:
            data["options"] = options

        return self._post(
            "{0}/authenticate".format(
                self.otp_url,
            ),
            data=data,
        )
