import pytest
from . import Keys, TestTxBuilder, builder_p2wpkh, Addresses

from defichain import TxBuilder, Ocean
from defichain.exceptions.transactions import TxBuilderError
from defichain.exceptions.http import BadRequest


@pytest.mark.transactions
def test_create():  # 01
    assert TxBuilder(address=Keys.account.get_p2wpkh(), account=Keys.account, dataSource=Ocean(), feePerByte=1.0)
    with pytest.raises(TxBuilderError, match="The given address does not match the given account!"):
        assert TxBuilder(address=Keys.account.get_p2wpkh(), account=Keys.wallet.get_account(10),
                         dataSource=Ocean(), feePerByte=1.0)


@pytest.mark.transactions
def test_send_tx():  # 02
    with pytest.raises(BadRequest):
        assert builder_p2wpkh.send_tx(TestTxBuilder.tx_serialized)
    with pytest.raises(BadRequest):
        assert builder_p2wpkh.send_tx(TestTxBuilder.tx)


@pytest.mark.transactions
def test_test_tx():  # 03
    assert builder_p2wpkh.test_tx(TestTxBuilder.tx_serialized)
    assert builder_p2wpkh.test_tx(TestTxBuilder.tx)


@pytest.mark.transactions
def test_get_inputs_tx():  # 04
    assert builder_p2wpkh.get_inputs_tx().serialize() == TestTxBuilder.inputs_tx_serialized


@pytest.mark.transactions
def test_get_address():  # 05
    assert builder_p2wpkh.get_address() == Addresses.P2WPKH


@pytest.mark.transactions
def test_get_account():  # 06
    assert builder_p2wpkh.get_account() == Keys.account


@pytest.mark.transactions
def test_get_dataSource():  # 07
    assert builder_p2wpkh.get_dataSource()


@pytest.mark.transactions
def test_get_feePerByte():  # 08
    assert builder_p2wpkh.get_feePerByte() == 1

