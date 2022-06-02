class WrongParameters(Exception):
    """
    If the expected paremeters were not passed.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"WrongParameters: {self.message}")
