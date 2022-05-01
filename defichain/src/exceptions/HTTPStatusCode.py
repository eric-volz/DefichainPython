# RPC Error Codes
# https://github.com/bitcoin/bitcoin/blob/master/src/rpc/protocol.h

from enum import Enum


class HTTPStatusCode(Enum):
    HTTP_OK = 200
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_FORBIDDEN = 403
    HTTP_NOT_FOUND = 404
    HTTP_BAD_METHOD = 405
    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_SERVICE_UNAVAILABLE = 503
