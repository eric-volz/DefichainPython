from defichain.src.exceptions.RPCErrorCode import RPCErrorCode


class ServiceUnavailable(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"Service Unavailable(503): {self.rpcErrorCode}: {self.message}")
