from defichain.src.exceptions.RPCErrorCode import RPCErrorCode


class NotFound(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"NotFound(404): {self.rpcErrorCode}: {self.message}")
