import pytest
from tests.node.util import createNode

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError
from defichain.exceptions.BadRequest import BadRequest

node = createNode()


@pytest.mark.query
def test_getblocktemplate():  # 01
    string = ".* RPC_INVALID_REQUEST: getblocktemplate can only be called by masternodes"
    with pytest.raises(BadRequest, match=string):
        assert node.mining.getblocktemplate()
        assert node.mining.getblocktemplate({})
        assert node.mining.getblocktemplate(template_request={})


@pytest.mark.query
def test_getmininginfo():  # 02
    assert node.mining.getmininginfo()


@pytest.mark.query
def test_getmintinginfo():  # 03
    assert node.mining.getmintinginfo()


@pytest.mark.query
def test_getnetworkhashps():  # 04
    assert node.mining.getnetworkhashps()
    assert node.mining.getnetworkhashps(120, -1)
    assert node.mining.getnetworkhashps(nblocks=120, height=-1)


@pytest.mark.query
def test_prioritisetransaction():  # 05
    txid = "16960f9001a021d745757714baf25fe7f8a4637d92efe708ecac77cc0da7e404"
    assert node.mining.prioritisetransaction(txid, 10000)
    assert node.mining.prioritisetransaction(txid, 10000, 0)
    assert node.mining.prioritisetransaction(txid=txid, fee_delta=10000, dummy=0)


@pytest.mark.query
def test_submitblock():  # 06
    hex="048230"
    string = ".* RPC_DESERIALIZATION_ERROR: Block decode failed"
    with pytest.raises(InternalServerError, match=string):
        assert node.mining.submitblock(hex)
        assert node.mining.submitblock(hex, "ignored")
        assert node.mining.submitblock(hexdata=hex, dummy="ignored")


@pytest.mark.query
def test_submitheader():  # 06
    hex = "048230"
    string = ".* RPC_DESERIALIZATION_ERROR: Block header decode failed"
    with pytest.raises(InternalServerError, match=string):
        assert node.mining.submitheader(hex)
        assert node.mining.submitheader(hexdata=hex)
