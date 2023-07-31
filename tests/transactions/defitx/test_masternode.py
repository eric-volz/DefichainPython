import pytest

from defichain.networks import DefichainMainnet
from defichain.transactions.defitx import DefiTx, CreateMasternode, ResignMasternode, UpdateMasternode
from . import Addresses, TestMasternode


@pytest.mark.transactions
def test_create_masternode():  # 01
    create_masternode_0: CreateMasternode = CreateMasternode(operatorAddress=TestMasternode.operatorAddress, timeLock=0)
    create_masternode_5: CreateMasternode = CreateMasternode(operatorAddress=TestMasternode.operatorAddress, timeLock=5)
    create_masternode_10: CreateMasternode = CreateMasternode(operatorAddress=TestMasternode.operatorAddress,
                                                              timeLock=10)

    assert create_masternode_0.serialize() == TestMasternode.create_massternode_timelock_0_serialized
    assert create_masternode_5.serialize() == TestMasternode.create_massternode_timelock_5_serialized
    assert create_masternode_10.serialize() == TestMasternode.create_massternode_timelock_10_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestMasternode.create_massternode_timelock_0_serialized).serialize() == \
           TestMasternode.create_massternode_timelock_0_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestMasternode.create_massternode_timelock_5_serialized).serialize() == \
           TestMasternode.create_massternode_timelock_5_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestMasternode.create_massternode_timelock_10_serialized).serialize() == \
           TestMasternode.create_massternode_timelock_10_serialized


@pytest.mark.transactions
def test_resign_masternode():  # 02
    resignMasternode: ResignMasternode = ResignMasternode(masternodeId=TestMasternode.mn_id)

    assert resignMasternode.serialize() == TestMasternode.resign_masternode_serialized

    assert DefiTx.deserialize(DefichainMainnet, resignMasternode.serialize()).serialize() == \
           TestMasternode.resign_masternode_serialized


@pytest.mark.transactions
def test_update_masternode():  # 03
    updateMasternode: UpdateMasternode = UpdateMasternode(masternodeId=TestMasternode.mn_id,
                                                          operatorAddress=TestMasternode.operatorAddress,
                                                          ownerAddress=TestMasternode.ownerAddress,
                                                          rewardAddress=TestMasternode.rewardAddress)

    assert updateMasternode.serialize() == TestMasternode.update_masternode_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestMasternode.update_masternode_serialized).serialize() == \
           TestMasternode.update_masternode_serialized
