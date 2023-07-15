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
