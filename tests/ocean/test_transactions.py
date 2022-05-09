import pytest
from defichain import Ocean

ocean = Ocean()
TXID = "bfb4bab92292e9c9b260c30e110bbbea0d8e0c78015a9058f67f1770d84f478f"
SIZE = 30
NEXT = None


@pytest.mark.query
def test_get():  # 01
    assert ocean.transactions.get(TXID)
    assert ocean.transactions.get(id=TXID)


@pytest.mark.query
def test_getVins():  # 02
    assert ocean.transactions.getVins(TXID)
    assert ocean.transactions.getVins(TXID, SIZE, NEXT)
    assert ocean.transactions.getVins(txid=TXID, size=SIZE, next=NEXT)


@pytest.mark.query
def test_getVouts():  # 03
    assert ocean.transactions.getVouts(TXID)
    assert ocean.transactions.getVouts(TXID, SIZE, NEXT)
    assert ocean.transactions.getVouts(txid=TXID, size=SIZE, next=NEXT)
