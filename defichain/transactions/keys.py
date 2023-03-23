from abc import ABC, abstractmethod
from typing import Any

from defichain.exceptions.transactions import KeyError
from defichain import Wallet
from defichain.transactions.utils import Converter


# TODO: Documentation


class Key(ABC):

    @staticmethod
    def is_publicKey(network: Any, publicKey: str) -> bool:
        try:
            Wallet(network).from_public_key(publicKey)
            return True
        except:
            return False

    @staticmethod
    def is_privateKey(network: Any, privateKey: str) -> bool:
        try:
            Wallet(network).from_private_key(privateKey)
            return True
        except:
            return False

    @staticmethod
    def is_wif(network: Any, wif: str) -> bool:
        try:
            Wallet(network).from_wif(wif)
            return True
        except:
            return False

    @staticmethod
    @abstractmethod
    def verify(network: Any, key: str) -> bool:
        pass

    def __init__(self, network: Any, publicKey: str):
        self._network = None
        self._account: Wallet = None
        self.set_network(network)
        self.set_publicKey(publicKey)

    @abstractmethod
    def __bytes__(self) -> bytes:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def bytes(self) -> bytes:
        return bytes(self)

    def p2sh_address(self) -> str:
        return self._account.default_address()

    def p2pkh_address(self) -> str:
        return self._account.legacy_address()

    def p2wpkh_address(self) -> str:
        return self._account.bech32_address()

    # Get Information

    def get_publicKey(self) -> str:
        return self._account.public_key()

    def get_network(self):
        return self._network

    # Set Information

    def set_publicKey(self, publicKey: str) -> None:
        if not publicKey == "":
            PublicKey.verify(self.get_network(), publicKey)
            self._account.from_public_key(publicKey)

    def set_network(self, network: Any) -> None:
        self._network = network
        self._account = Wallet(network)


class PublicKey(Key):

    @staticmethod
    def from_privateKey(network: Any, privateKey: str) -> "PublicKey":
        if PublicKey.is_privateKey(network, privateKey):
            account = Wallet(network).from_private_key(privateKey)
            return PublicKey(network, account.public_key())
        else:
            raise KeyError("The given private key is not valid")

    @staticmethod
    def from_wif(network: Any, wif: str) -> "PublicKey":
        if PublicKey.is_wif(network, wif):
            account = Wallet(network).from_wif(wif)
            return PublicKey(network, account.public_key())
        else:
            raise KeyError("The given wif is not valid")

    @staticmethod
    def verify(network: Any, publicKey: str) -> bool:
        if not PublicKey.is_publicKey(network, publicKey):
            raise KeyError("The given public key is not valid")
        return True

    def __init__(self, network: Any, publicKey: str):
        if not PublicKey.verify(network, publicKey):
            raise KeyError("The given public key is not valid")
        super().__init__(network, publicKey)

    def __bytes__(self) -> bytes:
        return Converter.hex_to_bytes(self.get_publicKey())

    def __str__(self) -> str:
        return self.get_publicKey()


class PrivateKey(Key):

    @staticmethod
    def verify(network: Any, key: str) -> bool:
        if not (PrivateKey.is_privateKey(network, key) or PrivateKey.is_wif(network, key)):
            raise KeyError("The given private key or wif is not a valid private key")
        return True

    def __init__(self, network: Any, privateKey: str = "",
                 wif: str = ""):
        super().__init__(network, "")

        if privateKey != "" and wif != "":
            raise KeyError("Only one input is allowed: privateKey or wif")
        elif privateKey != "" and wif == "":
            self.set_privateKey(privateKey)
        elif privateKey == "" and wif != "":
            self.set_wif(wif)
        else:
            raise KeyError("You have to provide at least of one input: privateKey or wif")

    def __bytes__(self) -> bytes:
        return Converter.hex_to_bytes(self.get_privateKey())

    def __str__(self) -> str:
        return self.get_privateKey()

    # Get Information
    def get_privateKey(self) -> str:
        return self._account.private_key()

    def get_wif(self) -> str:
        return self._account.wif()

    # Set information
    def set_privateKey(self, privateKey: str) -> None:
        self.verify(self.get_network(), privateKey)
        self._account.from_private_key(privateKey)

    def set_wif(self, wif: str) -> None:
        self.verify(self.get_network(), wif)
        self._account.from_wif(wif)
