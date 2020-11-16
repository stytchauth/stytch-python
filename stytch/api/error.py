class StytchError(Exception):
    def __init__(
        self,
        request_id: str,
        error_type: str,
        error_message: str,
        error_url: str,
        **kwargs
    ):
        self.request_id = request_id
        self.error_type = error_type
        self.error_message = error_message
        self.error_url = error_url

    def __repr__(self):
        return "StytchError {0}".format(self.__dict__)
