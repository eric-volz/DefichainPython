
class NotYetSupportedError(Exception):
    def __init__(self):
        super().__init__(f"NotYetSupportedError")
