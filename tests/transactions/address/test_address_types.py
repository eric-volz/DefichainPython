import pytest

from . import MainNet, TestNet
from defichain.transactions.address import P2PKH, P2SH, P2WPKH
from defichain.transactions.constants import AddressTypes

network = (MainNet, TestNet)


@pytest.mark.transactions
def test_from_publicKey():  # 01
    for n in network:
        assert P2PKH.from_publicKey(n.NETWORK, n.PUBLIC_KEY).get_address() == n.P2PKH
        assert P2SH.from_publicKey(n.NETWORK, n.PUBLIC_KEY).get_address() == n.P2SH
        assert P2WPKH.from_publicKey(n.NETWORK, n.PUBLIC_KEY).get_address() == n.P2WPKH


@pytest.mark.transactions
def test_from_privateKey():  # 02
    for n in network:
        assert P2PKH.from_privateKey(n.NETWORK, n.PRIVATE_KEY).get_address() == n.P2PKH
        assert P2SH.from_privateKey(n.NETWORK, n.PRIVATE_KEY).get_address() == n.P2SH
        assert P2WPKH.from_privateKey(n.NETWORK, n.PRIVATE_KEY).get_address() == n.P2WPKH


@pytest.mark.transactions
def test_from_scriptPublicKey():  # 03
    for n in network:
        assert P2PKH.from_scriptPublicKey(n.NETWORK, n.P2PKH_SCRIPTPUBLICKEY).get_address() == n.P2PKH
        assert P2SH.from_scriptPublicKey(n.NETWORK, n.P2SH_SCRIPTPUBLICKEY).get_address() == n.P2SH
        assert P2WPKH.from_scriptPublicKey(n.NETWORK, n.P2WPKH_SCRIPTPUBLICKEY).get_address() == n.P2WPKH


@pytest.mark.transactions
def test_from_publicKeyHash():  # 04
    for n in network:
        assert P2PKH.from_publicKeyHash(n.NETWORK, n.P2PKH_PUBLICKEYHASH).get_address() == n.P2PKH
        assert P2WPKH.from_publicKeyHash(n.NETWORK, n.P2WPKH_PUBLICKEYHASH).get_address() == n.P2WPKH


@pytest.mark.transactions
def test_get_addressType():  # 05
    for n in network:
        assert P2PKH(n.NETWORK, n.P2PKH).get_addressType() == AddressTypes.P2PKH
        assert P2SH(n.NETWORK, n.P2SH).get_addressType() == AddressTypes.P2SH
        assert P2WPKH(n.NETWORK, n.P2WPKH).get_addressType() == AddressTypes.P2WPKH


@pytest.mark.transactions
def test_get_redeemScript():  # 06
    for n in network:
        assert P2PKH(n.NETWORK, n.P2PKH).get_redeemScript() == n.P2PKH_REDEEMSCRIPT
        assert P2SH(n.NETWORK, n.P2SH).get_redeemScript() == n.P2SH_REDEEMSCRIPT
        assert P2WPKH(n.NETWORK, n.P2WPKH).get_redeemScript() == n.P2WPKH_REDEEMSCRIPT


@pytest.mark.transactions
def test_get_publicKeyHash():  # 07
    for n in network:
        assert P2PKH(n.NETWORK, n.P2PKH).get_publicKeyHash() == n.P2PKH_PUBLICKEYHASH
        assert P2WPKH(n.NETWORK, n.P2WPKH).get_publicKeyHash() == n.P2WPKH_PUBLICKEYHASH


@pytest.mark.transactions
def test_decode():  # 08
    for n in network:
        assert P2PKH.decode(n.P2PKH) == n.P2PKH_DECODE
        assert P2SH.decode(n.P2SH) == n.P2SH_DECODE
        assert P2WPKH.decode(n.P2WPKH) == n.P2WPKH_DECODE


@pytest.mark.transactions
def test_encode():  # 09
    for n in network:
        assert P2PKH.encode(n.NETWORK, n.P2PKH_DECODE) == n.P2PKH
        assert P2SH.encode(n.NETWORK, n.P2SH_DECODE) == n.P2SH
        assert P2WPKH.encode(n.NETWORK, n.P2WPKH_DECODE) == n.P2WPKH


@pytest.mark.transactions
def test_scriptPublicKey_to_address():  # 10
    for n in network:
        assert P2PKH.scriptPublicKey_to_address(n.NETWORK, n.P2PKH_SCRIPTPUBLICKEY) == n.P2PKH
        assert P2SH.scriptPublicKey_to_address(n.NETWORK, n.P2SH_SCRIPTPUBLICKEY) == n.P2SH
        assert P2WPKH.scriptPublicKey_to_address(n.NETWORK, n.P2WPKH_SCRIPTPUBLICKEY) == n.P2WPKH
