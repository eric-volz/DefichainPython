class NotFound(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"NotFound(404): {self.message}")
