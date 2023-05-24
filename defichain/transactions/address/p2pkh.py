from typing import Any

import hashlib
import binascii

from defichain.exceptions.transactions import AddressError
from defichain.networks import Network
from defichain.transactions.constants import AddressTypes, OPCodes
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.libs import base58
from .base58address import Base58Address
from .script import Script


class P2PKH(Base58Address):  # Legacy

    @staticmethod
    def from_publicKey(network: Any, publicKey: str) -> "P2PKH":
        """
        Generates a P2PKH address object from the given public key

        :param network: (required) The network in witch the public key should be used
        :type network: Network
        :param publicKey: (required) public key
        :type publicKey: str
        :return: P2PKH - returns the P2PKH address object
        """
        return P2PKH(network, PublicKey(network, publicKey).p2pkh_address())

    @staticmethod
    def from_privateKey(network: Any, privateKey: str) -> "P2PKH":
        """
        Generates a P2PKH address object from the given private key

        :param network: (required) The network in witch the private key should be used
        :type network: Network
        :param privateKey: (required) private key
        :type privateKey: str
        :return: P2PKH - returns the P2PKH address object
        """
        return P2PKH(network, PrivateKey(network, privateKey).p2pkh_address())

    @staticmethod
    def from_scriptPublicKey(network: Any, scriptPublicKey: str) -> "P2PKH":
        """
        Generates a P2PKH address object from the given script private key

        :param network: (required) The network in witch the script public key should be used
        :type network: Network
        :param scriptPublicKey: (required) script public key
        :type scriptPublicKey: str
        :return: P2PKH - returns the P2PKH address object
        """
        return P2PKH(network, Base58Address.scriptPublicKey_to_address(network, scriptPublicKey))

    @staticmethod
    def from_publicKeyHash(network: Any, publicKeyHash: str) -> "P2PKH":
        if network.NETWORK == "mainnet":
            checksumHash = "12" + publicKeyHash
        elif network.NETWORK == "testnet":
            checksumHash = "0f" + publicKeyHash
        else:
            raise AddressError("The specified network is not supported")
        for _ in range(2):
            checksumHash = hashlib.sha256(binascii.unhexlify(checksumHash)).hexdigest()
        checksum = checksumHash[:8]
        if network.NETWORK == "mainnet":
            hash = "12" + publicKeyHash + checksum
        elif network.NETWORK == "testnet":
            hash = "0f" + publicKeyHash + checksum
        else:
            raise AddressError("The specified network is not supported")
        address = base58.encode(bytes.fromhex(hash))
        return P2PKH(network, address)

    def __init__(self, network: Any, address: str):
        super().__init__(network, address)

    def get_addressType(self) -> str:
        return AddressTypes.P2PKH

    def get_scriptPublicKey(self) -> str:
        return Script.build_script([OPCodes.OP_DUP, OPCodes.OP_HASH160, Base58Address.decode(self.get_address())[2:42],
                                    OPCodes.OP_EQUALVERIFY, OPCodes.OP_CHECKSIG])

    def get_redeemScript(self) -> str:
        return self.get_scriptPublicKey()

    def get_publicKeyHash(self) -> str:
        return Base58Address.decode(self.get_address())[2:42]

    def get_bytes_scriptPublicKey(self) -> bytes:
        return bytes.fromhex(self.get_scriptPublicKey())

    def get_bytes_redeemScript(self) -> bytes:
        return bytes.fromhex(self.get_redeemScript())

    def get_bytes_publicKeyHash(self) -> bytes:
        return bytes.fromhex(Base58Address.decode(self.get_address())[2:42])


