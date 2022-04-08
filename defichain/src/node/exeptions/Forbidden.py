from .RPCErrorCode import RPCErrorCode


class Forbidden(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"Forbidden(403): {self.rpcErrorCode}: {self.message}")
