import pytest
from . import builder_p2wpkh, TestPool

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_poolswap():  # 01
    tx = builder_p2wpkh.pool.poolswap(addressFrom=TestPool.addressFrom, tokenFrom=TestPool.tokenFrom,
                                      amountFrom=TestPool.amountFrom, tokenTo=TestPool.tokenTo,
                                      addressTo=TestPool.addressTo, maxPrice=TestPool.maxPrice)

    assert tx.serialize() == TestPool.poolswap_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_compositeswap():  # 02
    tx = builder_p2wpkh.pool.compositeswap(addressFrom=TestPool.addressFrom, tokenFrom=TestPool.tokenFrom,
                                           amountFrom=TestPool.amountFrom, tokenTo=TestPool.tokenTo,
                                           addressTo=TestPool.addressTo, maxPrice=TestPool.maxPrice,
                                           pools=TestPool.pools)

    assert tx.serialize() == TestPool.compositeswap_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_addpoolliquidity():  # 03
    tx = builder_p2wpkh.pool.addpoolliquidity(addressAmountFrom=TestPool.addressAmountFrom.build(),
                                              shareAddress=TestPool.addressFrom)

    assert tx.serialize() == TestPool.addpoolliquidity_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_removepoolliquidity():  # 04
    tx = builder_p2wpkh.pool.removepoolliquidity(addressFrom=TestPool.addressFrom, amount=TestPool.amount)

    assert tx.serialize() == TestPool.removepoolliquidity_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()
