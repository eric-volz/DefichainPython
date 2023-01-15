from defichain.exceptions.transactions import AddressError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from defichain.transactions.constants import AddressTypes

from .baseaddress import BaseAddress
from .p2pkh import P2PKH
from .p2sh import P2SH
from .p2wpkh import P2WPKH


class Address:

    @staticmethod
    def get_address_type(address: str) -> (str, DefichainMainnet or DefichainTestnet or DefichainRegtest) or None:
        # TODO: check for more address types

        # mainnet
        if address[0] == "8":
            return AddressTypes.P2PKH, DefichainMainnet
        elif address[:2] == DefichainMainnet.SEGWIT_ADDRESS.HRP:
            return AddressTypes.P2WPKH, DefichainMainnet
        elif address[0] == "d":
            return AddressTypes.P2SH, DefichainMainnet


        # testnet
        if address[0] == "7":
            return AddressTypes.P2PKH, DefichainTestnet
        elif address[:2] == DefichainTestnet.SEGWIT_ADDRESS.HRP:
            return AddressTypes.P2WPKH, DefichainTestnet
        elif address[0] == "t":
            return AddressTypes.P2SH, DefichainTestnet

        # regtest
        if address[0] == "m":
            return AddressTypes.P2PKH, DefichainRegtest
        elif address[0] == "2":
            return AddressTypes.P2SH, DefichainRegtest
        elif address[:4] == DefichainRegtest.SEGWIT_ADDRESS.HRP:
            return AddressTypes.P2WPKH, DefichainRegtest
        raise AddressError(f"Given Address: {address} is not valid")

    @staticmethod
    def from_address(address: str) -> "BaseAddress":
        # TODO: Make these methods more advanced
        type, network = Address.get_address_type(address)
        if type == AddressTypes.P2PKH:  # Legacy
            return P2PKH(network, address)
        elif type == AddressTypes.P2SH:  # Pay to Script Hash
            return P2SH(network, address)
        elif type == AddressTypes.P2WPKH:  # Native Segwit
            return P2WPKH(network, address)
        else:
            raise AddressError("This address ist not supported")
