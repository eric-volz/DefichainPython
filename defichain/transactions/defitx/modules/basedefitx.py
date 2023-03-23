from abc import ABC, abstractmethod
from typing import Any
import json


class BaseDefiTx(ABC):
    @staticmethod
    @abstractmethod
    def deserialize(network: Any, hex: str) -> "BaseDefiTx":
        pass

    @abstractmethod
    def __bytes__(self) -> bytes:
        pass

    def __str__(self):
        return json.dumps(self.to_json(), indent=5)

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

