import pytest
from . import builder_p2pkh, builder_p2sh, builder_p2wpkh, Addresses, TestUTXO

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_send():  # 01
    tx_p2pkh = builder_p2pkh.utxo.send(amount=0.00001, addressTo=Addresses.P2WPKH,
                                       changeAddress=builder_p2pkh.get_address())
    tx_p2sh = builder_p2sh.utxo.send(amount=0.00001, addressTo=Addresses.P2WPKH)
    tx_p2wpkh = builder_p2wpkh.utxo.send(amount=0.00001, addressTo=Addresses.P2WPKH)

    assert tx_p2pkh.serialize() == TestUTXO.send_p2pkh_serialized
    assert tx_p2sh.serialize() == TestUTXO.send_p2sh_serialized
    assert tx_p2wpkh.serialize() == TestUTXO.send_p2wpkh_serialized

    assert Transaction.deserialize(DefichainMainnet, tx_p2pkh.serialize()).serialize() == tx_p2pkh.serialize()
    assert Transaction.deserialize(DefichainMainnet, tx_p2sh.serialize()).serialize() == tx_p2sh.serialize()
    assert Transaction.deserialize(DefichainMainnet, tx_p2wpkh.serialize()).serialize() == tx_p2wpkh.serialize()


@pytest.mark.transactions
def test_sendall():  # 02
    tx = builder_p2wpkh.utxo.sendall(addressTo=Addresses.P2WPKH)

    assert tx.serialize() == TestUTXO.sendall_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_sendmany():  # 03
    tx_p2wpkh = builder_p2wpkh.utxo.sendmany(addressAmountTo=TestUTXO.addressAmountTo.build())
    tx_p2pkh = builder_p2wpkh.utxo.sendmany(addressAmountTo=TestUTXO.addressAmountTo.build(),
                                            changeAddress=Addresses.P2PKH)

    assert tx_p2wpkh.serialize() == TestUTXO.sendmany_same_change_address_serialized
    assert tx_p2pkh.serialize() == TestUTXO.sendmany_different_change_address_serialized

    assert Transaction.deserialize(DefichainMainnet, tx_p2wpkh.serialize()).serialize() == tx_p2wpkh.serialize()
    assert Transaction.deserialize(DefichainMainnet, tx_p2pkh.serialize()).serialize() == tx_p2pkh.serialize()
