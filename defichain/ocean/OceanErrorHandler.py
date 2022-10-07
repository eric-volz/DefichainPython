from defichain.exceptions.http.BadRequest import BadRequest
from defichain.exceptions.http.Unauthorized import Unauthorized
from defichain.exceptions.http.Forbidden import Forbidden
from defichain.exceptions.http.NotFound import NotFound
from defichain.exceptions.http.BadMethod import BadMethod
from defichain.exceptions.http.UnprocessableEntity import UnprocessableEntity
from defichain.exceptions.http.InternalServerError import InternalServerError
from defichain.exceptions.http.ServiceUnavailable import ServiceUnavailable


STATUS_CODES_WITH_ERROR = [400, 401, 403, 404, 405, 422, 500, 503]


class OceanErrorHandler:
    def __init__(self, response):
        self.statusCode = response.status_code

        if self.statusCode in STATUS_CODES_WITH_ERROR:
            if self.statusCode == 401:
                raise Unauthorized()
            else:
                self.response_text = response.json()
                if 'error' in self.response_text and self.response_text['error'] is not None:
                    msg = self.response_text["error"]
                    if self.statusCode == 400:
                        raise BadRequest(f"{msg}")
                    if self.statusCode == 403:
                        raise Forbidden(f"{msg}")
                    if self.statusCode == 404:
                        raise NotFound(f"{msg}")
                    if self.statusCode == 405:
                        raise BadMethod(f"{msg}")
                    if self.statusCode == 422:
                        raise UnprocessableEntity(f"{msg}")
                    if self.statusCode == 500:
                        raise InternalServerError(f"{msg}")
                    if self.statusCode == 503:
                        raise ServiceUnavailable(f"{msg}")
