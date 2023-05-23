import pytest
from tests.util import load_secrets_conf

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

from . import node
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_createmasternode():  # 01
    string = ".* RPC_WALLET_ERROR: Insufficient funds"
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


@pytest.mark.query
def test_getmasternodeblocks():  # 05
    mn_id = "f02de244dfc9e64412a8ff5ca518e806dd65bd896ab62e85e77996981cb36c04"
    ownerAddress = "8UNfA7MdNLTRsbzBP6Qm9N7HWoLHeNLB8n"
    operatorAddress = "8TGDAfyR21MQNVVqvaiL6bq9Xt4TxeTuSy"
    depth = 1000000
    assert node.masternodes.getmasternodeblocks(mn_id)
    assert node.masternodes.getmasternodeblocks(id=mn_id)
    assert node.masternodes.getmasternodeblocks(ownerAddress=ownerAddress)
    assert node.masternodes.getmasternodeblocks(operatorAddress=operatorAddress)
    assert node.masternodes.getmasternodeblocks(id=mn_id, depth=depth)
    assert node.masternodes.getmasternodeblocks(ownerAddress=ownerAddress, depth=depth)
    assert node.masternodes.getmasternodeblocks(operatorAddress=operatorAddress, depth=depth)


@pytest.mark.query
def test_listanchors():  # 06
    assert node.masternodes.listanchors()


@pytest.mark.query
def test_listmasternodes():  # 07
    mn_id = "e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100"
    assert node.masternodes.listmasternodes()
    assert node.masternodes.listmasternodes(mn_id, True, 10, False)
    assert node.masternodes.listmasternodes(start=mn_id, including_start=True, limit=10, verbose=False)


@pytest.mark.query
def test_resignmasternode():  # 08
    mn_id = "e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100"
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Incorrect authorization for "
    with pytest.raises(InternalServerError, match=string):
        assert node.masternodes.resignmasternode(mn_id)


@pytest.mark.query
def test_updatemasternode():  # 09
    mn_id = "e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100"
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Incorrect authorization for 8XctLWjNsRJByMrYCgNxqyw9F1JhGYoDNb"
    with pytest.raises(InternalServerError, match=string):
        assert node.masternodes.updatemasternode(mn_id, {"ownerAddress": "8N9gJZFTYrempWvr13f5SR9X3PNJBCwU5U"})
        assert node.masternodes.updatemasternode(mn_id, {"operatorAddress": "8N9gJZFTYrempWvr13f5SR9X3PNJBCwU5U"})
        assert node.masternodes.updatemasternode(mn_id, {"rewardAddress": "8N9gJZFTYrempWvr13f5SR9X3PNJBCwU5U"})
        assert node.masternodes.updatemasternode(mn_id, {"ownerAddress": "8N9gJZFTYrempWvr13f5SR9X3PNJBCwU5U"}, [])
        assert node.masternodes.updatemasternode(mn_id=mn_id,
                                                 values={"ownerAddress": "8N9gJZFTYrempWvr13f5SR9X3PNJBCwU5U"},
                                                 inputs=[])

