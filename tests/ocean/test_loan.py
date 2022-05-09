import pytest
from defichain import Ocean

ocean = Ocean()
SIZE = 30
NEXT = None


@pytest.mark.query
def test_listScheme():  # 01
    assert ocean.loan.listScheme()
    assert ocean.loan.listScheme(SIZE, NEXT)
    assert ocean.loan.listScheme(size=SIZE, next=NEXT)


@pytest.mark.query
def test_getScheme():  # 02
    scheme = "MIN150"
    assert ocean.loan.getScheme(scheme)
    assert ocean.loan.getScheme(id=scheme)


@pytest.mark.query
def test_listCollateralToken():  # 03
    assert ocean.loan.listCollateralToken()
    assert ocean.loan.listCollateralToken(SIZE, NEXT)
    assert ocean.loan.listCollateralToken(size=SIZE, next=NEXT)


@pytest.mark.query
def test_getCollateralToken():  # 04
    token = 1  # ETH
    assert ocean.loan.getCollateralToken(token)
    assert ocean.loan.getCollateralToken(id=token)


@pytest.mark.query
def test_listLoanToken():  # 05
    assert ocean.loan.listLoanToken()
    assert ocean.loan.listLoanToken(SIZE, NEXT)
    assert ocean.loan.listLoanToken(size=SIZE, next=NEXT)


@pytest.mark.query
def test_getLoanToken():  # 06
    token = 26  # SPY
    assert ocean.loan.getLoanToken(token)
    assert ocean.loan.getLoanToken(id=token)


@pytest.mark.query
def test_listVault():  # 07
    assert ocean.loan.listVault()
    assert ocean.loan.listVault(SIZE, NEXT)
    assert ocean.loan.listVault(size=SIZE, next=NEXT)


@pytest.mark.query
def test_getVault():  # 08
    vault = "fb2dd56658bc2b13fc129539aca8a9ff1f86f8a966a02dbb91c365fc59c1898b"  # SPY
    assert ocean.loan.getVault(vault)
    assert ocean.loan.getVault(id=vault)


@pytest.mark.query
def test_listVaultAuctionHistory():  # 09
    id = "00d1f13efe448980dea15824fd3df82d311a9daeba31428929f827e8c9764e2f"
    height = 1865100
    batchIndex = 0
    assert ocean.loan.listVaultAuctionHistory(id, height, batchIndex)
    assert ocean.loan.listVaultAuctionHistory(id, height, batchIndex, SIZE, NEXT)
    assert ocean.loan.listVaultAuctionHistory(id=id, height=height, batchIndex=batchIndex, size=SIZE, next=NEXT)


@pytest.mark.query
def test_listAction():  # 10
    assert ocean.loan.listAuction()
    assert ocean.loan.listAuction(SIZE, NEXT)
    assert ocean.loan.listAuction(size=SIZE, next=NEXT)
