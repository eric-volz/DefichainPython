import pytest

from defichain.transactions.rawtransactions import estimate_fee
from . import TestFee


@pytest.mark.transactions
def test_p2pkh_inputs():  # 01
    assert estimate_fee(TestFee.P2PKH_Input_Tx, 1) == 192


@pytest.mark.transactions
def test_p2sh_inputs():  # 02
    assert estimate_fee(TestFee.P2SH_Input_Tx, 1) == 215


@pytest.mark.transactions
def test_p2wpkh_inputs():  # 03
    assert estimate_fee(TestFee.P2WPKH_Input_Tx, 1) == 192


@pytest.mark.transactions
def test_p2pkh_and_p2sh_inputs():  # 04
    assert estimate_fee(TestFee.P2PKH_and_P2SH_Input_Tx, 1) == 363


@pytest.mark.transactions
def test_p2pkh_and_p2wpkh_inputs():  # 05
    assert estimate_fee(TestFee.P2PKH_and_P2WPKH_Input_Tx, 1) == 340


@pytest.mark.transactions
def test_p2sh_and_p2wpkh_inputs():  # 06
    assert estimate_fee(TestFee.P2SH_and_P2WPKH_Input_Tx, 1) == 365


@pytest.mark.transactions
def test_p2pkh_and_p2sh_and_p2wpkh_inputs():  # 07
    assert estimate_fee(TestFee.P2PKH_and_P2SH_and_P2WPKH_Input_Tx, 1) == 513
