import pytest

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

from . import node


@pytest.mark.query
def test_addnode():  # 01
    url = "127.0.0.1:8554"
    command = "onetry"
    assert node.network.addnode(url, command) is None
    assert node.network.addnode(node=url, command=command) is None


@pytest.mark.query
def test_clearbanned():  # 02
    banned = node.network.clearbanned()
    assert banned or banned is None


@pytest.mark.query
def test_disconnectnode():  # 03
    url = "127.0.0.1:8554"
    nodeId = "1"
    string = ".* RPC_CLIENT_NODE_NOT_CONNECTED: Node not found in connected nodes"
    with pytest.raises(InternalServerError, match=string):
        assert node.network.disconnectnode()
        assert node.network.disconnectnode(url)
        assert node.network.disconnectnode("", nodeId)
        assert node.network.disconnectnode(url, nodeId)
        assert node.network.disconnectnode(address=url, nodeid=nodeId)


@pytest.mark.query
def test_getaddednodeinfo():  # 04
    url = "127.0.0.1:8554"
    result1 = node.network.getaddednodeinfo()
    assert result1 or result1 == []
    string = ".* RPC_CLIENT_NODE_NOT_ADDED: Error: Node has not been added."
    with pytest.raises(InternalServerError, match=string):
        result2 = node.network.getaddednodeinfo(url)
        assert result2 or result2 == []
        result3 = node.network.getaddednodeinfo(node=url)
        assert result3 or result3 == []


@pytest.mark.query
def test_getconnectioncount():  # 05
    assert node.network.getconnectioncount()


@pytest.mark.query
def test_getnettotals():  # 06
    assert node.network.getnettotals()


@pytest.mark.query
def test_getnetworkinfo():  # 07
    assert node.network.getnetworkinfo()


@pytest.mark.query
def test_getnodeaddresses():  # 08
    assert node.network.getnodeaddresses()


@pytest.mark.query
def test_getpeerinfo():  # 09
    assert node.network.getpeerinfo()


@pytest.mark.query
def test_getversioninfo():  # 10
    assert node.network.getversioninfo()


@pytest.mark.query
def test_listbanned():  # 11
    banned = node.network.listbanned()
    assert banned or banned == []


@pytest.mark.query
def test_ping():  # 12
    assert node.network.ping() is None


@pytest.mark.query
def test_setban():  # 13
    subnet = "127.0.0.1"
    command = "add"
    bantime = 0
    absolute = False
    assert node.network.setban(subnet, command) is None
    node.network.clearbanned()
    assert node.network.setban(subnet, command, bantime, absolute) is None
    node.network.clearbanned()
    assert node.network.setban(subnet=subnet, command=command, bantime=bantime, absolute=absolute) is None
    node.network.clearbanned()


@pytest.mark.query
def test_setnetworkactive():  # 14
    assert node.network.setnetworkactive(True)

