import pytest
from . import ocean

ADDRESS = "dN592sZaESZ8qnk4jqd5LgZdJUtCKcjZmQ"
SIZE = 30
NEXT = None


@pytest.mark.query
def test_getAccountHistory():  # 01
    assert ocean.address.getAccountHistory(ADDRESS, 1945985, 24)
    assert ocean.address.getAccountHistory(address=ADDRESS, height=1945985, txno=24)


@pytest.mark.query
def test_listAccountHistory():  # 02
    assert ocean.address.listAccountHistory(ADDRESS)
    assert ocean.address.listAccountHistory(ADDRESS, SIZE, NEXT)
    assert ocean.address.listAccountHistory(address=ADDRESS, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getBalance():  # 03
    assert ocean.address.getBalance(ADDRESS)
    assert ocean.address.getBalance(address=ADDRESS)


@pytest.mark.query
def test_getAggregation():  # 04
    assert ocean.address.getAggregation(ADDRESS)
    assert ocean.address.getAggregation(address=ADDRESS)


@pytest.mark.query
def test_listToken():  # 05
    assert ocean.address.listToken(ADDRESS)
    assert ocean.address.listToken(ADDRESS, SIZE, NEXT)
    assert ocean.address.listToken(address=ADDRESS, size=SIZE, next=NEXT)


@pytest.mark.query
def test_listVault():  # 06
    assert ocean.address.listVault(ADDRESS)
    assert ocean.address.listVault(ADDRESS, SIZE, NEXT)
    assert ocean.address.listVault(address=ADDRESS, size=SIZE, next=NEXT)


@pytest.mark.query
def test_listTransaction():  # 07
    assert ocean.address.listTransaction(ADDRESS)
    assert ocean.address.listTransaction(ADDRESS, SIZE, NEXT)
    assert ocean.address.listTransaction(address=ADDRESS, size=SIZE, next=NEXT)


@pytest.mark.query
def test_listTransactionUnspent():  # 08
    assert ocean.address.listTransactionUnspent(ADDRESS)
    assert ocean.address.listTransactionUnspent(ADDRESS, SIZE, NEXT)
    assert ocean.address.listTransactionUnspent(address=ADDRESS, size=SIZE, next=NEXT)
