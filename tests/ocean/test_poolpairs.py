import pytest
from . import ocean

SIZE = 30
NEXT = None


@pytest.mark.query
def test_list():  # 01
    assert ocean.poolpairs.list()
    assert ocean.poolpairs.list(SIZE, NEXT)
    assert ocean.poolpairs.list(size=SIZE, next=NEXT)


@pytest.mark.query
def test_get():  # 02
    id = 4  # ETH-DFI
    assert ocean.poolpairs.get(id)
    assert ocean.poolpairs.get(id=id)


@pytest.mark.query
def test_listPoolSwaps():  # 03
    id = 4  # ETH-DFI
    assert ocean.poolpairs.listPoolSwaps(id)
    assert ocean.poolpairs.listPoolSwaps(id, SIZE, NEXT)
    assert ocean.poolpairs.listPoolSwaps(id=id, size=SIZE, next=NEXT)


@pytest.mark.query
def test_listPoolSwapsVerbose():  # 04
    id = 4  # ETH-DFI
    assert ocean.poolpairs.listPoolSwapsVerbose(id)
    assert ocean.poolpairs.listPoolSwapsVerbose(id, SIZE, NEXT)
    assert ocean.poolpairs.listPoolSwapsVerbose(id=id, size=SIZE, next=NEXT)


@pytest.mark.query
def test_listPoolSwapAggregates():  # 05
    id = 4  # ETH-DFI
    interval = 3600
    assert ocean.poolpairs.listPoolSwapAggregates(id, interval)
    assert ocean.poolpairs.listPoolSwapAggregates(id, interval, SIZE, NEXT)
    assert ocean.poolpairs.listPoolSwapAggregates(id=id, interval=interval, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getSwappableTokens():  # 06
    tokenId = 0  # DFI
    assert ocean.poolpairs.getSwappableTokens(tokenId)
    assert ocean.poolpairs.getSwappableTokens(tokenId=tokenId)


@pytest.mark.query
def test_getBestPath():  # 07
    fromTokenId = 0  # DFI
    toTokenId = 26  # SPY
    assert ocean.poolpairs.getBestPath(fromTokenId, toTokenId)
    assert ocean.poolpairs.getBestPath(fromTokenId=fromTokenId, toTokenId=toTokenId)


@pytest.mark.query
def test_getAllPaths():  # 08
    fromTokenId = 0  # DFI
    toTokenId = 26  # SPY
    assert ocean.poolpairs.getAllPaths(fromTokenId, toTokenId)
    assert ocean.poolpairs.getAllPaths(fromTokenId=fromTokenId, toTokenId=toTokenId)


@pytest.mark.query
def test_listDexPrices():  # 09
    assert ocean.poolpairs.listDexPrices("DUSD")
    assert ocean.poolpairs.listDexPrices(denomination="DUSD")
