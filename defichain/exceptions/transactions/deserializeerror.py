class DeserializeError(Exception):
    def __init__(self, msg):
        super().__init__(f"DeserializeError: {msg}")