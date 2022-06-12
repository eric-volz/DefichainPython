class ServiceUnavailable(Exception):
    """
    The server cannot handle the request.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"ServiceUnavailable(503): {self.message}")
