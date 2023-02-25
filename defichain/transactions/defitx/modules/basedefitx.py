from abc import ABC, abstractmethod

from defichain.networks import DefichainMainnet, DefichainTestnet


class BaseDefiTx(ABC):
    @staticmethod
    @abstractmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet, hex: str) -> "BaseDefiTx":
        pass

    @abstractmethod
    def __bytes__(self) -> bytes:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def to_json(self) -> {}:
        pass

    def size(self) -> int:
        return len(self.bytes())

    def serialize(self) -> str:
        return bytes(self).hex()

    def bytes(self) -> bytes:
        return bytes(self)

    @abstractmethod
    def get_defiTxType(self) -> str:
        pass

