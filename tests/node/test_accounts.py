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


@pytest.mark.transactions
def test_accounttoutxos():  # 03
    assert len(node.accounts.accounttoutxos(address, {address: "0.00001000"})) == LENGTH_OF_TXID
    assert len(node.accounts.accounttoutxos(address, {address: "0.00001000"}, [])) == LENGTH_OF_TXID
    assert len(node.accounts.accounttoutxos(_from=address, to={address: "0.00001000"}, inputs=[])) == LENGTH_OF_TXID


@pytest.mark.query
def test_executesmartcontract():  # 04
    string = ".* RPC_INVALID_PARAMETER: Specified smart contract not found"
    with pytest.raises(InternalServerError, match=string):
        assert node.accounts.executesmartcontract("test", "0.00000001@DFI")
    with pytest.raises(InternalServerError, match=string):
        assert node.accounts.executesmartcontract("test", "0.00000001@DFI", address, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.accounts.executesmartcontract(name="test", amount="0.00000001@DFI", address=address, inputs=[])


@pytest.mark.transactions
def test_futureswap():  # 05
    assert len(node.accounts.futureswap(address, "0.00000001@DUSD", "SPY")) == LENGTH_OF_TXID
    assert len(node.accounts.futureswap(address, "0.00000001@DUSD", "SPY", [])) == LENGTH_OF_TXID
    assert len(node.accounts.futureswap(address=address, amount="0.00000001@DUSD", destination="SPY", inputs=[])) == LENGTH_OF_TXID


@pytest.mark.query
def test_getaccount():  # 06
    assert node.accounts.getaccount(address)
    assert node.accounts.getaccount(address, 0, True, 100, False)
    assert node.accounts.getaccount(address, start=0, including_start=True, limit=100, indexed_amounts=False)


@pytest.mark.query
def test_getaccounthistory():  # 07
    assert node.accounts.getaccounthistory(address, 1882244, 2) == {}
    assert node.accounts.getaccounthistory(owner=address, blockheight=1882244, txn=2) == {}


@pytest.mark.query
def test_getburninfo():  # 08
    assert node.accounts.getburninfo()


@pytest.mark.query
def test_getpendingfutureswaps():  # 09
    assert node.accounts.getpendingfutureswaps(address)
    assert node.accounts.getpendingfutureswaps(address=address)


@pytest.mark.query
def test_gettokenbalances():  # 10
    assert node.accounts.gettokenbalances()
    assert node.accounts.gettokenbalances(0, True, 100, False, False)
    assert node.accounts.gettokenbalances(start=0, including_start=True, limit=100, indexed_amounts=False,
                                          symbol_lookup=False)


@pytest.mark.query
def test_listaccounthistory():  # 11
    blockcount = node.blockchain.getblockcount()
    assert node.accounts.listaccounthistory(address)
    assert node.accounts.listaccounthistory(address, blockcount, 10000000, True, "", "", 100)
    assert node.accounts.listaccounthistory(owner=address, maxBlockHeight=blockcount, depth=10000000, no_rewards=True,
                                            token="", txtype="", limit=100)
