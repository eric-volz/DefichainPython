
class RawTransactionError(Exception):
    def __init__(self, msg):
        super().__init__(f"RawTransactionError: {msg}")
