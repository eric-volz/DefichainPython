class BadRequest(Exception):
    """
    The server cannot or will not process the request due to an apparent client error.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"BadRequest(400): {self.message}")
