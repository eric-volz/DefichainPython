class Forbidden(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"Forbidden(403): {self.message}")
