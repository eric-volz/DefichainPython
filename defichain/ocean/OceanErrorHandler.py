from defichain.logger import Logger
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
    def __init__(self, response, logger: Logger):
        self.statusCode = response.status_code
        self.logger = logger

        if self.statusCode in STATUS_CODES_WITH_ERROR:
            if self.statusCode == 401:
                if logger:
                    self.logger.error("OceanError", f"Unauthorized")
                raise Unauthorized()
            else:
                self.response_text = response.json()
                if 'error' in self.response_text and self.response_text['error'] is not None:
                    msg = self.response_text["error"]
                    if self.statusCode == 400:
                        if logger:
                            self.logger.error("OceanError", f"BadRequest {msg}")
                        raise BadRequest(f"{msg}")
                    if self.statusCode == 403:
                        if logger:
                            self.logger.error("OceanError", f"Forbidden {msg}")
                        raise Forbidden(f"{msg}")
                    if self.statusCode == 404:
                        if logger:
                            self.logger.error("OceanError", f"NotFound {msg}")
                        raise NotFound(f"{msg}")
                    if self.statusCode == 405:
                        if logger:
                            self.logger.error("OceanError", f"BadMethod {msg}")
                        raise BadMethod(f"{msg}")
                    if self.statusCode == 422:
                        if logger:
                            self.logger.error("OceanError", f"UnprocessableEntity {msg}")
                        raise UnprocessableEntity(f"{msg}")
                    if self.statusCode == 500:
                        if logger:
                            self.logger.error("OceanError", f"InternalServerError {msg}")
                        raise InternalServerError(f"{msg}")
                    if self.statusCode == 503:
                        if logger:
                            self.logger.error("OceanError", f"ServiceUnavailable {msg}")
                        raise ServiceUnavailable(f"{msg}")
