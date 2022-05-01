from defichain.src.exceptions.HTTPStatusCode import HTTPStatusCode
from defichain.src.exceptions.RPCErrorCode import RPCErrorCode

from defichain.src.exceptions.BadRequest import BadRequest
from defichain.src.exceptions.Unauthorized import Unauthorized
from defichain.src.exceptions.Forbidden import Forbidden
from defichain.src.exceptions.NotFound import NotFound
from defichain.src.exceptions.BadMethod import BadMethod
from defichain.src.exceptions.InternalServerError import InternalServerError
from defichain.src.exceptions.ServiceUnavailable import ServiceUnavailable


class OceanErrorHandler:
    def __init__(self, response):
        self.statusCode = response.status_code

        if self.statusCode == HTTPStatusCode.HTTP_UNAUTHORIZED.value:
            raise Unauthorized()
        else:
            self.response_text = response.json()
            if 'error' in self.response_text and self.response_text['error'] is not None:
                msg = self.response_text["error"]
                if self.statusCode == HTTPStatusCode.HTTP_BAD_REQUEST.value:
                    raise BadRequest(f": {msg}")
                elif self.statusCode == HTTPStatusCode.HTTP_FORBIDDEN.value:
                    raise Forbidden(f": {msg}")
                elif self.statusCode == HTTPStatusCode.HTTP_NOT_FOUND.value:
                    raise NotFound(f": {msg}")
                elif self.statusCode == HTTPStatusCode.HTTP_BAD_METHOD.value:
                    raise BadMethod(f": {msg}")
                elif self.statusCode == HTTPStatusCode.HTTP_INTERNAL_SERVER_ERROR.value:
                    raise InternalServerError(f": {msg}")
                elif self.statusCode == HTTPStatusCode.HTTP_SERVICE_UNAVAILABLE.value:
                    raise ServiceUnavailable(f": {msg}")
