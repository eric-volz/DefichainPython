class Unauthorized(Exception):
    def __init__(self):
        super().__init__(f"Unauthorized(401): Authorization failed: Incorrect rpcuser or rpcpassword")
