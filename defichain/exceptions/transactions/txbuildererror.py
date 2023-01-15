class TxBuilderError(Exception):
    def __init__(self, msg):
        super().__init__(f"TxBuilderError: {msg}")