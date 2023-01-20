class TokenError(Exception):
    def __init__(self, msg):
        super().__init__(f"TokensError: {msg}")