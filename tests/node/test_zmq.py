import pytest

from . import node


@pytest.mark.query
def test_getzmqnotifications():  # 01
    zmq = node.zmq.getzmqnotifications()
    assert zmq or zmq == []
