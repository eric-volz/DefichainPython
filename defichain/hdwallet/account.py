from .wallet import Wallet
from typing import Any


class Account:

    @staticmethod
    def _is_publicKey(network: Any, publicKey: str) -> bool:
        try:
            Wallet(network).from_public_key(publicKey)
            return True
        except:
            return False

    @staticmethod
    def _is_privateKey(network: Any, privateKey: str) -> bool:
        try:
            Wallet(network).from_private_key(privateKey)
            return True
        except:
            return False

    @staticmethod
    def _is_wif(network: Any, wif: str) -> bool:
        try:
            Wallet(network).from_wif(wif)
            return True
        except:
            return False

    def __init__(self, network: Any, key: str):
        """
        An account is a representation of one private / public key.

        :param network: (required) network instance: DefichainMainnet, DefichainTestnet
        :type network: network
        :param key: (required) standard private key or wif
        :type key: str

        :returns: Account -- Account instance
        """
        self._network = None
        self._wallet: Wallet = Wallet(network)
        self.set_network(network)
        self.set_key(key)

    # Get information
    def get_network(self) -> Any:
        """
        Get Network

        :return: DefichainMainnet | DefichainTestnet
        """
        return self._network

    def get_publicKey(self) -> str:
        """
        Get Public Key

        :return: str
        """
        return self._wallet.public_key()

    def get_privateKey(self) -> str:
        """
        Get Private Key

        :return: str
        """
        return self._wallet.private_key()

    def get_wif(self) -> str:
        """
        Get WIF Key (also private key)

        :return: str
        """
        return self._wallet.wif()

    def get_p2sh(self) -> str:
        """
        Get P2SH (default) Address

        :return: str
        """
        return self._wallet.p2sh_address()

    def get_p2pkh(self) -> str:
        """
        Get P2PKH (legacy) Address

        :return: str
        """

        return self._wallet.p2pkh_address()

    def get_p2wpkh(self) -> str:
        """
        Get P2WPKH (bech32) Address

        :return: str
        """
        return self._wallet.p2wpkh_address()

    def is_private(self) -> bool:
        """
        Checks if given key is a private key

        :return: bool
        """
        return self._is_privateKey(self.get_network(), self._wallet.private_key())

    # Set Information
    def set_network(self, network: "DefichainMainnet | DefichainTestnet") -> None:
        """
        Set Network

        :param network: (required) network instance: DefichainMainnet, DefichainTestnet
        :type network: network
        :return: None
        """
        self._network = network

    def set_key(self, key: str) -> None:
        """
        Set Key

        :param key: (required) public - / private - or wif key
        :type key: str
        :return: None
        """
        if self._is_publicKey(self.get_network(), key):
            self._wallet.from_public_key(key)
        elif self._is_privateKey(self.get_network(), key):
            self._wallet.from_private_key(key)
        elif self._is_wif(self.get_network(), key):
            self._wallet.from_wif(key)
