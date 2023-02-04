from abc import ABC
import binascii

from defichain.exceptions.transactions import AddressError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .baseaddress import BaseAddress
from defichain.transactions.constants import CHARSET, CHARSET_BASE
from defichain.libs import bech32


class Bech32Address(BaseAddress, ABC):
    @staticmethod
    def _is_bech32address(address: str) -> bool:
        bech32decode = bech32.bech32_decode(address)
        if not bech32decode[0]:
            raise AddressError(f"The given address: {address} is not a valid bech32 address")
        return True

    @staticmethod
    def _is_scriptPublicKey(scriptPublicKey: str) -> bool:
        if not (scriptPublicKey[0:4] == "0014" and len(scriptPublicKey) == 44):
            raise AddressError(f"The given script public key: {scriptPublicKey} is not valid")
        return True

    @staticmethod
    def decode(address: str) -> str:
        data = reversed(address[4:-6])
        return '%x' % sum([CHARSET.find(c) * CHARSET_BASE ** i for i, c in enumerate(data)])

    @staticmethod
    def encode(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, scriptPublicKey: str) -> str:
        binary = binascii.unhexlify(scriptPublicKey)
        version = binary[0] - 0x50 if binary[0] else 0
        program = binary[2:]
        return bech32.encode(network.SEGWIT_ADDRESS.HRP, version, program)

    @staticmethod
    def scriptPublicKey_to_address(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                                   scriptPublicKey: str) -> str:
        if scriptPublicKey[0:4] == "0014":
            return Bech32Address.encode(network, scriptPublicKey)

    @staticmethod
    def verify(address: str) -> bool:
        return Bech32Address._is_bech32address(address)

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network)
        self._address = None
        self.set_address(address)

    # Get Information
    def get_address(self) -> str:
        return self._address

    # Set Information
    def set_address(self, address: str) -> None:
        self.verify(address)
        self._address = address

    def set_scriptPublicKey(self, scriptPublicKey: str) -> None:
        self._is_scriptPublicKey(scriptPublicKey)
        self.set_address(self.scriptPublicKey_to_address(self.get_network(), scriptPublicKey))
