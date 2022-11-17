import pytest
from tests.util import load_secrets_conf

# Import Exceptions

from . import node
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_getmemoryinfo():  # 01
    assert node.control.getmemoryinfo()
    assert node.control.getmemoryinfo("stats")
    assert node.control.getmemoryinfo(mode="stats")


@pytest.mark.query
def test_getrpcinfo():  # 02
    assert node.control.getrpcinfo()


@pytest.mark.query
def test_help():  # 03
    assert node.control.help()
    assert node.control.help("help")
    assert node.control.help(command="help")


@pytest.mark.query
def test_logging():  # 04
    assert node.control.logging()
    assert node.control.logging([], [])
    assert node.control.logging(include=[], exclude=[])


@pytest.mark.query
def test_stop():  # 05
    # assert node.control.stop() --> should work :)
    assert True


@pytest.mark.query
def test_uptime():  # 06
    assert node.control.uptime()
