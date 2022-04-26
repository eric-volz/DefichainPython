import pytest
from tests.node.util import createNode

# Import Exceptions
from defichain.src.node.exceptions.InternalServerError import InternalServerError

node = createNode()


@pytest.mark.query
def test_appointoracle():  # 01
    address = "df1qxejhhu8xjx5mfh33khaz2fnlt8jwcyar450gtr"
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.appointoracle(address=address, pricefeeds=[{"currency": "USD", "token": "BTC"}],
                                              weightage=20)


@pytest.mark.query
def test_getfixedintervalprice():  # 02
    fixedIntervalPriceId = "DFI/USD"
    assert node.oracles.getfixedintervalprice(fixedIntervalPriceId=fixedIntervalPriceId)


@pytest.mark.query
def test_getfutureswapblock():  # 03
    assert node.oracles.getfutureswapblock()


@pytest.mark.query
def test_getoracledata():  # 04
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    assert node.oracles.getoracledata(oracleid=oracleid)


@pytest.mark.query
def test_getprice():  # 05
    currency = "USD"
    token = "DFI"
    assert node.oracles.getprice(currency=currency, token=token)


@pytest.mark.query
def test_listfixedintervalprices():  # 06
    currency = "USD"
    token = "DFI"
    assert node.oracles.listfixedintervalprices()
    assert node.oracles.listfixedintervalprices(start=f"{token}/{currency}", limit=5)


@pytest.mark.query
def test_listlatestrawprices():  # 07
    currency = "USD"
    token = "DFI"
    start = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    assert node.oracles.listlatestrawprices("USD", "DFI")
    assert node.oracles.listlatestrawprices(currency=currency, token=token, start=start, including_start=True, limit=3)


@pytest.mark.query
def test_listoracles():  # 08
    start = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    assert node.oracles.listoracles()
    assert node.oracles.listoracles(start=start, including_start=True, limit=3)


@pytest.mark.query
def test_listprices():  # 09
    assert node.oracles.listprices()
    assert node.oracles.listprices(start=2, including_start=True, limit=5)


@pytest.mark.query
def test_removeoracle():  # 10
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.removeoracle(oracleid=oracleid, inputs=[])


@pytest.mark.query
def test_setoracledata():  # 11
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    timestamp = 1650994232
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.setoracledata(oracleid=oracleid, timestamp=timestamp, prices=100, inputs=[])


@pytest.mark.query
def test_updateoracle():  # 12
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    timestamp = 1650994232
    pricefeeds = [{"currency": "USD", "token": "DFI"}]
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.updateoracle(oracleid=oracleid, timestamp=timestamp, prices=pricefeeds, weightage=2, inputs=[])
