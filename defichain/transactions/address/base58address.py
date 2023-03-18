from abc import ABC
from typing import Any
import binascii
import hashlib

from defichain.exceptions.transactions import AddressError
from defichain.libs import base58
from defichain.transactions.utils import Converter
from .baseaddress import BaseAddress


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
    def _is_scriptPublicKey(scriptPublicKey: str) -> bool:
        if not ((scriptPublicKey[0:6] == "76a914" and len(scriptPublicKey) == 50) or
                (scriptPublicKey[0:4] == "a914" and len(scriptPublicKey) == 46)):
            raise AddressError(f"The given script public key: {scriptPublicKey} is not valid")
        return True

    @staticmethod
    def decode(address: str) -> str:
        return base58.decode(address).hex()

    @staticmethod
    def encode(network: Any, scriptPublicKey: str) -> str:
        return base58.check_encode(Converter.hex_to_bytes(scriptPublicKey))

    @staticmethod
    def scriptPublicKey_to_address(network: Any,
                                   scriptPublicKey: str) -> str:
        Base58Address._is_scriptPublicKey(scriptPublicKey)
        if scriptPublicKey[0:6] == "76a914":  # P2PKH
            script = Converter.int_to_hex(network.PUBLIC_KEY_ADDRESS, 1) + scriptPublicKey[6:46]
            return Base58Address.encode(network, script)
        elif scriptPublicKey[0:4] == "a914":  # P2SH
            script = Converter.int_to_hex(network.SCRIPT_ADDRESS, 1) + scriptPublicKey[4:44]
            return Base58Address.encode(network, script)

    @staticmethod
    def verify(address: str) -> bool:
        return Base58Address._is_base58address(address)

    def __init__(self, network: Any, address: str):
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
