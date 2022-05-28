import pytest
from tests.util import createNode

node = createNode()


@pytest.mark.query
def test_getrpcstats():  # 01
    node.blockchain.getblockcount()
    assert node.stats.getrpcstats("getblockcount")
    assert node.stats.getrpcstats(command="getblockcount")


@pytest.mark.query
def test_listrpcstats():  # 02
    assert node.stats.listrpcstats()
