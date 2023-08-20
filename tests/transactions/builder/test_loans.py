import pytest
from . import builder_p2wpkh, TestLoans, Addresses

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_takeloan():  # 01
    tx = builder_p2wpkh.loans.takeloan(TestLoans.vault_id, Addresses.P2WPKH, TestLoans.amounts)

    assert tx.serialize() == TestLoans.take_loan_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_paybackloan():  # 02
    tx = builder_p2wpkh.loans.paybackloan(TestLoans.vault_id, Addresses.P2WPKH, TestLoans.amounts)

    assert tx.serialize() == TestLoans.payback_loan_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()

