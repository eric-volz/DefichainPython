from abc import ABC, abstractmethod

from defichain.exceptions.transactions import KeyError

from defichain import Wallet
from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from defichain.transactions.utils import *


# TODO: Documentation


class Key(ABC):

    @staticmethod
    def is_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str) -> bool:
        try:
            Wallet(network).from_public_key(public_key)
            return True
        except:
            return False

    @staticmethod
    def is_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, private_key: str) -> bool:
        try:
            Wallet(network).from_private_key(private_key)
            return True
        except:
            return False

    @staticmethod
    def is_wif(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, wif: str) -> bool:
        try:
            Wallet(network).from_wif(wif)
            return True
        except:
            return False

    @staticmethod
    @abstractmethod
    def verify(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, key: str) -> bool:
        pass

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str):
        self._network = None
        self._account: Wallet = None
        self.set_network(network)
        self.set_public_key(public_key)

    @abstractmethod
    def __bytes__(self) -> bytes:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def bytes(self) -> bytes:
        return bytes(self)

    def default_address(self) -> str:
        return self._account.default_address()

    def legacy_address(self) -> str:
        return self._account.legacy_address()

    def bech32_address(self) -> str:
        return self._account.bech32_address()

    # Get Information

    def get_public_key(self) -> str:
        return self._account.public_key()

    def get_network(self):
        return self._network

    # Set Information

    def set_public_key(self, public_key: str) -> None:
        if not public_key == "":
            PublicKey.verify(self.get_network(), public_key)
            self._account.from_public_key(public_key)

    def set_network(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest) -> None:
        self._network = network
        self._account = Wallet(network)


class PublicKey(Key):

    @staticmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "PublicKey":
        if PublicKey.is_private_key(network, private_key):
            account = Wallet(network).from_private_key(private_key)
            return PublicKey(network, account.public_key())
        else:
            raise KeyError("The given private key is not valid")

    @staticmethod
    def from_wif(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, wif: str) -> "PublicKey":
        if PublicKey.is_wif(network, wif):
            account = Wallet(network).from_wif(wif)
            return PublicKey(network, account.public_key())
        else:
            raise KeyError("The given wif is not valid")

    @staticmethod
    def verify(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str) -> bool:
        if not PublicKey.is_public_key(network, public_key):
            raise KeyError("The given public key is not valid")
        return True

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str):
        if not PublicKey.verify(network, public_key):
            raise KeyError("The given public key is not valid")
        super().__init__(network, public_key)

    def __bytes__(self) -> bytes:
        return hex_to_bytes(self.get_public_key())

    def __str__(self) -> str:
        return self.get_public_key()


class PrivateKey(Key):

    @staticmethod
    def verify(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, key: str) -> bool:
        if not (PrivateKey.is_private_key(network, key) or PrivateKey.is_wif(network, key)):
            raise KeyError("The given private key or wif is not a valid private key")
        return True

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, private_key: str = "",
                 wif: str = ""):
        super().__init__(network, "")

        if private_key != "" and wif != "":
            raise KeyError("Only one input is allowed: private_key or wif")
        elif private_key != "" and wif == "":
            self.set_private_key(private_key)
        elif private_key == "" and wif != "":
            self.set_wif(wif)
        else:
            raise KeyError("You have to provide at least of one input: private_key or wif")

    def __bytes__(self) -> bytes:
        return hex_to_bytes(self.get_private_key())

    def __str__(self) -> str:
        return self.get_private_key()

    # Get Information
    def get_private_key(self) -> str:
        return self._account.private_key()

    def get_wif(self) -> str:
        return self._account.wif()

    # Set information
    def set_private_key(self, private_key: str) -> None:
        self.verify(self.get_network(), private_key)
        self._account.from_private_key(private_key)

    def set_wif(self, wif: str) -> None:
        self.verify(self.get_network(), wif)
        self._account.from_wif(wif)
