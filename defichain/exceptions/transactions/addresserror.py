
class AddressError(Exception):
    def __init__(self, msg):
        super().__init__(f"AddressError: {msg}")
