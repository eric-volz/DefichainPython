import pytest
from tests.node.util import createNode, load_secrets_conf, LENGTH_OF_TXID

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

node = createNode()
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_accounthistorycount():  # 01
    assert node.accounts.accounthistorycount(address)
    assert node.accounts.accounthistorycount(address, True, "DFI", "")
    assert node.accounts.accounthistorycount(owner=address, no_rewards=True, token="DFI", txtype="")


@pytest.mark.transactions
def test_accounttoaccount():  # 02
    assert len(node.accounts.accounttoaccount(address, {address: "0.0001@DUSD"})) == LENGTH_OF_TXID
    assert len(node.accounts.accounttoaccount(address, {address: "0.0001@DUSD"}, [])) == LENGTH_OF_TXID
    assert len(node.accounts.accounttoaccount(_from=address, to={address: "0.0001@DUSD"}, inputs=[])) == LENGTH_OF_TXID
