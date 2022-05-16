import pytest
from tests.util import createNode

node = createNode()


@pytest.mark.query
def test_getzmqnotifications():  # 01
    zmq = node.zmq.getzmqnotifications()
    assert zmq or zmq == []
