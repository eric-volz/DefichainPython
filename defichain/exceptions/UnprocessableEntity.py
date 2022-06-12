class UnprocessableEntity(Exception):
    """
    The request was well-formed but was unable to be followed due to semantic errors.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"UnprocessableEntity(422): {self.message}")
