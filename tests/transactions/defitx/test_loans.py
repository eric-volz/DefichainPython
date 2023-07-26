import pytest

from defichain.networks import DefichainMainnet
from defichain.transactions.defitx import DefiTx, TakeLoan, PaybackLoan
from . import Addresses, TestLoans


@pytest.mark.transactions
def test_takeloan():  # 01
    takeloan_p2pkh: TakeLoan = TakeLoan(vaultId=TestLoans.vaultId, addressTo=Addresses.P2PKH, amounts=TestLoans.amounts)
    takeloan_p2sh: TakeLoan = TakeLoan(vaultId=TestLoans.vaultId, addressTo=Addresses.P2SH, amounts=TestLoans.amounts)
    takeloan_p2wpkh: TakeLoan = TakeLoan(vaultId=TestLoans.vaultId, addressTo=Addresses.P2WPKH,
                                         amounts=TestLoans.amounts)

    assert takeloan_p2pkh.serialize() == TestLoans.takeloan_p2pkh_serialized
    assert takeloan_p2sh.serialize() == TestLoans.takeloan_p2sh_serialized
    assert takeloan_p2wpkh.serialize() == TestLoans.takeloan_p2wpkh_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestLoans.takeloan_p2pkh_serialized).serialize() == \
           TestLoans.takeloan_p2pkh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestLoans.takeloan_p2sh_serialized).serialize() == \
           TestLoans.takeloan_p2sh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestLoans.takeloan_p2wpkh_serialized).serialize() == \
           TestLoans.takeloan_p2wpkh_serialized


@pytest.mark.transactions
def test_paybackloan():  # 02
    paybackloan_p2pkh: PaybackLoan = PaybackLoan(vaultId=TestLoans.vaultId, addressFrom=Addresses.P2PKH,
                                                 amounts=TestLoans.amounts)
    paybackloan_p2sh: PaybackLoan = PaybackLoan(vaultId=TestLoans.vaultId, addressFrom=Addresses.P2SH,
                                                amounts=TestLoans.amounts)
    paybackloan_p2wpkh: PaybackLoan = PaybackLoan(vaultId=TestLoans.vaultId, addressFrom=Addresses.P2WPKH,
                                                  amounts=TestLoans.amounts)

    assert paybackloan_p2pkh.serialize() == TestLoans.paybackloan_p2pkh_serialized
    assert paybackloan_p2sh.serialize() == TestLoans.paybackloan_p2sh_serialized
    assert paybackloan_p2wpkh.serialize() == TestLoans.paybackloan_p2wpkh_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestLoans.paybackloan_p2pkh_serialized).serialize() == \
           TestLoans.paybackloan_p2pkh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestLoans.paybackloan_p2sh_serialized).serialize() == \
           TestLoans.paybackloan_p2sh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestLoans.paybackloan_p2wpkh_serialized).serialize() == \
           TestLoans.paybackloan_p2wpkh_serialized
