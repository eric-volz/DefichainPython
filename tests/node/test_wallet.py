import pytest
from tests.util import createNode, load_secrets_conf

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
    assert node.wallet.backupwallet("backup") is None
    assert node.wallet.backupwallet(destination="backup") is None


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
    string = ".* RPC_WALLET_ERROR: Wallet tests_wallet already exists."
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.createwallet("tests_wallet")
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.createwallet("tests_wallet", False, False, "", False)
    with pytest.raises(InternalServerError, match=string):
        assert node.wallet.createwallet(wallet_name="tests_wallet", disable_private_keys=False, blank=False,
                                        passphrase="", avoid_reuse=False)

@pytest.mark.query
def test_dumpprivkey():  # 07
    assert node.wallet.dumpprivkey(address)
    assert node.wallet.dumpprivkey(address=address)

