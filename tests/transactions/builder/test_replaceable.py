import pytest
from . import builder_replaceable, TestReplaceableTransactions, Addresses

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_replaceable():  # 01
    tx = builder_replaceable.utxo.sendall(Addresses.P2WPKH)

    assert tx.serialize() == TestReplaceableTransactions.replaceable_transaction_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()