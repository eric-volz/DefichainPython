import pytest
from . import ocean

SIZE = 30
NEXT = None


@pytest.mark.query
def test_list():  # 01
    assert ocean.oracles.list()
    assert ocean.oracles.list(SIZE, NEXT)
    assert ocean.oracles.list(size=SIZE, next=NEXT)


@pytest.mark.query
def test_getPriceFeed():  # 02
    oracleId = "d6c72ef84c9246b0800a9fb1f76a3c1ec071ff566a2aefc1faa20a4bd204ac14"
    token = "BTC"
    currency = "USD"
    assert ocean.oracles.getPriceFeed(oracleId, token, currency)
    assert ocean.oracles.getPriceFeed(oracleId, token, currency, SIZE, NEXT)
    assert ocean.oracles.getPriceFeed(oracleId=oracleId, token=token, currency=currency, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getOracleByAddress():  # 03
    address = "df1quc4qephru0a2m58ctusw2qx4cmksdqrvayeklg"
    assert ocean.oracles.getOracleByAddress(address)
    assert ocean.oracles.getOracleByAddress(address=address)
