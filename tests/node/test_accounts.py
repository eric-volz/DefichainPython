import pytest
import time
from tests.util import createNode, load_secrets_conf, LENGTH_OF_TXID

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError
from defichain.exceptions.http.BadRequest import BadRequest

node = createNode()
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_accounthistorycount():  # 01
    assert node.accounts.accounthistorycount(address)
    assert node.accounts.accounthistorycount(address, True, "DFI", "")
    assert node.accounts.accounthistorycount(owner=address, no_rewards=True, token="DFI", txtype="")


@pytest.mark.transactions
def test_accounttoaccount():  # 02
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert len(node.accounts.accounttoaccount(address, {address: "0.0001@DUSD"})) == LENGTH_OF_TXID
    assert len(node.accounts.accounttoaccount(address, {address: "0.0001@DUSD"}, [])) == LENGTH_OF_TXID
    assert len(node.accounts.accounttoaccount(_from=address, to={address: "0.0001@DUSD"}, inputs=[])) == LENGTH_OF_TXID


@pytest.mark.transactions
def test_accounttoutxos():  # 03
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

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
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

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
def test_getpendingdusdswaps():  # 09
    result1 = node.accounts.getpendingdusdswaps(address)
    assert result1 or result1 == {}
    result2 = node.accounts.getpendingdusdswaps(address=address)
    assert result2 or result2 == {}


@pytest.mark.query
def test_getpendingfutureswaps():  # 10
    assert node.accounts.getpendingfutureswaps(address)
    assert node.accounts.getpendingfutureswaps(address=address)


@pytest.mark.query
def test_gettokenbalances():  # 11
    assert node.accounts.gettokenbalances()
    assert node.accounts.gettokenbalances(0, True, 100, False, False)
    assert node.accounts.gettokenbalances(start=0, including_start=True, limit=100, indexed_amounts=False,
                                          symbol_lookup=False)


@pytest.mark.query
def test_listaccounthistory():  # 12
    blockcount = node.blockchain.getblockcount()
    assert node.accounts.listaccounthistory(address)
    assert node.accounts.listaccounthistory(address, blockcount, 10000000, True, "", "", 100, 0)
    assert node.accounts.listaccounthistory(owner=address, maxBlockHeight=blockcount, depth=10000000, no_rewards=True,
                                            token="", txtype="", limit=100, txn=0)


@pytest.mark.query
def test_listaccounts():  # 13
    assert node.accounts.listaccounts()
    assert node.accounts.listaccounts('001400007a7328b9554650a56d980095071a201341a2@3', True, 100, True, False, False)
    assert node.accounts.listaccounts(start='001400007a7328b9554650a56d980095071a201341a2@3', including_start=True,
                                      limit=100, verbose=True, indexed_amounts=False, is_mine_only=False)


@pytest.mark.query
def test_listburnhistory():  # 14
    assert node.accounts.listburnhistory()
    assert node.accounts.listburnhistory(node.blockchain.getblockcount(), 10000, "DFI", "", 100)
    assert node.accounts.listburnhistory(maxBlockHeight=node.blockchain.getblockcount(), depth=10000, token="DFI",
                                         txtype="", limit=100)


@pytest.mark.query
def test_listcommunitybalances():  # 15
    assert node.accounts.listcommunitybalances()


@pytest.mark.query
def test_listpendingfutureswaps():  # 16
    result = node.accounts.listpendingdusdswaps()
    assert result or result == []


@pytest.mark.query
def test_listpendingfutureswaps():  # 17
    result = node.accounts.listpendingfutureswaps()
    assert result or result == []


@pytest.mark.transactions
def test_sendtokenstoaddress():  # 18
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert len(node.accounts.sendtokenstoaddress({address: "0.0001@DUSD"}, {address: "0.0001@DUSD"})) == LENGTH_OF_TXID
    assert len(node.accounts.sendtokenstoaddress({address: "0.0001@DUSD"}, {address: "0.0001@DUSD"}, "pie")) == LENGTH_OF_TXID
    assert len(node.accounts.sendtokenstoaddress(_from={address: "0.0001@DUSD"}, to={address: "0.0001@DUSD"},
                                                 selectionMode="pie")) == LENGTH_OF_TXID


@pytest.mark.transactions
def test_sendutxosfrom():  # 19
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert len(node.accounts.sendutxosfrom(address, address, 0.001)) == LENGTH_OF_TXID
    assert len(node.accounts.sendutxosfrom(address, address, 0.001, address)) == LENGTH_OF_TXID
    assert len(node.accounts.sendutxosfrom(_from=address, to=address, amount=0.001, change=address)) == LENGTH_OF_TXID


@pytest.mark.transactions
def test_utxostoaccount():  # 20
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert len(node.accounts.utxostoaccount({address: "0.000001@DFI"})) == LENGTH_OF_TXID
    assert len(node.accounts.utxostoaccount({address: "0.000001@DFI"}, [])) == LENGTH_OF_TXID
    assert len(node.accounts.utxostoaccount(amounts={address: "0.000001@DFI"}, inputs=[])) == LENGTH_OF_TXID


@pytest.mark.transactions
def test_withdrawfutureswap():  # 21
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    string = ".* RPC_INVALID_REQUEST: Test DFIP2203Tx execution failed:\namount 0.00000000 is less than 1.00000000"
    with pytest.raises(BadRequest, match=string):
        assert node.accounts.withdrawfutureswap(address, "1@DUSD", "TSLA")
    with pytest.raises(BadRequest, match=string):
        assert node.accounts.withdrawfutureswap(address, "1@DUSD", "TSLA", [])
    with pytest.raises(BadRequest, match=string):
        assert node.accounts.withdrawfutureswap(address=address, amount="1@DUSD", destination="TSLA", inputs=[])
