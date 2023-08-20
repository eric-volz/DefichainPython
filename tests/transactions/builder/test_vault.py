import pytest
from . import builder_p2wpkh, TestVault, Addresses

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_createvault():  # 01
    tx = builder_p2wpkh.vault.createvault(ownerAddress=Addresses.P2WPKH, schemeId="MIN150", inputs=[TestVault.input])

    assert tx.serialize() == TestVault.create_vault_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_deposittovault():  # 02
    tx = builder_p2wpkh.vault.deposittovault(vaultId=TestVault.vault_id,
                                             addressFrom=Addresses.P2WPKH,
                                             amount=TestVault.amount)

    assert tx.serialize() == TestVault.deposit_to_vault_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_withdrawfromvault():  # 03
    tx = builder_p2wpkh.vault.deposittovault(vaultId=TestVault.vault_id,
                                             addressFrom=Addresses.P2WPKH,
                                             amount=TestVault.amount)

    assert tx.serialize() == TestVault.withdraw_from_vault_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()
