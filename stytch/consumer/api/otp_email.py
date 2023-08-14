# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.consumer.models.attribute import Attributes
from stytch.consumer.models.otp_email import (
    LoginOrCreateRequestLocale,
    LoginOrCreateResponse,
    SendRequestLocale,
    SendResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Email:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def send(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Attributes] = None,
        locale: Optional[SendRequestLocale | str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendResponse:
        """Send a one-time passcode (OTP) to a User using their email. If you'd like to create a user and send them a passcode with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email-otp).

        ### Add an email to an existing user
        This endpoint also allows you to add a new email to an existing Stytch User. Including a `user_id`, `session_token`, or `session_jwt` in the request will add the email to the pre-existing Stytch User upon successful authentication.

        Adding a new email to an existing Stytch User requires the User to be present and validate the email via OTP. This requirement is in place to prevent account takeover attacks.

        ### Next steps
        Collect the OTP which was delivered to the user. Call [Authenticate OTP](https://stytch.com/docs/api/authenticate-otp) using the OTP `code` along with the `phone_id` found in the response as the `method_id`.

        Fields:
          - email: The email address of the user to send the one-time passcode to. You may use sandbox@stytch.com to test this endpoint, see [Testing](https://stytch.com/docs/home#resources_testing) for more detail.
          - expiration_minutes: Set the expiration for the one-time passcode, in minutes. The minimum expiration is 1 minute and the maximum is 10 minutes. The default expiration is 2 minutes.
          - attributes: Provided attributes help with fraud detection.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - user_id: The unique ID of a specific User.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
        """  # noqa
        data: Dict[str, Any] = {
            "email": email,
        }
        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if locale is not None:
            data["locale"] = locale
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id

        url = self.api_base.url_for("/v1/otps/email/send", data)
        res = self.sync_client.post(url, data)
        return SendResponse.from_json(res.response.status_code, res.json)

    async def send_async(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Attributes] = None,
        locale: Optional[SendRequestLocale] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendResponse:
        """Send a one-time passcode (OTP) to a User using their email. If you'd like to create a user and send them a passcode with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email-otp).

        ### Add an email to an existing user
        This endpoint also allows you to add a new email to an existing Stytch User. Including a `user_id`, `session_token`, or `session_jwt` in the request will add the email to the pre-existing Stytch User upon successful authentication.

        Adding a new email to an existing Stytch User requires the User to be present and validate the email via OTP. This requirement is in place to prevent account takeover attacks.

        ### Next steps
        Collect the OTP which was delivered to the user. Call [Authenticate OTP](https://stytch.com/docs/api/authenticate-otp) using the OTP `code` along with the `phone_id` found in the response as the `method_id`.

        Fields:
          - email: The email address of the user to send the one-time passcode to. You may use sandbox@stytch.com to test this endpoint, see [Testing](https://stytch.com/docs/home#resources_testing) for more detail.
          - expiration_minutes: Set the expiration for the one-time passcode, in minutes. The minimum expiration is 1 minute and the maximum is 10 minutes. The default expiration is 2 minutes.
          - attributes: Provided attributes help with fraud detection.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - user_id: The unique ID of a specific User.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
        """  # noqa
        data: Dict[str, Any] = {
            "email": email,
        }
        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if locale is not None:
            data["locale"] = locale
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id

        url = self.api_base.url_for("/v1/otps/email/send", data)
        res = await self.async_client.post(url, data)
        return SendResponse.from_json(res.response.status, res.json)

    def login_or_create(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Attributes] = None,
        create_user_as_pending: Optional[bool] = None,
        locale: Optional[LoginOrCreateRequestLocale | str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        """Send a one-time passcode (OTP) to a User using their email. If the email is not associated with a User already, a User will be created.

        ### Next steps

        Collect the OTP which was delivered to the User. Call [Authenticate OTP](https://stytch.com/docs/api/authenticate-otp) using the OTP `code` along with the `phone_id` found in the response as the `method_id`.

        Fields:
          - email: The email address of the user to send the one-time passcode to. You may use sandbox@stytch.com to test this endpoint, see [Testing](https://stytch.com/docs/home#resources_testing) for more detail.
          - expiration_minutes: Set the expiration for the one-time passcode, in minutes. The minimum expiration is 1 minute and the maximum is 10 minutes. The default expiration is 2 minutes.
          - attributes: Provided attributes help with fraud detection.
          - create_user_as_pending: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false.
                If true, users will be saved with status pending in Stytch's backend until authenticated.
                If false, users will be created as active. An example usage of
                a true flag would be to require users to verify their phone by entering the OTP code before creating
                an account for them.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
        """  # noqa
        data: Dict[str, Any] = {
            "email": email,
        }
        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if create_user_as_pending is not None:
            data["create_user_as_pending"] = create_user_as_pending
        if locale is not None:
            data["locale"] = locale
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id

        url = self.api_base.url_for("/v1/otps/email/login_or_create", data)
        res = self.sync_client.post(url, data)
        return LoginOrCreateResponse.from_json(res.response.status_code, res.json)

    async def login_or_create_async(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Attributes] = None,
        create_user_as_pending: Optional[bool] = None,
        locale: Optional[LoginOrCreateRequestLocale] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        """Send a one-time passcode (OTP) to a User using their email. If the email is not associated with a User already, a User will be created.

        ### Next steps

        Collect the OTP which was delivered to the User. Call [Authenticate OTP](https://stytch.com/docs/api/authenticate-otp) using the OTP `code` along with the `phone_id` found in the response as the `method_id`.

        Fields:
          - email: The email address of the user to send the one-time passcode to. You may use sandbox@stytch.com to test this endpoint, see [Testing](https://stytch.com/docs/home#resources_testing) for more detail.
          - expiration_minutes: Set the expiration for the one-time passcode, in minutes. The minimum expiration is 1 minute and the maximum is 10 minutes. The default expiration is 2 minutes.
          - attributes: Provided attributes help with fraud detection.
          - create_user_as_pending: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false.
                If true, users will be saved with status pending in Stytch's backend until authenticated.
                If false, users will be created as active. An example usage of
                a true flag would be to require users to verify their phone by entering the OTP code before creating
                an account for them.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
        """  # noqa
        data: Dict[str, Any] = {
            "email": email,
        }
        if expiration_minutes is not None:
            data["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if create_user_as_pending is not None:
            data["create_user_as_pending"] = create_user_as_pending
        if locale is not None:
            data["locale"] = locale
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id

        url = self.api_base.url_for("/v1/otps/email/login_or_create", data)
        res = await self.async_client.post(url, data)
        return LoginOrCreateResponse.from_json(res.response.status, res.json)
