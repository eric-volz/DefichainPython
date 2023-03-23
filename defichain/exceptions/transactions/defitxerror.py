class DefiTxError(Exception):
    def __init__(self, msg):
        super().__init__(f"InputError: {msg}")
