from defichain.src.exceptions.RPCErrorCode import RPCErrorCode


class InternalServerError(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"InternalServerError(500): {self.rpcErrorCode}: {self.message}")
