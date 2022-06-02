class Unauthorized(Exception):
    """
    Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided.
    """
    def __init__(self):
        super().__init__(f"Unauthorized(401): Authorization failed: Incorrect rpcuser or rpcpassword")
