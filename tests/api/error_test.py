import json
import pytest

from stytch.api.error import StytchError

class TestStytchError:
    def test_traceback_message(self):
        response = """
        {
          "request_id": "request-id-test-59331c7a-e4d6-41dc-aa3f-65f5cc3fdfdc",
          "error_type": "invalid_email",
          "error_message": "Email format is invalid",
          "error_url": "https://stytch.com/docs/api/errors/400"
        }
        """

        with pytest.raises(StytchError, match="Email format is invalid"):
            raise StytchError(**json.loads(response))
