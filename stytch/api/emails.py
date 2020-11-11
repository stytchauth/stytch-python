from .base import Base


class Emails(Base):
    @property
    def emails_url(self):
        return self.get_url("emails")

    def send_email_verification(
        self,
        email_id: str,
        user_id: str,
        magic_link_url: str,
        expiration_minutes: int = 10,
    ):
        return self._post(
            "{0}/{1}/send_verification".format(self.emails_url, email_id),
            data={
                "user_id": user_id,
                "email_id": email_id,
                "magic_link_url": magic_link_url,
                "expiration_minutes": expiration_minutes,
            },
        )

    def verify_email(
        self,
        token: str,
    ):
        return self._post(
            "{0}/{1}/verify".format(
                self.emails_url,
                token,
            ),
            data={},
        )

    def delete_email(
        self,
        email_id: str,
        user_id: str,
    ):
        return self._delete(
            "{0}/{1}/users/{2}".format(self.emails_url, email_id, user_id),
        )
