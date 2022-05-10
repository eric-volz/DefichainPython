import pytest
from defichain import Ocean

ocean = Ocean()
SIZE = 30
NEXT = None


@pytest.mark.query
def test_list():  # 01
    assert ocean.prices.list()
    assert ocean.prices.list(SIZE, NEXT)
    assert ocean.prices.list(size=SIZE, next=NEXT)


@pytest.mark.query
def test_get():  # 02
    token = "DFI"
    currency = "USD"
    assert ocean.prices.get(token, currency)
    assert ocean.prices.get(token=token, currency=currency)


@pytest.mark.query
def test_getFeedActive():  # 03
    token = "DFI"
    currency = "USD"
    assert ocean.prices.getFeedActive(token, currency)
    assert ocean.prices.getFeedActive(token, currency, SIZE, NEXT)
    assert ocean.prices.getFeedActive(token=token, currency=currency, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getFeed():  # 04
    token = "DFI"
    currency = "USD"
    assert ocean.prices.getFeed(token, currency)
    assert ocean.prices.getFeed(token, currency, SIZE, NEXT)
    assert ocean.prices.getFeed(token=token, currency=currency, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getFeedWithInterval():  # 05
    token = "DFI"
    currency = "USD"
    interval = 3600
    assert ocean.prices.getFeedWithInterval(token, currency, interval)
    assert ocean.prices.getFeedWithInterval(token, currency, interval, SIZE, NEXT)
    assert ocean.prices.getFeedWithInterval(token=token, currency=currency, interval=interval, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getOracles():  # 06
    token = "DFI"
    currency = "USD"
    assert ocean.prices.getOracles(token, currency)
    assert ocean.prices.getOracles(token, currency, SIZE, NEXT)
    assert ocean.prices.getOracles(token=token, currency=currency, size=SIZE, next=NEXT)
