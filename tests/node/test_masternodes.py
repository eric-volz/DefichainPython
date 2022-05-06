import pytest
from tests.node.util import createNode, load_secrets_conf

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

node = createNode()
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_createmasternode():  # 01
    string = ".* RPC_WALLET_ERROR: Add-on auth TX failed: Insufficient funds"
    with pytest.raises(InternalServerError, match=string):
        assert node.masternodes.createmasternode(address)
        assert node.masternodes.createmasternode(address, address, [], "TENYEARTIMELOCK")
        assert node.masternodes.createmasternode(ownerAddress=address, operatorAddress=address, inputs=[],
                                                 timelock="TENYEARTIMELOCK")


@pytest.mark.query
def test_getactivemasternodecount():  # 02
    assert node.masternodes.getactivemasternodecount()
    assert node.masternodes.getactivemasternodecount(100)
    assert node.masternodes.getactivemasternodecount(blockCount=100)


@pytest.mark.query
def test_getanchorteams():  # 03
    assert node.masternodes.getanchorteams()
    assert node.masternodes.getanchorteams(10)
    assert node.masternodes.getanchorteams(blockHeight=10)


@pytest.mark.query
def test_getmasternode():  # 04
    mn_id = "e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100"
    assert node.masternodes.getmasternode(mn_id)
    assert node.masternodes.getmasternode(mn_id=mn_id)

