from defichain.exceptions.transactions import AddressError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from defichain.transactions.constants import POSSIBLE_ADDRESS_TYPES

from .baseaddress import BaseAddress
from .p2pkh import P2PKH
from .p2sh import P2SH
from .p2wpkh import P2WPKH
from .p2wsh import P2WSH


class Address:

    @staticmethod
    def get_address_type(address: str) -> (str, DefichainMainnet or DefichainTestnet or DefichainRegtest) or None:
        # TODO: check for more address types

        # mainnet
        if address[0] == "8":
            return POSSIBLE_ADDRESS_TYPES[0], DefichainMainnet
        elif address[:2] == DefichainMainnet.SEGWIT_ADDRESS.HRP:
            return POSSIBLE_ADDRESS_TYPES[2], DefichainMainnet

        # testnet
        if address[0] == "7":
            return POSSIBLE_ADDRESS_TYPES[0], DefichainTestnet
        elif address[:2] == DefichainTestnet.SEGWIT_ADDRESS.HRP:
            return POSSIBLE_ADDRESS_TYPES[2], DefichainTestnet

        # regtest
        if address[0] == "m":
            return POSSIBLE_ADDRESS_TYPES[0], DefichainRegtest
        elif address[:4] == DefichainRegtest.SEGWIT_ADDRESS.HRP:
            return POSSIBLE_ADDRESS_TYPES[2], DefichainRegtest
        return None

    @staticmethod
    def from_address(address: str) -> "BaseAddress":
        # TODO: Make these methods more advanced
        type, network = Address.get_address_type(address)
        if type == POSSIBLE_ADDRESS_TYPES[0]:  # Legacy
            return P2PKH(network, address)
        elif type == POSSIBLE_ADDRESS_TYPES[1]:  # Pay to Script Hash
            return P2SH(network, address)
        elif type == POSSIBLE_ADDRESS_TYPES[2]:  # Native Segwit
            return P2WPKH(network, address)
        elif type == POSSIBLE_ADDRESS_TYPES[3]:
            return P2WSH(network, address)
        else:
            raise AddressError("This address ist not supported")
