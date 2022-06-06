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


@pytest.mark.query
def test_getreceivedbylabel():  # 17
    assert node.wallet.getreceivedbylabel("")
    assert node.wallet.getreceivedbylabel("", 1)
    assert node.wallet.getreceivedbylabel(label="", minconf=1)


@pytest.mark.query
def test_gettransaction():  # 18
    txid = node.wallet.listtransactions(count=1)[0]["txid"]

    assert node.wallet.gettransaction(txid)
    assert node.wallet.gettransaction(txid, True)
    assert node.wallet.gettransaction(txid=txid, include_watchonly=True)


@pytest.mark.query
def test_getunconfirmedbalance():  # 19
    result1 = node.wallet.getunconfirmedbalance()
    assert result1 or result1 == 0.0
    result2 = node.wallet.getunconfirmedbalance(False)
    assert result2 or result2 == 0.0
    result3 = node.wallet.getunconfirmedbalance(with_tokens=False)
    assert result2 or result3 == 0.0


@pytest.mark.query
def test_getwalletinfo():  # 20
    assert node.wallet.getwalletinfo()
    assert node.wallet.getwalletinfo(False)
    assert node.wallet.getwalletinfo(with_tokens=False)


@pytest.mark.query
def test_importaddress():  # 21
    assert node.wallet.importaddress(address, rescan=False) is None
    assert node.wallet.importaddress(address, "", False, False) is None
    assert node.wallet.importaddress(address=address, label="", rescan=False, p2sh=False) is None


@pytest.mark.query
def test_importmulti():  # 22
    string = '.* RPC_TYPE_ERROR: Expected type object, got bool'
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.importmulti([])
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.importmulti([], False)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.importmulti(requests=[], rescan=False)


@pytest.mark.query
def test_importprivkey():  # 23
    priv_key = "KxmHsh3zrURFKPsqR5fUAyE6viuqe4dRc6KUzKyGtPyjhWXzmPVN"

    assert node.wallet.importprivkey(priv_key, rescan=False) is None
    assert node.wallet.importprivkey(priv_key, "", False) is None
    assert node.wallet.importprivkey(privkey=priv_key, label="", rescan=False) is None


@pytest.mark.query
def test_importprunedfunds():  # 24
    pass


@pytest.mark.query
def test_importpubkey():  # 25
    pub_key = "028bfcd13b59fe60442ae6dd2861b327ba47c5def1d289b5e5b73c8db0ad65a327"

    assert node.wallet.importpubkey(pub_key, rescan=False) is None
    assert node.wallet.importpubkey(pub_key, "", False) is None
    assert node.wallet.importpubkey(pubkey=pub_key, label="", rescan=False) is None


@pytest.mark.query
def test_importwallet():  # 26
    wallet_path = load_secrets_conf()["wallet_path"]

    assert node.wallet.importwallet(wallet_path) is None
    assert node.wallet.importwallet(filename=wallet_path) is None


@pytest.mark.query
def test_keypoolrefill():  # 27
    assert node.wallet.keypoolrefill() is None
    assert node.wallet.keypoolrefill(100) is None
    assert node.wallet.keypoolrefill(newsize=100) is None


@pytest.mark.query
def test_listaddressgroupings():  # 28
    assert node.wallet.listaddressgroupings()


@pytest.mark.query
def test_listlables():  # 29
    assert node.wallet.listlabels()
    assert node.wallet.listlabels("")
    assert node.wallet.listlabels(purpose="")


@pytest.mark.query
def test_listlockunspent():  # 30
    result = node.wallet.listlockunspent()
    assert result or result == []


