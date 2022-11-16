import pytest
from . import ocean

@pytest.mark.query
def test_call():  # 01
    assert ocean.rpc.call("getblockcount")
    assert ocean.rpc.call("getblockhash", 100)
