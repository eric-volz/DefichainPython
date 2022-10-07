import pytest
import os, time
from tests.util import createNode, load_secrets_conf

from pathlib import Path
path = str(Path.home())

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

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


@pytest.mark.query
def test_listreceivedbyaddress():  # 31
    assert node.wallet.listreceivedbyaddress()
    assert node.wallet.listreceivedbyaddress(1, False, True, address)
    assert node.wallet.listreceivedbyaddress(minconf=1, include_empty=False, include_watchonly=True,
                                             address_filter=address)


@pytest.mark.query
def test_listreceivedbylabel():  # 32
    assert node.wallet.listreceivedbylabel()
    assert node.wallet.listreceivedbylabel(1, False, True)
    assert node.wallet.listreceivedbylabel(minconf=1, include_empty=False, include_watchonly=True)


@pytest.mark.query
def test_listsinceblock():  # 33
    assert node.wallet.listsinceblock()
    assert node.wallet.listsinceblock("279b1a87aedc7b9471d4ad4e5f12967ab6259926cd097ade188dfcf22ebfe72a", 1, True, True)
    assert node.wallet.listsinceblock(blockhash="279b1a87aedc7b9471d4ad4e5f12967ab6259926cd097ade188dfcf22ebfe72a",
                                      target_confirmations=1, include_watchonly=True, include_removed=True)


@pytest.mark.query
def test_listtransactions():  # 34
    assert node.wallet.listtransactions()
    assert node.wallet.listtransactions("*", 10, 0, True, False)
    assert node.wallet.listtransactions(label="*", count=10, skip=0, include_watchonly=True, exclude_custom_tx=False)


@pytest.mark.query
def test_listunspent():  # 35
    result1 = node.wallet.listunspent()
    assert result1 or result1 == []
    result2 = node.wallet.listunspent(1, 9999999, [], True, 0, 9999999, 10, 9999999, "DFI")
    assert result2 or result2 == []
    result3 = node.wallet.listunspent(mincof=1, maxcof=9999999, addresses=[], include_unsafe=True, minimumAmount=0,
                                      maximumAmount=9999999, maximumCount=10, minimumSumAmount=9999999, tokenId="DFI")
    assert result3 or result3 == []


@pytest.mark.query
def test_listwalletdir():  # 36
    assert node.wallet.listwalletdir()


@pytest.mark.query
def test_listwallets():  # 37
    assert node.wallet.listwallets()


@pytest.mark.query
def test_loadwallet():  # 38
    wallet_path = load_secrets_conf()["wallet_path"]
    string = ".* RPC_WALLET_ERROR: Wallet file verification failed: Error loading wallet .*"
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.loadwallet(wallet_path)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.loadwallet(filename=wallet_path)


@pytest.mark.query
def test_lockunspent():  # 39
    assert node.wallet.lockunspent(True)
    assert node.wallet.lockunspent(True, [])
    assert node.wallet.lockunspent(unlock=True, transactions=[])


@pytest.mark.query
def test_removeprunedfunds():  # 40
    txid = "e56d3960e850ffe5dffd4733ced07d644527eb81e86440952195ce9556b665ea"

    string = ".* RPC_INVALID_PARAMETER: Transaction does not exist in wallet."
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.removeprunedfunds(txid)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.removeprunedfunds(txid=txid)


@pytest.mark.query
def test_rescanblockchain():  # 41
    assert node.wallet.rescanblockchain(node.blockchain.getblockcount()-100, node.blockchain.getblockcount())
    assert node.wallet.rescanblockchain(start_height=node.blockchain.getblockcount() - 100,
                                        stop_height=node.blockchain.getblockcount())


@pytest.mark.transactions
def test_sendmany():  # 42
    assert node.wallet.sendmany("", {address: 0.00001})
    assert node.wallet.sendmany("", {address: 0.00001}, 0, "Test", [], True, 1, "UNSET")
    assert node.wallet.sendmany(dummy="", amounts={address: 0.00001}, minconf=0, comment="Test", subtractfeefrom=[],
                                replaceable=True, conf_target=1, estimate_mode="UNSET")


@pytest.mark.transactions
def test_sendtoaddress():  # 43
    assert node.wallet.sendtoaddress(address, 0.0001)
    assert node.wallet.sendtoaddress(address, 0.0001, "Test", "Myself", False, True, 1, "UNSET", False)
    assert node.wallet.sendtoaddress(address=address, amount=0.0001, comment="Test", comment_to="Myself",
                                     subtractfeefromamount=False, replaceable=True, conf_target=1,
                                     estimate_mode="UNSET", avoid_reuse=False)


@pytest.mark.query
def test_sethdseed():  # 44
    assert node.wallet.sethdseed() is None
    assert node.wallet.sethdseed(False, None) is None
    assert node.wallet.sethdseed(newkeypool=False, seed=None) is None


@pytest.mark.query
def test_setlabel():  # 45
    assert node.wallet.setlabel(address, "") is None
    assert node.wallet.setlabel(address=address, label="") is None


@pytest.mark.query
def test_settxfee():  # 46
    assert node.wallet.settxfee(0.00001)
    assert node.wallet.settxfee(amount=0.00001)


@pytest.mark.query
def test_setwalletflag():  # 47
    string = ".* RPC_INVALID_PARAMETER: Wallet flag is already set to false: avoid_reuse"
    assert node.wallet.setwalletflag("avoid_reuse")
    assert node.wallet.setwalletflag("avoid_reuse", False)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.setwalletflag(flag="avoid_reuse", value=False)


@pytest.mark.query
def test_signmessage():  # 48
    assert node.wallet.signmessage(address, "test")
    assert node.wallet.signmessage(address=address, message="test")


@pytest.mark.query
def test_signrawtransactionwithwallet():  # 49
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)

    assert node.wallet.signrawtransactionwithwallet(raw_tx)
    assert node.wallet.signrawtransactionwithwallet(raw_tx, [], "ALL")
    assert node.wallet.signrawtransactionwithwallet(hexstring=raw_tx, prevtxs=[], sighashtype="ALL")


@pytest.mark.query
def test_unloadwallet():  # 50
    assert node.wallet.unloadwallet() is None
    node.wallet.loadwallet(load_secrets_conf()["wallet_path"])


@pytest.mark.query
def test_walletcreatefundedpsbt():  # 51
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]
    assert node.wallet.walletcreatefundedpsbt([{"txid": txid, "vout": vout}],
                                              [{address: 0.00001}])
    assert node.wallet.walletcreatefundedpsbt([{"txid": txid, "vout": vout}],
                                              [{address: 0.00001}],
                                              0, address, 0, None, True, False, 0.0001, [], True, None, None, False)
    assert node.wallet.walletcreatefundedpsbt([{"txid": txid, "vout": vout}],
                                              [{address: 0.00001}],
                                              0, None, 0, "legacy", True, False, None, [], True, 1, "UNSET", False)
    assert node.wallet.walletcreatefundedpsbt(inputs=[{"txid": txid, "vout": vout}],
                                              outputs=[{address: 0.00001}],
                                              locktime=0,
                                              changeAddress=address,
                                              changePosition=0,
                                              change_type=None,
                                              includeWatching=True,
                                              lockUnspents=False,
                                              feeRate=None,
                                              subtractFeeFromOutputs=[],
                                              replaceable=True,
                                              conf_target=1,
                                              estimate_mode="UNSET",
                                              bip32derivs=False)


@pytest.mark.query
def test_walletlock():  # 52
    assert node.wallet.walletlock() is None
    node.wallet.walletpassphrase(load_secrets_conf()["wallet_password"], 3600)


@pytest.mark.query
def test_walletpassphrase():  # 53
    assert node.wallet.walletpassphrase(load_secrets_conf()["wallet_password"], 3600) is None
    assert node.wallet.walletpassphrase(passphrase=load_secrets_conf()["wallet_password"], timeout=3600) is None


@pytest.mark.query
def test_walletpassphrasechange():  # 54
    secrets = load_secrets_conf()
    assert node.wallet.walletpassphrasechange(secrets["wallet_password"], secrets["wallet_password"]) is None
    assert node.wallet.walletpassphrasechange(oldpassphrase=secrets["wallet_password"],
                                              newpassphrase=secrets["wallet_password"]) is None


@pytest.mark.query
def test_walletprocesspsbt():  # 55
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]
    psbt = node.rawtransactions.createpsbt([{"txid": txid, "vout": vout}], [{address: 0.00000001}], 0, True)

    assert node.wallet.walletprocesspsbt(psbt)
    assert node.wallet.walletprocesspsbt(psbt, True, "ALL", False)
    assert node.wallet.walletprocesspsbt(psbt=psbt, sign=True, sighashtype="ALL", bip32derivs=False)
