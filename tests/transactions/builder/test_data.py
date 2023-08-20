import pytest
from . import builder_p2wpkh, Addresses, TestData

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_hex_data():  # 01
    tx = builder_p2wpkh.data.hex_data(data=TestData.hex, addressAmountTo=TestData.addressAmountTo.build(),
                                      changeAddress=Addresses.P2WPKH)

    assert tx.serialize() == TestData.hex_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()


@pytest.mark.transactions
def test_str_data():  # 02
    tx = builder_p2wpkh.data.str_data(data=TestData.string, addressAmountTo=TestData.addressAmountTo.build(),
                                      changeAddress=Addresses.P2WPKH)

    assert tx.serialize() == TestData.hex_serialized

    assert Transaction.deserialize(DefichainMainnet, tx.serialize()).serialize() == tx.serialize()
