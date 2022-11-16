# RPC Error Codes
# https://github.com/bitcoin/bitcoin/blob/master/src/rpc/protocol.h
from defichain.logger import Logger
from defichain.exceptions.http.RPCErrorCode import RPCErrorCode

from defichain.exceptions.http.BadRequest import BadRequest
from defichain.exceptions.http.Unauthorized import Unauthorized
from defichain.exceptions.http.Forbidden import Forbidden
from defichain.exceptions.http.NotFound import NotFound
from defichain.exceptions.http.BadMethod import BadMethod
from defichain.exceptions.http.InternalServerError import InternalServerError
from defichain.exceptions.http.ServiceUnavailable import ServiceUnavailable

STATUS_CODES_WITH_ERROR = [400, 401, 403, 404, 405, 500, 503]


class RPCErrorHandler:
    def __init__(self, response, logger: Logger):
        self.statusCode = response.status_code
        self.logger = logger

        if self.statusCode in STATUS_CODES_WITH_ERROR:
            if self.statusCode == 401:
                if logger:
                    self.logger.error("NodeError", f"Unauthorized")
                raise Unauthorized()
            else:
                self.response_text = response.json()
                if 'error' in self.response_text and self.response_text['error'] is not None:
                    rpc_code = self.response_text["error"]["code"]
                    rpc_name = RPCErrorCode(rpc_code).name
                    msg = self.response_text["error"]["message"]
                    if self.statusCode == 400:
                        if logger:
                            self.logger.error("NodeError", f"BadRequest: {rpc_name}: {msg}")
                        raise BadRequest(f"{rpc_name}: {msg}")
                    if self.statusCode == 403:
                        if logger:
                            self.logger.error("NodeError", f"Forbidden: {rpc_name}: {msg}")
                        raise Forbidden(f"{rpc_name}: {msg}")
                    if self.statusCode == 404:
                        if logger:
                            self.logger.error("NodeError", f"NotFound: {rpc_name}: {msg}")
                        raise NotFound(f"{rpc_name}: {msg}")
                    if self.statusCode == 405:
                        if logger:
                            self.logger.error("NodeError", f"BadMethod: {rpc_name}: {msg}")
                        raise BadMethod(f"{rpc_name}: {msg}")
                    if self.statusCode == 500:
                        if logger:
                            self.logger.error("NodeError", f"InternalServerError: {rpc_name}: {msg}")
                        raise InternalServerError(f"{rpc_name}: {msg}")
                    if self.statusCode == 503:
                        if logger:
                            self.logger.error("NodeError", f"ServiceUnavailable: {rpc_name}: {msg}")
                        raise ServiceUnavailable(f"{rpc_name}: {msg}")
