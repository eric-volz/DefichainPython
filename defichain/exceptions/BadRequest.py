class BadRequest(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"BadRequest(400): {self.message}")
