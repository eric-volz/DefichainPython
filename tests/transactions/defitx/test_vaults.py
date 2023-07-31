import pytest

from defichain.networks import DefichainMainnet
from defichain.transactions.defitx import DefiTx, CreateVault, DepositToVault, WithdrawFromVault
from . import Addresses, TestVaults


@pytest.mark.transactions
def test_craetevault():  # 01
    createvault: CreateVault = CreateVault(ownerAddress=TestVaults.ownerAddress, schemeId=TestVaults.schemeId)

    assert createvault.serialize() == TestVaults.createvault_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestVaults.createvault_serialized).serialize() == \
           TestVaults.createvault_serialized


@pytest.mark.transactions
def test_deposittovault():  # 02
    deposittovault: DepositToVault = DepositToVault(vaultId=TestVaults.vaultId, addressFrom=TestVaults.addressFrom,
                                                    amount=TestVaults.amount)

    assert deposittovault.serialize() == TestVaults.deposittovault_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestVaults.deposittovault_serialized).serialize() == \
           TestVaults.deposittovault_serialized


@pytest.mark.transactions
def test_withdrawfromvault():  # 03
    withdrawfromvault: WithdrawFromVault = WithdrawFromVault(vaultId=TestVaults.vaultId, addressTo=TestVaults.addressTo,
                                                             amount=TestVaults.amount)

    assert withdrawfromvault.serialize() == TestVaults.withdrawfromvault_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestVaults.withdrawfromvault_serialized).serialize() == \
           TestVaults.withdrawfromvault_serialized
