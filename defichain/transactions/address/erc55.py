from typing import Any

from web3 import Web3
from eth_keys import keys

from .baseaddress import BaseAddress
from .script import Script
from defichain.transactions.utils import Converter
from defichain.transactions.constants import AddressTypes, OPCodes


class ERC55:
    @staticmethod
    def from_publicKey(publicKey: str) -> "ERC55":
        address = keys.PublicKey(Converter.hex_to_bytes(publicKey)).to_address()
        return ERC55(address)

    @staticmethod
    def from_privateKey(privateKey: str) -> "ERC55":
        address = keys.PrivateKey(Converter.hex_to_bytes(privateKey)).to_address()
        return ERC55(address)

    @staticmethod
    def from_scriptPublicKey(scriptPublicKey: str) -> "ERC55":
        address = "0x" + bytes(reversed(bytes().fromhex(scriptPublicKey[4:]))).hex()
        return ERC55(address)

    @staticmethod
    def verify(address: str) -> bool:
        return Web3.is_address(address)

    def __init__(self, address: str):
        self._address = None
        self.set_address(address)

    def get_addressType(self) -> str:
        return AddressTypes.ERC55

    def get_address(self) -> str:
        return self._address

    def get_scriptPublicKey(self) -> str:
        return Script.build_script([OPCodes.OP_16, bytes(reversed(bytes().fromhex(self.get_address()[2:]))).hex()])

    def get_bytes_scriptPublicKey(self) -> bytes:
        return bytes.fromhex(self.get_scriptPublicKey())


    def set_address(self, address: str) -> None:
        self._address = address

    def set_scriptPublicKey(self, scriptPublicKey: str) -> None:
        self._address = "0x" + bytes(reversed(bytes().fromhex(scriptPublicKey[4:]))).hex()

