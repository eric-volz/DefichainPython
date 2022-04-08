from .RPCErrorCode import RPCErrorCode


class BadRequest(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"Bad Request(400): {self.rpcErrorCode}: {self.message}")
