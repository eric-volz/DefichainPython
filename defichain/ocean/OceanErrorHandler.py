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
        self.logger_error = None
        if logger:
            self.logger_error = logger.get_error_logger("OceanError")

        if self.statusCode in STATUS_CODES_WITH_ERROR:
            if self.statusCode == 401:
                if self.logger_error:
                    self.logger_error.error(f"Unauthorized")
                raise Unauthorized()
            else:
                self.response_text = response.json()
                if 'error' in self.response_text and self.response_text['error'] is not None:
                    msg = self.response_text["error"]
                    if self.statusCode == 400:
                        if self.logger_error:
                            self.logger_error.error(f"BadRequest {msg}")
                        raise BadRequest(f"{msg}")
                    if self.statusCode == 403:
                        if self.logger_error:
                            self.logger_error.error(f"Forbidden {msg}")
                        raise Forbidden(f"{msg}")
                    if self.statusCode == 404:
                        if self.logger_error:
                            self.logger_error.error(f"NotFound {msg}")
                        raise NotFound(f"{msg}")
                    if self.statusCode == 405:
                        if self.logger_error:
                            self.logger_error.error(f"BadMethod {msg}")
                        raise BadMethod(f"{msg}")
                    if self.statusCode == 422:
                        if self.logger_error:
                            self.logger_error.error(f"UnprocessableEntity {msg}")
                        raise UnprocessableEntity(f"{msg}")
                    if self.statusCode == 500:
                        if self.logger_error:
                            self.logger_error.error(f"InternalServerError {msg}")
                        raise InternalServerError(f"{msg}")
                    if self.statusCode == 503:
                        if self.logger_error:
                            self.logger_error.error(f"ServiceUnavailable {msg}")
                        raise ServiceUnavailable(f"{msg}")
