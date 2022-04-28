import pytest
from tests.node.util import createNode

# Import Exceptions
from defichain.src.node.exceptions.InternalServerError import InternalServerError

node = createNode()


@pytest.mark.query
def test_appointoracle():  # 01
    address = "df1qxejhhu8xjx5mfh33khaz2fnlt8jwcyar450gtr"
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    pricefeeds = [{"currency": "USD", "token": "BTC"}]
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.appointoracle(address, pricefeeds, 20, [])
        assert node.oracles.appointoracle(address=address, pricefeeds=pricefeeds, weightage=20, inputs=[])


@pytest.mark.query
def test_getfixedintervalprice():  # 02
    currency = "USD"
    token = "DFI"
    assert node.oracles.getfixedintervalprice(token, currency)
    assert node.oracles.getfixedintervalprice(token=token, currency=currency)


@pytest.mark.query
def test_getfutureswapblock():  # 03
    assert node.oracles.getfutureswapblock()


@pytest.mark.query
def test_getoracledata():  # 04
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    assert node.oracles.getoracledata(oracleid)
    assert node.oracles.getoracledata(oracleid=oracleid)


@pytest.mark.query
def test_getprice():  # 05
    currency = "USD"
    token = "DFI"
    assert node.oracles.getprice(token, currency)
    assert node.oracles.getprice(token=token, currency=currency)


@pytest.mark.query
def test_listfixedintervalprices():  # 06
    currency = "USD"
    token = "DFI"
    assert node.oracles.listfixedintervalprices()
    assert node.oracles.listfixedintervalprices(f"{token}/{currency}", 5)
    assert node.oracles.listfixedintervalprices(start=f"{token}/{currency}", limit=5)


@pytest.mark.query
def test_listlatestrawprices():  # 07
    currency = "USD"
    token = "DFI"
    start = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    assert node.oracles.listlatestrawprices(token, currency, start, True, 3)
    assert node.oracles.listlatestrawprices(token=token, currency=currency, start=start, including_start=True, limit=3)


@pytest.mark.query
def test_listoracles():  # 08
    start = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    assert node.oracles.listoracles()
    assert node.oracles.listoracles(start, True, 3)
    assert node.oracles.listoracles(start=start, including_start=True, limit=3)


@pytest.mark.query
def test_listprices():  # 09
    assert node.oracles.listprices()
    assert node.oracles.listprices(2, True, 5)
    assert node.oracles.listprices(start=2, including_start=True, limit=5)


@pytest.mark.query
def test_removeoracle():  # 10
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.removeoracle(oracleid, [])
        assert node.oracles.removeoracle(oracleid=oracleid, inputs=[])


@pytest.mark.query
def test_setoracledata():  # 11
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    timestamp = 1650994232
    prices = [{"currency": "USD", "tokenAmount": "4@DFI"}]
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Incorrect authorization for .*"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.setoracledata(oracleid, timestamp, prices, [])
        assert node.oracles.setoracledata(oracleid=oracleid, timestamp=timestamp, prices=prices, inputs=[])


@pytest.mark.query
def test_updateoracle():  # 12
    oracleid = "a4492224b78b065d3c044e65e4968e9b326f1b19b615b50f79d3ab58df10f2c5"
    address = "df1qxejhhu8xjx5mfh33khaz2fnlt8jwcyar450gtr"
    pricefeeds = [{"currency": "USD", "token": "DFI"}]
    string = r".*RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.oracles.updateoracle(oracleid, address, pricefeeds, 2, [])
        assert node.oracles.updateoracle(oracleid=oracleid, address=address, pricefeeds=pricefeeds, weightage=2,
                                         inputs=[])
