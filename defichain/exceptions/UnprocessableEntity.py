class UnprocessableEntity(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"UnprocessableEntity(422): {self.message}")
