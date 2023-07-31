import pytest

from defichain.networks import DefichainMainnet
from defichain.transactions.defitx import DefiTx, PoolSwap, CompositeSwap, AddPoolLiquidity, RemovePoolLiquidity
from . import Addresses, TestPool


@pytest.mark.transactions
def test_poolswap():  # 01
    poolswap: PoolSwap = PoolSwap(addressFrom=TestPool.addressFrom, tokenFrom=TestPool.tokenFrom,
                                  amountFrom=TestPool.amountFrom, addressTo=TestPool.addressTo,
                                  tokenTo=TestPool.tokenTo, maxPrice=TestPool.maxPrice)

    assert poolswap.serialize() == TestPool.poolswap_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestPool.poolswap_serialized).serialize() == \
           TestPool.poolswap_serialized


@pytest.mark.transactions
def test_compositeswap():  # 02
    compositeswap: CompositeSwap = CompositeSwap(addressFrom=TestPool.addressFrom, tokenFrom=TestPool.tokenFrom,
                                                 amountFrom=TestPool.amountFrom, addressTo=TestPool.addressTo,
                                                 tokenTo=TestPool.tokenTo2, maxPrice=TestPool.maxPrice,
                                                 pools=TestPool.pools)

    assert compositeswap.serialize() == TestPool.compositeswap_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestPool.compositeswap_serialized).serialize() == \
           TestPool.compositeswap_serialized


@pytest.mark.transactions
def test_addpoolliquidity():  # 03
    addpoolliquidity: AddPoolLiquidity = AddPoolLiquidity(addressAmount=TestPool.addressAmount,
                                                          shareAddress=Addresses.P2WPKH)

    assert addpoolliquidity.serialize() == TestPool.addpoolliquidity_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestPool.addpoolliquidity_serialized).serialize() == \
           TestPool.addpoolliquidity_serialized


@pytest.mark.transactions
def test_removepoolliquidity():  # 04
    removepoolliquidity: RemovePoolLiquidity = RemovePoolLiquidity(addressFrom=Addresses.P2WPKH,
                                                                   amount=TestPool.removeAmount)

    assert removepoolliquidity.serialize() == TestPool.removepoolliquidity_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestPool.removepoolliquidity_serialized).serialize() == \
           TestPool.removepoolliquidity_serialized
