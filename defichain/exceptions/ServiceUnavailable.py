class ServiceUnavailable(Exception):
    """
    The server cannot handle the request.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"Service Unavailable(503): {self.message}")
