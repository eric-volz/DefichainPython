import pytest

from . import TestToken
from defichain.networks import DefichainMainnet, DefichainTestnet
from defichain.transactions.utils import Token


@pytest.mark.transactions
def test_get_symbol_from_id():  # 01
    # Mainnet
    for id in TestToken.MAINNET_IDs:
        assert Token.get_symbol_from_id(DefichainMainnet, id) in TestToken.MAINNET_SYMBOLS

    # Testnet
    for id in TestToken.TESTNET_IDs:
        assert Token.get_symbol_from_id(DefichainTestnet, id) in TestToken.TESTNET_SYMBOLS


@pytest.mark.transactions
def test_get_id_from_symbol():  # 02
    # Mainnet
    for symbol in TestToken.MAINNET_SYMBOLS:
        assert Token.get_id_from_symbol(DefichainMainnet, symbol) in TestToken.MAINNET_IDs

    # Testnet
    for symbol in TestToken.TESTNET_SYMBOLS:
        assert Token.get_id_from_symbol(DefichainTestnet, symbol) in TestToken.TESTNET_IDs


@pytest.mark.transactions
def test_get_name_from_id():  # 03
    # Mainnet
    for id in TestToken.MAINNET_IDs:
        Token.get_name_from_id(DefichainMainnet, id)

    # Testnet
    for id in TestToken.TESTNET_IDs:
        Token.get_name_from_id(DefichainTestnet, id)


@pytest.mark.transactions
def test_verify_tokenId():  # 04
    # Mainnet
    for id in TestToken.MAINNET_IDs:
        Token.verify_tokenId(DefichainMainnet, id)

    # Testnet
    for id in TestToken.TESTNET_IDs:
        Token.verify_tokenId(DefichainTestnet, id)


@pytest.mark.transactions
def test_checkAndConvert():  # 05
    # Mainnet
    # Test ID
    for id in TestToken.MAINNET_IDs:
        assert Token.checkAndConvert(DefichainMainnet, id) in TestToken.MAINNET_IDs

    # Test Symbol
    for symbol in TestToken.MAINNET_SYMBOLS:
        assert Token.checkAndConvert(DefichainMainnet, symbol) in TestToken.MAINNET_IDs

    # Testnet
    # Test ID
    for id in TestToken.TESTNET_IDs:
        assert Token.checkAndConvert(DefichainTestnet, id) in TestToken.TESTNET_IDs

    # Test Symbol
    for symbol in TestToken.TESTNET_SYMBOLS:
        assert Token.checkAndConvert(DefichainTestnet, symbol) in TestToken.TESTNET_IDs
