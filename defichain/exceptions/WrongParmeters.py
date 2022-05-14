class WrongParameters(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"WrongParameters: {self.message}")
