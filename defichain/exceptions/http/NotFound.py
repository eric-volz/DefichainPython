class NotFound(Exception):
    """
    The requested resource could not be found but may be available in the future.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"NotFound(404): {self.message}")
