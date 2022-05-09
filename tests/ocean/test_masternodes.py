import pytest
from defichain import Ocean

ocean = Ocean()
SIZE = 30
NEXT = None


@pytest.mark.query
def test_list():  # 01
    assert ocean.masternodes.list()
    assert ocean.masternodes.list(SIZE, NEXT)
    assert ocean.masternodes.list(size=SIZE, next=NEXT)


@pytest.mark.query
def test_get():  # 02
    id = "6be52cb3ce612b6949b7652e35aa42e3ad7174d284c9d5685ee42a9f230a1fe6"
    assert ocean.masternodes.get(id)
    assert ocean.masternodes.get(id=id)
