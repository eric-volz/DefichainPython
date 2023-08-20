import pytest
from . import builder_p2wpkh, TestMasternode

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_createmasternode():  # 01
    tx = builder_p2wpkh.masternode.createmasternode(operatorAddress=TestMasternode.operatorAddress,
                                                    timeLock=0, inputs=[TestMasternode.input])

    assert tx.serialize() == TestMasternode.createmasternode_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_resignmasternode():  # 02
    tx = builder_p2wpkh.masternode.resignmasternode(masternodeId=TestMasternode.mn_id)

    assert tx.serialize() == TestMasternode.resignmasternode_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_updatemasternode():  # 03
    tx = builder_p2wpkh.masternode.updatemasternode(masternodeId=TestMasternode.mn_id,
                                                    ownerAddress=TestMasternode.ownerAddress,
                                                    operatorAddress=TestMasternode.operatorAddress,
                                                    rewardAddress=TestMasternode.rewardAddress)

    assert tx.serialize() == TestMasternode.updatemasternode_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()
