class Forbidden(Exception):
    """
    The request contained valid data and was understood by the server, but the server is refusing action.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"Forbidden(403): {self.message}")
