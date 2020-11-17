class StytchError(Exception):
    def __init__(
        self,
        request_id: str = None,
        error_type: str = None,
        error_message: str = None,
        error_url: str = None,
        **kwargs
    ):
        self.request_id = request_id
        self.error_type = error_type
        self.error_message = error_message
        self.error_url = error_url

    def __repr__(self):
        return "StytchError {0}".format(self.__dict__)
