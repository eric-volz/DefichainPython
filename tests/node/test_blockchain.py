import pytest
from util import createNode

node = createNode()


@pytest.mark.query
def test_clearmempool():  # 01
    assert node.blockchain.clearmempool()


@pytest.mark.query
def test_getbestblockhash():  # 02
    assert node.blockchain.getbestblockhash()


@pytest.mark.query
def test_getblock():  # 03
    assert node.blockchain.getblock("934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d")["hash"] == \
           '934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d'


@pytest.mark.query
def test_getblockchaininfo():  # 04
    assert node.blockchain.getblockchaininfo()


@pytest.mark.query
def test_getblockcount():  # 05
    assert node.blockchain.getblockcount()
