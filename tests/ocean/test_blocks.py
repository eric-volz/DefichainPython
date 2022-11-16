import pytest
from . import ocean

SIZE = 30
NEXT = None


@pytest.mark.query
def test_list():  # 01
    assert ocean.blocks.list()
    assert ocean.blocks.list(SIZE, NEXT)
    assert ocean.blocks.list(size=SIZE, next=NEXT)


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
    assert ocean.blocks.getTransactions(blockhash, SIZE, NEXT)
    assert ocean.blocks.getTransactions(hash=blockhash, size=SIZE, next=NEXT)

