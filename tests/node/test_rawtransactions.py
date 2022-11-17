import pytest
from tests.util import load_secrets_conf
import time

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

from . import node
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.query
def test_analyzepsbt():  # 01
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)
    psbt = node.rawtransactions.converttopsbt(raw_tx)
    assert node.rawtransactions.analyzepsbt(psbt)
    assert node.rawtransactions.analyzepsbt(psbt=psbt)


@pytest.mark.query
def test_combinepsbt():  # 02
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)
    psbt = node.rawtransactions.converttopsbt(raw_tx)
    assert node.rawtransactions.combinepsbt([psbt])
    assert node.rawtransactions.combinepsbt(txs=[psbt])


@pytest.mark.query
def test_combinerawtransaction():  # 03
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    string = ".* RPC_DESERIALIZATION_ERROR: Missing transactions"
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.combinerawtransaction([])
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.combinerawtransaction(txs=[])


@pytest.mark.query
def test_converttopsbt():  # 04
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)
    assert node.rawtransactions.converttopsbt(raw_tx)
    assert node.rawtransactions.converttopsbt(raw_tx, False, False)
    assert node.rawtransactions.converttopsbt(hexstring=raw_tx, permitsigdata=False, iswitness=False)


@pytest.mark.query
def test_createpsbt():  # 05
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    assert node.rawtransactions.createpsbt([{"txid": txid, "vout": vout}], [{address: 0.00000001}])
    assert node.rawtransactions.createpsbt([{"txid": txid, "vout": vout}], [{address: 0.00000001}], 0, True)
    assert node.rawtransactions.createpsbt(inputs=[{"txid": txid, "vout": vout}], outputs=[{address: 0.00000001}],
                                           locktime=0, replaceable=True)


@pytest.mark.query
def test_createrawtransaction():  # 06
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    assert node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}], [{address: 0.00000001}])
    assert node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}], [{address: 0.00000001}], 0, True)
    assert node.rawtransactions.createrawtransaction(inputs=[{"txid": txid, "vout": vout}],
                                                     outputs=[{address: 0.00000001}],
                                                     locktime=0, replaceable=True)


@pytest.mark.query
def test_decodepsbt():  # 07
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]
    psbt = node.rawtransactions.createpsbt([{"txid": txid, "vout": vout}], [{address: 0.00000001}], 0, True)

    assert node.rawtransactions.decodepsbt(psbt)
    assert node.rawtransactions.decodepsbt(psbt=psbt)


@pytest.mark.query
def test_decoderawtransaction():  # 08
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)

    assert node.rawtransactions.decoderawtransaction(raw_tx)
    assert node.rawtransactions.decoderawtransaction(raw_tx, True)
    assert node.rawtransactions.decoderawtransaction(hexstring=raw_tx, iswitness=True)


@pytest.mark.query
def test_decodescript():  # 09
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)
    assert node.rawtransactions.decodescript(raw_tx)
    assert node.rawtransactions.decodescript(hexstring=raw_tx)


@pytest.mark.query
def test_finalizepsbt():  # 10
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    psbt = node.rawtransactions.createpsbt([{"txid": txid, "vout": vout}],
                                           [{address: 0.00000001}], 0, True)

    assert node.rawtransactions.finalizepsbt(psbt)
    assert node.rawtransactions.finalizepsbt(psbt, True)
    assert node.rawtransactions.finalizepsbt(psbt=psbt, extract=True)


@pytest.mark.query
def test_fundrawtransaction():  # 11
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00001}], 0, True)
    assert node.rawtransactions.fundrawtransaction(raw_tx, address, 0, None, False, False, None, [], True, None,
                                                   "UNSET", True)
    assert node.rawtransactions.fundrawtransaction(raw_tx, None, 0, "legacy", False, False, None, [], True, 1, "UNSET",
                                                   True)
    assert node.rawtransactions.fundrawtransaction(hexstring=raw_tx, changeAddress=address, changePosition=0,
                                                   change_type=None, includeWatching=False, lockUnspents=False,
                                                   feeRate=None, subtractFeeFromOutputs=[], replaceable=True,
                                                   conf_target=1, estimate_mode="UNSET", iswitness=True)


@pytest.mark.query
def test_getrawtransaction():  # 12
    txid = "0e44c71ac4f84a8dc422dc9e22158939c3c2724b9bcfae21acb2b523f058c164"
    blockhash = "ebeae29e1279aebce345e63656446d79e7a18cd7631de7d19025ddf80a20afa7"
    assert node.rawtransactions.getrawtransaction(txid, blockhash=blockhash)
    assert node.rawtransactions.getrawtransaction(txid, False, blockhash)
    assert node.rawtransactions.getrawtransaction(txid=txid, verbose=False, blockhash=blockhash)


@pytest.mark.query
def test_joinpsbts():  # 13
    string = ".* RPC_INVALID_PARAMETER: At least two PSBTs are required to join PSBTs."
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.joinpsbts([])
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.joinpsbts(txs=[])


@pytest.mark.query
def test_sendrawtransaction():  # 14
    HEX = "0400000001616cd43cb0d396c52d6a5342f9411307a4dc4847f9237ff8bbb62e0c247be803010000006a4730440220119839df669b" \
          "f6eb24dd7b806cdb782ffc1ffa892fd663b5be6bf3d22cc9fdd9022028f4e981bcbcfbec0ff508a9b67fd353840ed3132c4528ecc8" \
          "94b90cda49382f012102d9438499f4280c74afa1e9cf1d3df9cff599d05740d9355acc6be97f45575251fdffffff0262390f000000" \
          "00001976a9147d8c7b0c6e867e3034afc49eabc16ed33590400388ac007950d705000000001976a9147d8c7b0c6e867e3034afc49e" \
          "abc16ed33590400388ac0000000000"
    string = ".* RPC_VERIFY_ERROR: Missing inputs"
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.sendrawtransaction(HEX)
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.sendrawtransaction(HEX, 0.1)
    with pytest.raises(InternalServerError, match=string):
        assert node.rawtransactions.sendrawtransaction(hexstring=HEX, maxfeerate=0.1)


@pytest.mark.query
def test_signrawtransactionwithkey():  # 15
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    key = node.wallet.dumpprivkey(address)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    raw_tx = node.rawtransactions.createrawtransaction([{"txid": txid, "vout": vout}],
                                                       [{address: 0.00000001}], 0, True)

    assert node.rawtransactions.signrawtransactionwithkey(raw_tx, [key])
    assert node.rawtransactions.signrawtransactionwithkey(raw_tx, [key], [], "ALL")
    assert node.rawtransactions.signrawtransactionwithkey(hexstring=raw_tx, privatekey=[key], prevtxs=[],
                                                          sighashtype="ALL")


@pytest.mark.query
def test_testmempoolaccept():  # 16
    HEX = "0400000001616cd43cb0d396c52d6a5342f9411307a4dc4847f9237ff8bbb62e0c247be803010000006a4730440220119839df669b" \
          "f6eb24dd7b806cdb782ffc1ffa892fd663b5be6bf3d22cc9fdd9022028f4e981bcbcfbec0ff508a9b67fd353840ed3132c4528ecc8" \
          "94b90cda49382f012102d9438499f4280c74afa1e9cf1d3df9cff599d05740d9355acc6be97f45575251fdffffff0262390f000000" \
          "00001976a9147d8c7b0c6e867e3034afc49eabc16ed33590400388ac007950d705000000001976a9147d8c7b0c6e867e3034afc49e" \
          "abc16ed33590400388ac0000000000"
    assert node.rawtransactions.testmempoolaccept([HEX])
    assert node.rawtransactions.testmempoolaccept([HEX], 0.1)
    assert node.rawtransactions.testmempoolaccept(rawtxs=[HEX], maxfeerate=0.1)


@pytest.mark.query
def test_utxoupdatepsbt():  # 17
    # Wait for valid unspent parameter
    while not node.wallet.listunspent(addresses=[address]):
        time.sleep(0.5)

    unspent = node.wallet.listunspent(addresses=[address])
    txid = unspent[0]["txid"]
    vout = unspent[0]["vout"]

    psbt = node.rawtransactions.createpsbt([{"txid": txid, "vout": vout}],
                                           [{address: 0.00000001}], 0, True)

    assert node.rawtransactions.utxoupdatepsbt(psbt)
    assert node.rawtransactions.utxoupdatepsbt(psbt, [])
    assert node.rawtransactions.utxoupdatepsbt(psbt=psbt, descriptors=[])
