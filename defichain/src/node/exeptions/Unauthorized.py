from .RPCErrorCode import RPCErrorCode


class Unauthorized(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"Unauthorized(401): {self.rpcErrorCode}: {self.message}")
