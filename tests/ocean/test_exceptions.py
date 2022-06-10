import re
import pytest
from defichain.ocean.OceanErrorHandler import OceanErrorHandler
from requests.models import Response


response = Response()
response._content = b'{"result": "None", "error": {"code": -32600, "message": "Das ist ein Test"}, "id": "None"}'


@pytest.mark.query
def test_BadMethod():  # 01
    response.status_code = 405
    string = "BadMethod(405): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)


@pytest.mark.query
def test_BadRequest():  # 02
    response.status_code = 400
    string = "BadRequest(400): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)


@pytest.mark.query
def test_Forbidden():  # 03
    response.status_code = 403
    string = "Forbidden(403): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)


@pytest.mark.query
def test_InternalServerError():  # 04
    response.status_code = 500
    string = "InternalServerError(500): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)


@pytest.mark.query
def test_NotFound():  # 05
    response.status_code = 404
    string = "NotFound(404): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)


@pytest.mark.query
def test_ServiceUnavailable():  # 06
    response.status_code = 503
    string = "ServiceUnavailable(503): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)

@pytest.mark.query
def test_UnprocessableEntity():  # 07
    response.status_code = 422
    string = "UnprocessableEntity(422): {'code': -32600, 'message': 'Das ist ein Test'}"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)


@pytest.mark.query
def test_Unauthorized():  # 08
    response.status_code = 401
    string = "Unauthorized(401): Authorization failed: Incorrect rpcuser or rpcpassword"
    with pytest.raises(Exception, match=re.escape(string)):
        assert OceanErrorHandler(response)
