import pytest

from . import TestConverter
from defichain.transactions.utils import Converter


@pytest.mark.transactions
def test_int_to_bytes():  # 01
    assert Converter.int_to_bytes(TestConverter.INT, 5) == TestConverter.BYTES


@pytest.mark.transactions
def test_bytes_to_int():  # 02
    assert Converter.bytes_to_int(TestConverter.BYTES) == TestConverter.INT


@pytest.mark.transactions
def test_hex_to_bytes():  # 03
    assert Converter.hex_to_bytes(TestConverter.HEX) == TestConverter.BYTES


@pytest.mark.transactions
def test_bytes_to_hex():  # 04
    assert Converter.bytes_to_hex(TestConverter.BYTES) == TestConverter.HEX


@pytest.mark.transactions
def test_hex_to_int():  # 05
    assert Converter.hex_to_int(TestConverter.HEX) == TestConverter.INT


@pytest.mark.transactions
def test_int_to_hex():  # 06
    assert Converter.int_to_hex(TestConverter.INT, 5) == TestConverter.HEX


@pytest.mark.transactions
def test_str_to_hex():  # 07
    assert Converter.str_to_hex(TestConverter.STR) == TestConverter.HEX


@pytest.mark.transactions
def test_hex_to_str():  # 08
    assert Converter.hex_to_str(TestConverter.HEX) == TestConverter.STR


@pytest.mark.transactions
def test_float_to_int():  # 09
    assert Converter.float_to_int(TestConverter.FLOAT) == TestConverter.INT


@pytest.mark.transactions
def test_int_to_float():  # 10
    assert Converter.int_to_float(TestConverter.INT) == TestConverter.FLOAT


@pytest.mark.transactions
def test_amount_float_to_int():  # 11
    assert Converter.amount_float_to_int(TestConverter.AMOUNT_FLOAT) == TestConverter.AMOUNT_INT


@pytest.mark.transactions
def test_addressAmount_float_to_int():  # 12
    assert Converter.addressAmount_float_to_int(TestConverter.ADDRESS_AMOUNT_FLOAT) == TestConverter.ADDRESS_AMOUNT_INT
