from defichain.src.exceptions.RPCErrorCode import RPCErrorCode


class BadMethod(Exception):
    def __init__(self, code, msg):
        self.message = msg
        self.rpcErrorCode = RPCErrorCode(code).name
        super().__init__(f"Bad Method(405): {self.rpcErrorCode}: {self.message}")
