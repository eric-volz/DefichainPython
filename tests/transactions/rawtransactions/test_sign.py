import pytest

from defichain.transactions.rawtransactions.sign import sign_legacy_input, sign_segwit_input
from . import Keys, TestSign


@pytest.mark.transactions
def test_sign_legacy_input():  # 01
    assert sign_legacy_input(Keys.privateKey, TestSign.DataBytes, TestSign.SigHashBytes) == TestSign.LegacySignature


@pytest.mark.transactions
def test_sign_segwit_input():  # 02
    assert sign_segwit_input(Keys.privateKey, TestSign.DataBytes) == TestSign.SegwitSignature
