import pytest
import os
from tests.util import createNode, load_secrets_conf
from pathlib import Path
path = str(Path.home())

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

node = createNode()
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_abandontransaction():  # 01
    txid = "8bb2a97832d5614523b75b082975c15ad17422df659898c5a5112757d438fb39"
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Invalid or non-wallet transaction id"
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.abandontransaction(txid)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.abandontransaction(txid=txid)


@pytest.mark.query
def test_abortrescan():  # 02
    assert node.wallet.abortrescan() or not node.wallet.abortrescan()


@pytest.mark.query
def test_addmultisigaddress():  # 03
    address1 = node.wallet.getnewaddress()
    address2 = node.wallet.getnewaddress()
    address3 = node.wallet.getnewaddress()
    assert node.wallet.addmultisigaddress(3, [address1, address2, address3])
    assert node.wallet.addmultisigaddress(3, [address1, address2, address3], "test", "legacy")
    assert node.wallet.addmultisigaddress(nrequired=3, keys=[address1, address2, address3], label="test",
                                          address_type="legacy")

@pytest.mark.query
def test_backupwallet():  # 04
    assert node.wallet.backupwallet(path + os.sep + "backup_wallet") is None
    os.remove(path + os.sep + "backup_wallet")
    assert node.wallet.backupwallet(destination=path + os.sep + "backup_wallet") is None
    os.remove(path + os.sep + "backup_wallet")


@pytest.mark.query
def test_bumpfee():  # 05
    txid = "8bb2a97832d5614523b75b082975c15ad17422df659898c5a5112757d438fb39"
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Invalid or non-wallet transaction id"
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.bumpfee(txid)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.bumpfee(txid, 1, None, True, "UNSET")
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.bumpfee(txid=txid, confTarget=1, totalFee=None, replaceable=True, estimate_mode="UNSET")


@pytest.mark.query
def test_createwallet():  # 06
    wallet_name = load_secrets_conf()["wallet_path"].split(os.sep)[-1]
    string = f".* RPC_WALLET_ERROR: Wallet {wallet_name} already exists."
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.createwallet(wallet_name)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.createwallet(wallet_name, False, False, "", False)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.createwallet(wallet_name=wallet_name, disable_private_keys=False, blank=False,
                                        passphrase="", avoid_reuse=False)

@pytest.mark.query
def test_dumpprivkey():  # 07
    assert node.wallet.dumpprivkey(address)
    assert node.wallet.dumpprivkey(address=address)


@pytest.mark.query
def test_dumpwallet():  # 08
    assert node.wallet.dumpwallet(path + os.sep + "dump_wallet")
    os.remove(path + os.sep + "dump_wallet")
    assert node.wallet.dumpwallet(filename=path + os.sep + "dump_wallet")
    os.remove(path + os.sep + "dump_wallet")


@pytest.mark.query
def test_encryptwallet():  # 09
    """
    assumes that a password has been set!
    Otherwise, the test fails and test is new password of the wallet
    """
    string = ".* RPC_WALLET_WRONG_ENC_STATE: Error: running with an encrypted wallet, but encryptwallet was called."
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.encryptwallet("test")
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.encryptwallet(passphrase="test")


@pytest.mark.query
def test_getaddressesbylabel():  # 10
    assert node.wallet.getaddressesbylabel("")
    assert node.wallet.getaddressesbylabel(label="")


@pytest.mark.query
def test_getaddressinfo():  # 11
    assert node.wallet.getaddressinfo(address)
    assert node.wallet.getaddressinfo(address=address)


@pytest.mark.query
def test_getbalance():  # 12
    string = '.* RPC_WALLET_ERROR: wallet does not have the "avoid reuse" feature enabled'
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.getbalance()
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.getbalance("*", 0, True, True, False)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.getbalance(dummy="*", minconf=0, include_watchonly=True, avoid_reuse=True, with_tokens=False)


@pytest.mark.query
def test_getbalances():  # 13
    assert node.wallet.getbalances()
    assert node.wallet.getbalances(with_tokens=False)


@pytest.mark.query
def test_getnewaddress():  # 14
    assert node.wallet.getnewaddress()
    assert node.wallet.getnewaddress("", "legacy")
    assert node.wallet.getnewaddress(label="", address_type="legacy")


@pytest.mark.query
def test_getrawchangeaddress():  # 15
    assert node.wallet.getrawchangeaddress()
    assert node.wallet.getrawchangeaddress("legacy")
    assert node.wallet.getrawchangeaddress(address_type="legacy")


@pytest.mark.query
def test_getreceivedbyaddress():  # 16
    assert node.wallet.getreceivedbyaddress(address)
    assert node.wallet.getreceivedbyaddress(address, 1)
    assert node.wallet.getreceivedbyaddress(address=address, minconf=1)
