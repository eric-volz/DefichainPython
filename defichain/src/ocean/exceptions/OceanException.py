from .HTTPStatusCode import HttpStatusCode
from .RPCErrorCode import RPCErrorCode


class OceanException(Exception):
    def __init__(self, httpErrorCode, args):
        error_string = "\n"
        httpErrorName = HttpStatusCode(httpErrorCode).name
        error_string += f"{httpErrorName} ({httpErrorCode}): \n"
        for arg in args:

            if arg[0] == "message":
                rpcErrorCode = None
                rpcErrorName = None
                split = arg[1].split(", ")
                msg = split[0]
                for string in split:
                    if "code" in string:
                        split = string.split(" ")
                        rpcErrorCode = int(split[1])
                        rpcErrorName = RPCErrorCode(rpcErrorCode).name
                if rpcErrorCode:
                    error_string += f"{rpcErrorName} ({rpcErrorCode}) \n"
                if msg:
                    error_string += f"message: {msg} \n"
            else:
                error_string += f"{arg[0]}: {arg[1]} \n"
        super().__init__(error_string)
