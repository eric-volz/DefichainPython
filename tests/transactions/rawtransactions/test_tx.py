import pytest

from defichain import Ocean
from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet

from . import TestTx, Addresses


@pytest.mark.transactions
def test_create_transaction():  # 01
    for i in range(len(TestTx.tx_unsigned)):
        assert TestTx.tx_unsigned[i].serialize() == TestTx.serialized_unsigned[i]


@pytest.mark.transactions
def test_deserialize_transaction():  # 02
    for i in TestTx.serialized_unsigned:
        assert Transaction.deserialize(DefichainMainnet, i).serialize() == i

    for i in TestTx.serialized_signed:
        assert Transaction.deserialize(DefichainMainnet, i).serialize() == i


@pytest.mark.transactions
def test_sign_transaction():  # 03
    for i in range(len(TestTx.tx_signed)):
        assert TestTx.tx_signed[i].serialize() == TestTx.serialized_signed[i]


@pytest.mark.transactions
def test_fee_transaction():  # 05
    for i in range(len(TestTx.tx_unsigned)):
        assert TestTx.tx_unsigned[i].get_fee() == TestTx.fee[i]

    for i in range(len(TestTx.tx_signed)):
        assert TestTx.tx_signed[i].get_fee() == TestTx.fee[i]


@pytest.mark.transactions
def test_txid_transaction():  # 07
    for i in range(len(TestTx.tx_signed)):
        assert TestTx.tx_signed[i].get_txid() == TestTx.txid[i]


@pytest.mark.transactions
def test_unspent_transaction():  # 06
    for tx in TestTx.tx_signed:
        for unspent in tx.get_unspent([Addresses.P2WPKH]):
            assert unspent.serialize() in TestTx.unspent_inputs



