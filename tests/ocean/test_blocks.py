import pytest
from defichain import Ocean

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

ocean = Ocean()


@pytest.mark.query
def test_list():  # 01
    assert ocean.blocks.list()
    assert ocean.blocks.list(30, None)
    assert ocean.blocks.list(size=30, next=None)


@pytest.mark.query
def test_get():  # 02
    blockheight = 100
    blockhash = "b6e0ee6da7e61f6b672b72b9a8a68413cdf0344102acecccf9cf2a6d338630c6"
    assert ocean.blocks.get(blockheight)
    assert ocean.blocks.get(blockhash)
    assert ocean.blocks.get(id=blockheight)
    assert ocean.blocks.get(id=blockhash)


@pytest.mark.query
def test_getTransactions():  # 03
    blockhash = "b6e0ee6da7e61f6b672b72b9a8a68413cdf0344102acecccf9cf2a6d338630c6"
    assert ocean.blocks.getTransactions(blockhash)
    assert ocean.blocks.getTransactions(blockhash, 30, None)
    assert ocean.blocks.getTransactions(hash=blockhash, size=30, next=None)

