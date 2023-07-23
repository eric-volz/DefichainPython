import pytest

from defichain.transactions.rawtransactions import TxOutput, TxAddressOutput, TxDataOutput, TxDefiOutput
from defichain.networks import DefichainMainnet

from . import TestOutputs, Addresses


@pytest.mark.transactions
def test_address_output():  # 01
    txP2PKHOutput = TxAddressOutput(TestOutputs.VALUE, Addresses.P2PKH, 0)
    txP2SHOutput = TxAddressOutput(TestOutputs.VALUE, Addresses.P2SH, 0)
    txP2WPKHOutput = TxAddressOutput(TestOutputs.VALUE, Addresses.P2WPKH, 0)

    assert TxAddressOutput(value=TestOutputs.VALUE, address=Addresses.P2PKH, tokenId=0)

    assert txP2PKHOutput.serialize() == TestOutputs.P2PKH_Address_Output_Serialized
    assert txP2SHOutput.serialize() == TestOutputs.P2SH_Address_Output_Serialized
    assert txP2WPKHOutput.serialize() == TestOutputs.P2WPKH_Address_Output_Serialized

    assert TxOutput.deserialize(DefichainMainnet, TestOutputs.P2PKH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2PKH_Address_Output_Serialized
    assert TxOutput.deserialize(DefichainMainnet, TestOutputs.P2SH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2SH_Address_Output_Serialized
    assert TxOutput.deserialize(DefichainMainnet, TestOutputs.P2WPKH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2WPKH_Address_Output_Serialized
    assert TxOutput.deserialize(network=DefichainMainnet,
                                hex=TestOutputs.P2WPKH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2WPKH_Address_Output_Serialized

    assert TxAddressOutput.deserialize(DefichainMainnet, TestOutputs.P2PKH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2PKH_Address_Output_Serialized
    assert TxAddressOutput.deserialize(DefichainMainnet, TestOutputs.P2SH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2SH_Address_Output_Serialized
    assert TxAddressOutput.deserialize(DefichainMainnet, TestOutputs.P2WPKH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2WPKH_Address_Output_Serialized
    assert TxAddressOutput.deserialize(network=DefichainMainnet,
                                       hex=TestOutputs.P2WPKH_Address_Output_Serialized).serialize() == \
           TestOutputs.P2WPKH_Address_Output_Serialized


@pytest.mark.transactions
def test_data_output():  # 02
    txDataOutput = TxDataOutput(TestOutputs.DATA, 0)

    assert TxDataOutput(data=TestOutputs.DATA, tokenId=0)

    assert txDataOutput.serialize() == TestOutputs.Data_Output_Serialized

    assert TxOutput.deserialize(DefichainMainnet, TestOutputs.Data_Output_Serialized).serialize() == \
           TestOutputs.Data_Output_Serialized
    assert TxOutput.deserialize(network=DefichainMainnet, hex=TestOutputs.Data_Output_Serialized).serialize() == \
           TestOutputs.Data_Output_Serialized

    assert TxDataOutput.deserialize(DefichainMainnet, TestOutputs.Data_Output_Serialized).serialize() == \
           TestOutputs.Data_Output_Serialized
    assert TxDataOutput.deserialize(network=DefichainMainnet, hex=TestOutputs.Data_Output_Serialized).serialize() == \
           TestOutputs.Data_Output_Serialized


@pytest.mark.transactions
def test_defi_output():  # 03
    txDefiOutput = TxDefiOutput(1, TestOutputs.DefiTx, 0)

    assert TxDefiOutput(1, TestOutputs.DefiTx, 0)

    assert txDefiOutput.serialize() == TestOutputs.DefiTx_Output_Serialized

    assert TxOutput.deserialize(DefichainMainnet, TestOutputs.DefiTx_Output_Serialized).serialize() == \
           TestOutputs.DefiTx_Output_Serialized
    assert TxOutput.deserialize(network=DefichainMainnet, hex=TestOutputs.DefiTx_Output_Serialized).serialize() == \
           TestOutputs.DefiTx_Output_Serialized

    assert TxDefiOutput.deserialize(DefichainMainnet, TestOutputs.DefiTx_Output_Serialized).serialize() == \
           TestOutputs.DefiTx_Output_Serialized
    assert TxDefiOutput.deserialize(network=DefichainMainnet, hex=TestOutputs.DefiTx_Output_Serialized).serialize() == \
           TestOutputs.DefiTx_Output_Serialized

