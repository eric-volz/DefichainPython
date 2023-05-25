import pytest

from . import TestCalculate
from defichain.transactions.utils import Calculate


@pytest.mark.transactions
def test_dHash256():  # 01
    assert Calculate.dHash256(bytes.fromhex("6a")).hex() == TestCalculate.DHASH


@pytest.mark.transactions
def test_length_varInt():  # 02
    assert Calculate.length_varInt(TestCalculate.VARINT) == 3


@pytest.mark.transactions
def test_write_varInt():  # 03
    assert Calculate.write_varInt(TestCalculate.INT) == TestCalculate.VARINT


@pytest.mark.transactions
def test_raed_varInt():  # 04
    assert Calculate.read_varInt(TestCalculate.VARINT) == TestCalculate.INT


@pytest.mark.transactions
def test_length_compactSize():  # 05
    assert Calculate.length_compactSize(TestCalculate.COMPACTSIZE) == 3


@pytest.mark.transactions
def test_write_compactSize():  # 06
    assert Calculate.write_compactSize(TestCalculate.INT) == TestCalculate.COMPACTSIZE


@pytest.mark.transactions
def test_raed_compactSize():  # 07
    assert Calculate.read_compactSize(TestCalculate.COMPACTSIZE) == TestCalculate.INT


@pytest.mark.transactions
def test_addressAmountSum():  # 08
    assert Calculate.addressAmountSum(TestCalculate.ADDRESSAMOUNT) == 32898
