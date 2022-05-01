# RPC Error Codes
# https://github.com/bitcoin/bitcoin/blob/master/src/rpc/protocol.h

from defichain.src.exceptions.HTTPStatusCode import HTTPStatusCode

from defichain.src.exceptions.BadRequest import BadRequest
from defichain.src.exceptions.Unauthorized import Unauthorized
from defichain.src.exceptions.Forbidden import Forbidden
from defichain.src.exceptions.NotFound import NotFound
from defichain.src.exceptions.BadMethod import BadMethod
from defichain.src.exceptions.InternalServerError import InternalServerError
from defichain.src.exceptions.ServiceUnavailable import ServiceUnavailable


class RPCErrorHandler:
    def __init__(self, response):
        self.statusCode = response.status_code

        if self.statusCode == HTTPStatusCode.HTTP_UNAUTHORIZED.value:
            raise Unauthorized()
        else:
            self.response = response.json()
            if 'error' in self.response and self.response['error'] is not None:
                code = self.response["error"]["code"]
                msg = self.response["error"]["message"]
                if self.statusCode == HTTPStatusCode.HTTP_BAD_REQUEST.value:
                    raise BadRequest(code, msg)
                elif self.statusCode == HTTPStatusCode.HTTP_FORBIDDEN.value:
                    raise Forbidden(code, msg)
                elif self.statusCode == HTTPStatusCode.HTTP_NOT_FOUND.value:
                    raise NotFound(code, msg)
                elif self.statusCode == HTTPStatusCode.HTTP_BAD_METHOD.value:
                    raise BadMethod(code, msg)
                elif self.statusCode == HTTPStatusCode.HTTP_INTERNAL_SERVER_ERROR.value:
                    raise InternalServerError(code, msg)
                elif self.statusCode == HTTPStatusCode.HTTP_SERVICE_UNAVAILABLE.value:
                    raise ServiceUnavailable(code, msg)
