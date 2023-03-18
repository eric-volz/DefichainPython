from typing import Any
from defichain.exceptions.transactions import AddressError
from defichain.libs import bech32
from defichain.networks import Network, DefichainMainnet, DefichainTestnet
from defichain.transactions.constants import AddressTypes
from defichain.transactions.utils import Converter

from .baseaddress import BaseAddress
from .base58address import Base58Address
from .bech32address import Bech32Address
from .p2pkh import P2PKH
from .p2sh import P2SH
from .p2wpkh import P2WPKH


class Address:

    @staticmethod
    def get_addressType(address: str) -> (Network, str):
        """
        Analyses the given address and returns the network and the address type

        :param address: (required) address
        :return: (Network, AddressType)
        """
        # Base58
        _base58 = False
        _bech32 = False
        prefix = ""
        try:
            _base58 = Base58Address.verify(address)
            if _base58:
                prefix = Base58Address.decode(address)[0:2]
        except:
            pass

        if _base58:
            for network in [DefichainMainnet, DefichainTestnet]:
                if Converter.int_to_hex(network.PUBLIC_KEY_ADDRESS, 1) == prefix:
                    return network, AddressTypes.P2PKH
                elif Converter.int_to_hex(network.SCRIPT_ADDRESS, 1) == prefix:
                    return network, AddressTypes.P2SH

        # Bech32
        try:
            _bech32 = Bech32Address.verify(address)
            if _bech32:
                prefix = bech32.bech32_decode(address)[0]
        except:
            pass

        if _bech32:
            for network in [DefichainMainnet, DefichainTestnet]:
                if prefix == network.SEGWIT_ADDRESS.HRP:
                    return network, AddressTypes.P2WPKH
        raise AddressError("This address ist not supported")

    @staticmethod
    def from_address(address: str) -> "BaseAddress":
        """
        Creates the matching address object for the given address

        :param address: (requires) address
        :return: BaseAddress - returns one of these objects: P2PKH, P2SH, P2WPKH
        """
        network, addressType = Address.get_addressType(address)

        if addressType == AddressTypes.P2PKH:  # Legacy
            return P2PKH(network, address)
        elif addressType == AddressTypes.P2SH:  # Pay to Script Hash
            return P2SH(network, address)
        elif addressType == AddressTypes.P2WPKH:  # Native Segwit
            return P2WPKH(network, address)
        else:
            raise AddressError("This address ist not supported")

    @staticmethod
    def from_scriptPublicKey(network: Any, scriptPublicKey: str) -> "BaseAddress":
        """
        Creates the matching address object for the given script public key.

        Important: The script public key is universal.
        The correct network has to be specified to get the wanted address.

        :param network: (required) Network
        :param scriptPublicKey: (required) script public key
        :return: BaseAddress - returns one of these objects: P2PKH, P2SH, P2WPKH
        """
        # Base58
        try:
            return Address.from_address(Base58Address.scriptPublicKey_to_address(network, scriptPublicKey))
        except:
            pass

        # Bech32
        try:
            return Address.from_address(Bech32Address.scriptPublicKey_to_address(network, scriptPublicKey))
        except:
            pass

        raise AddressError("This script public key is not supported. Could be a multi signature transaction, witch is "
                           "currently not supported")

    @staticmethod
    def verify_address(address: str) -> bool:
        """
        Verifies if the given address is valid.

        Raises exception (AddressError) if address is not valid.

        :param address: (requires) address
        :return: bool - returns True if address is valid
        """
        Address.from_address(address)
        return True
