import pytest
from . import builder_p2wpkh, Addresses, TestAccounts

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_utxotoaccount():  # 01
    tx = builder_p2wpkh.accounts.utxostoaccount(address=Addresses.P2WPKH, amount=0.00001, tokenId=0)

    assert tx.serialize() == TestAccounts.utxo_to_account_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_accounttoutxo():  # 02
    tx = builder_p2wpkh.accounts.accounttoutxos(addressFrom=Addresses.P2WPKH,
                                                addressAmountTo=TestAccounts.addressAmountTo.build())

    assert tx.serialize() == TestAccounts.account_to_utxo_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_accounttoaccount():  # 03
    tx = builder_p2wpkh.accounts.accounttoaccount(addressFrom=Addresses.P2WPKH,
                                                  addressAmountTo=TestAccounts.addressAmountTo.build())

    assert tx.serialize() == TestAccounts.account_to_account_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()
