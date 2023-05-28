import pytest

from . import TestVerify
from defichain.exceptions.transactions import VerifyError
from defichain.transactions.utils import Verify


@pytest.mark.transactions
def test_is_hex():  # 01
    assert Verify.is_hex(TestVerify.HEX_TRUE) is True
    with pytest.raises(VerifyError):
        assert Verify.is_hex(TestVerify.HEX_FALSE)


@pytest.mark.transactions
def test_is_int():  # 02
    assert Verify.is_int(TestVerify.INT_TRUE) is True
    with pytest.raises(VerifyError):
        assert Verify.is_int(TestVerify.INT_FALSE)


@pytest.mark.transactions
def test_is_float():  # 03
    assert Verify.is_float(TestVerify.FLOAT_TRUE) is True
    with pytest.raises(VerifyError):
        assert Verify.is_float(TestVerify.FLOAT_FALSE)


@pytest.mark.transactions
def test_is_str():  # 04
    assert Verify.is_str(TestVerify.STR_TRUE) is True
    with pytest.raises(VerifyError):
        assert Verify.is_str(TestVerify.STR_FALSE)


@pytest.mark.transactions
def test_is_only_number_str():  # 05
    assert Verify.is_only_number_str(TestVerify.STR_NUMBER_TRUE) is True
    assert Verify.is_only_number_str(TestVerify.STR_NUMBER_FALSE) is False
