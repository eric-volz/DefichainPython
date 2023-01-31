from abc import ABC, abstractmethod

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest


class BaseAddress(ABC):

    @staticmethod
    @abstractmethod
    def from_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                        public_key: str) -> "BaseAddress":
        pass

    @staticmethod
    @abstractmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "BaseAddress":
        pass

    @staticmethod
    @abstractmethod
    def decode(address: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def encode(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, scriptPublicKey: str) -> str:
        pass

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest):
        self._network: DefichainMainnet or DefichainTestnet or DefichainRegtest = None
        self.set_network(network)

    @abstractmethod
    def verify(self, address: str) -> bool:
        pass

    # Get Information
    @abstractmethod
    def get_address(self) -> str:
        pass

    def get_network(self) -> DefichainMainnet or DefichainTestnet or DefichainRegtest:
        return self._network

    @abstractmethod
    def get_script_public_key(self) -> str:
        pass

    @abstractmethod
    def get_redeem_script(self) -> str:
        pass

    @abstractmethod
    def get_bytes_script_public_key(self) -> bytes:
        pass

    @abstractmethod
    def get_bytes_redeem_script(self) -> bytes:
        pass

    # Set Information

    @abstractmethod
    def set_address(self, address: str) -> None:
        pass

    def set_network(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest):
        self._network = network


class UnknownAddress(BaseAddress):
    pass
