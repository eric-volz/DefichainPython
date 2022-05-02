class InternalServerError(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"InternalServerError(500): {self.message}")
