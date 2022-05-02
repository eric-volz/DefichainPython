# RPC Error Codes
# https://github.com/bitcoin/bitcoin/blob/master/src/rpc/protocol.h

from defichain.exceptions.RPCErrorCode import RPCErrorCode

from defichain.exceptions.BadRequest import BadRequest
from defichain.exceptions.Unauthorized import Unauthorized
from defichain.exceptions.Forbidden import Forbidden
from defichain.exceptions.NotFound import NotFound
from defichain.exceptions.BadMethod import BadMethod
from defichain.exceptions.InternalServerError import InternalServerError
from defichain.exceptions.ServiceUnavailable import ServiceUnavailable

STATUS_CODES_WITH_ERROR = [400, 401, 403, 404, 405, 500, 503]


class RPCErrorHandler:
    def __init__(self, response):
        self.statusCode = response.status_code

        if self.statusCode in STATUS_CODES_WITH_ERROR:
            if self.statusCode == 401:
                raise Unauthorized()
            else:
                self.response_text = response.json()
                if 'error' in self.response_text and self.response_text['error'] is not None:
                    rpc_code = self.response_text["error"]["code"]
                    rpc_name = RPCErrorCode(rpc_code).name
                    msg = self.response_text["error"]["message"]
                    if self.statusCode == 400:
                        raise BadRequest(f"{rpc_name}: {msg}")
                    if self.statusCode == 403:
                        raise Forbidden(f"{rpc_name}: {msg}")
                    if self.statusCode == 404:
                        raise NotFound(f"{rpc_name}: {msg}")
                    if self.statusCode == 405:
                        raise BadMethod(f"{rpc_name}: {msg}")
                    if self.statusCode == 500:
                        raise InternalServerError(f"{rpc_name}: {msg}")
                    if self.statusCode == 503:
                        raise ServiceUnavailable(f"{rpc_name}: {msg}")
