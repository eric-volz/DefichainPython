from abc import ABC

from defichain.exceptions.transactions import AddressError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .baseaddress import BaseAddress

from defichain.libs import base58
import binascii
import hashlib


class Base58Address(BaseAddress, ABC):

    @staticmethod
    def _is_base58address(address: str) -> bool:
        base58decode = base58.decode(address).hex()
        hash = base58decode[:len(base58decode) - 8]
        checksum = base58decode[len(base58decode) - 8:]
        for x in range(1, 3):
            hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
        if checksum == hash[:8]:
            return True
        else:
            raise AddressError(f"The given address: {address} is not a valid base58 address")

    @staticmethod
    def decode(address: str) -> str:
        return base58.decode(address).hex()

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network)
        self._address = None
        self.set_address(address)

    def verify(self, address: str) -> bool:
        return self._is_base58address(address)

    # Get Information
    def get_address(self) -> str:
        return self._address

    # Set Information
    def set_address(self, address: str) -> None:
        self.verify(address)
        self._address = address
