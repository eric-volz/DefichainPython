import pytest

from defichain.transactions.rawtransactions import TxInput, TxP2PKHInput, TxP2SHInput, TxP2WPKHInput
from defichain.transactions.constants.rawtransactions import SEQUENCE
from defichain.networks import DefichainMainnet

from . import TestInputs, Addresses


@pytest.mark.transactions
def test_p2pkh_inputs():  # 01
    txInput = TxP2PKHInput(TestInputs.TXID, TestInputs.VOUT, Addresses.P2PKH)
    assert TxP2PKHInput(txid=TestInputs.TXID, vout=TestInputs.VOUT, address=Addresses.P2PKH, value=TestInputs.VALUE,
                        sequence=SEQUENCE)
    assert txInput.serialize() == TestInputs.P2PKH_Input_Serialized
    assert TxInput.deserialize(DefichainMainnet, TestInputs.P2PKH_Input_Serialized).serialize() == \
           TestInputs.P2PKH_Input_Serialized
    assert TxP2PKHInput.deserialize(DefichainMainnet, TestInputs.P2PKH_Input_Serialized).serialize() == \
           TestInputs.P2PKH_Input_Serialized


@pytest.mark.transactions
def test_p2sh_inputs():  # 02
    txInput = TxP2SHInput(TestInputs.TXID, TestInputs.VOUT, Addresses.P2WPKH, TestInputs.VALUE)
    assert TxP2SHInput(txid=TestInputs.TXID, vout=TestInputs.VOUT, address=Addresses.P2WPKH, value=TestInputs.VALUE,
                       sequence=SEQUENCE)
    assert txInput.serialize() == TestInputs.P2SH_Input_Serialized
    assert TxInput.deserialize(DefichainMainnet, TestInputs.P2SH_Input_Serialized).serialize() == \
           TestInputs.P2SH_Input_Serialized
    assert TxP2SHInput.deserialize(DefichainMainnet, TestInputs.P2SH_Input_Serialized).serialize() == \
           TestInputs.P2SH_Input_Serialized


@pytest.mark.transactions
def test_p2wpkh_inputs():  # 03
    txInput = TxP2WPKHInput(TestInputs.TXID, TestInputs.VOUT, Addresses.P2WPKH, TestInputs.VALUE)
    assert TxP2WPKHInput(txid=TestInputs.TXID, vout=TestInputs.VOUT, address=Addresses.P2WPKH, value=TestInputs.VALUE, sequence=SEQUENCE)
    assert txInput.serialize() == TestInputs.P2WPKH_Input_Serialized
    assert TxInput.deserialize(DefichainMainnet, TestInputs.P2WPKH_Input_Serialized).serialize() == \
           TestInputs.P2WPKH_Input_Serialized
    assert TxP2SHInput.deserialize(DefichainMainnet, TestInputs.P2WPKH_Input_Serialized).serialize() == \
           TestInputs.P2WPKH_Input_Serialized
