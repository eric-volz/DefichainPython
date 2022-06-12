class InternalServerError(Exception):
    """
    A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"InternalServerError(500): {self.message}")
