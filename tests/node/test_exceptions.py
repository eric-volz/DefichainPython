import re
import pytest
from defichain.node.RPCErrorHandler import RPCErrorHandler
from requests.models import Response


response = Response()
response._content = b'{"result": "None", "error": {"code": -32600, "message": "Das ist ein Test"}, "id": "None"}'


@pytest.mark.query
def test_BadMethod():  # 01
    response.status_code = 405
    string = "BadMethod(405): RPC_INVALID_REQUEST: Das ist ein Test"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)


@pytest.mark.query
def test_BadRequest():  # 02
    response.status_code = 400
    string = "BadRequest(400): RPC_INVALID_REQUEST: Das ist ein Test"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)


@pytest.mark.query
def test_Forbidden():  # 03
    response.status_code = 403
    string = "Forbidden(403): RPC_INVALID_REQUEST: Das ist ein Test"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)


@pytest.mark.query
def test_InternalServerError():  # 04
    response.status_code = 500
    string = "InternalServerError(500): RPC_INVALID_REQUEST: Das ist ein Test"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)


@pytest.mark.query
def test_NotFound():  # 05
    response.status_code = 404
    string = "NotFound(404): RPC_INVALID_REQUEST: Das ist ein Test"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)


@pytest.mark.query
def test_ServiceUnavailable():  # 06
    response.status_code = 503
    string = "ServiceUnavailable(503): RPC_INVALID_REQUEST: Das ist ein Test"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)


@pytest.mark.query
def test_Unauthorized():  # 07
    response.status_code = 401
    string = "Unauthorized(401): Authorization failed: Incorrect rpcuser or rpcpassword"
    with pytest.raises(Exception, match=re.escape(string)):
        assert RPCErrorHandler(response)
