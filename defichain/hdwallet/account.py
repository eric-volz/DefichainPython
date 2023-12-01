from .dvm_wallet import DVMWallet
from typing import Any
from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest


class Account:

    @staticmethod
    def _is_publicKey(network: Any, publicKey: str) -> bool:
        try:
            DVMWallet(network).from_public_key(publicKey)
            return True
        except:
            return False

    @staticmethod
    def _is_privateKey(network: Any, privateKey: str) -> bool:
        try:
            DVMWallet(network).from_private_key(privateKey)
            return True
        except:
            return False

    @staticmethod
    def _is_wif(network: Any, wif: str) -> bool:
        try:
            DVMWallet(network).from_wif(wif)
            return True
        except:
            return False

    def __init__(self, network: Any, key: str):
        self._network = None
        self._wallet: DVMWallet = DVMWallet(network)
        self.set_network(network)
        self.set_key(key)

    # Get information
    def get_network(self):
        return self._network

    def get_publicKey(self):
        return self._wallet.public_key()

    def get_privateKey(self):
        return self._wallet.private_key()

    def get_wif(self):
        return self._wallet.wif()

    def get_p2sh(self):
        return self._wallet.p2sh_address()

    def get_p2pkh(self):
        return self._wallet.p2pkh_address()

    def get_p2wpkh(self):
        return self._wallet.p2wpkh_address()

    def is_private(self):
        return self._is_privateKey(self.get_network(), self._wallet.private_key())

    # Set Information
    def set_network(self, network: "DefichainMainnet | DefichainTestnet") -> None:
        self._network = network

    def set_key(self, key: str):
        if self._is_publicKey(self.get_network(), key):
            self._wallet.from_public_key(key)
        elif self._is_privateKey(self.get_network(), key):
            self._wallet.from_private_key(key)
        elif self._is_wif(self.get_network(), key):
            self._wallet.from_wif(key)
