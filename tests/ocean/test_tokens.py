import pytest
from . import ocean

SIZE = 30
NEXT = None


@pytest.mark.query
def test_list():  # 01
    assert ocean.tokens.list()
    assert ocean.tokens.list(SIZE, NEXT)
    assert ocean.tokens.list(size=SIZE, next=NEXT)


@pytest.mark.query
def test_get():  # 02
    id = 0  # DFI
    assert ocean.tokens.get(id)
    assert ocean.tokens.get(id=id)
