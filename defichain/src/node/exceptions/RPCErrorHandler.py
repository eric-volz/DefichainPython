# RPC Error Codes
# https://github.com/bitcoin/bitcoin/blob/master/src/rpc/protocol.h

from .HTTPStatusCode import HTTPStatusCode

from .BadRequest import BadRequest
from .Unauthorized import Unauthorized
from .Forbidden import Forbidden
from .NotFound import NotFound
from .BadMethod import BadMethod
from .InternalServerError import InternalServerError
from .ServiceUnavailable import ServiceUnavailable


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
