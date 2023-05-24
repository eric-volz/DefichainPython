import pytest

from . import MainNet, TestNet
from defichain.transactions.address import Address, P2PKH, P2SH, P2WPKH
from defichain.transactions.constants import AddressTypes

network = (MainNet, TestNet)


@pytest.mark.transactions
def test_get_addressType():  # 01
    for n in network:
        assert Address.get_addressType(n.P2PKH) == (n.NETWORK, AddressTypes.P2PKH)
        assert Address.get_addressType(n.P2SH) == (n.NETWORK, AddressTypes.P2SH)
        assert Address.get_addressType(n.P2WPKH) == (n.NETWORK, AddressTypes.P2WPKH)


@pytest.mark.transactions
def test_from_address():  # 02
    for n in network:
        assert isinstance(Address.from_address(n.P2PKH), P2PKH)
        assert isinstance(Address.from_address(n.P2SH), P2SH)
        assert isinstance(Address.from_address(n.P2WPKH), P2WPKH)


@pytest.mark.transactions
def test_from_scriptPublicKey():  # 03
    for n in network:
        assert Address.from_scriptPublicKey(n.NETWORK, n.P2PKH_SCRIPTPUBLICKEY).get_address() == n.P2PKH
        assert Address.from_scriptPublicKey(n.NETWORK, n.P2SH_SCRIPTPUBLICKEY).get_address() == n.P2SH
        assert Address.from_scriptPublicKey(n.NETWORK, n.P2WPKH_SCRIPTPUBLICKEY).get_address() == n.P2WPKH


@pytest.mark.transactions
def test_verify_address():  # 04
    for n in network:
        assert Address.verify_address(n.P2PKH)
        assert Address.verify_address(n.P2SH)
        assert Address.verify_address(n.P2WPKH)
