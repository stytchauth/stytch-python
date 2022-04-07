class StytchError(Exception):
    def __init__(
        self,
        status_code: int = None,
        request_id: str = None,
        error_type: str = None,
        error_message: str = None,
        error_url: str = None,
        **kwargs
    ):
        self.status_code = status_code
        self.request_id = request_id
        self.error_type = error_type
        self.error_message = error_message
        self.error_url = error_url

    def __repr__(self):
        return "StytchError {0}".format(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

class ClientError(Exception):
    def __init__(self, code: str, message: str, cause: Exception = None):
        super().__init__(self, message)
        self.code = code
        self._message = message
        self.cause = cause

    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(self.__class__.__name__, self.code, self._message, self.cause)

    def __str__(self):
        s = "({}) {}".format(self.code, self._message)
        if self.cause:
            return "{}: {}".format(s, self.cause)
        return s
