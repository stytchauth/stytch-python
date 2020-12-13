from .base import Base


class Emails(Base):
    @property
    def emails_url(self):
        return self.get_url("emails")

    def delete_email(
        self,
        email_id: str,
        user_id: str,
    ):
        return self._delete(
            "{0}/{1}/users/{2}".format(self.emails_url, email_id, user_id),
        )
