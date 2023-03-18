from abc import ABC, abstractmethod
from typing import Any
import json

from defichain.exceptions.transactions import RawTransactionError
from defichain.networks import Network
from defichain.transactions.address import Address
from defichain.transactions.utils import Verify


class TxBase(ABC):

    @staticmethod
    def _is_txid(txid: str) -> bool:
        if txid:
            if not Verify.is_hex(txid):
                raise RawTransactionError("The given txid is not an hexadecimal string")
            if not len(txid) == 64:
                raise RawTransactionError("The given txid has not the length of 64 characters")
            return True

    @staticmethod
    def _is_vout(index: int) -> bool:
        if index:
            if not Verify.is_int(index):
                raise RawTransactionError("The given index is not an integer")
            return True

    @staticmethod
    def _is_address(address: str) -> bool:
        if address:
            if not Address.from_address(address).verify(address):
                raise RawTransactionError("The given address is not an valid")
            return True

    @staticmethod
    def _is_value(value: int) -> bool:
        if value:
            if not Verify.is_int(value):
                raise RawTransactionError("The given value is not an integer")
            return True

    @staticmethod
    def _is_sequence(sequence: str) -> bool:
        if sequence:
            if not Verify.is_hex(sequence):
                raise RawTransactionError("The given sequence is not an hexadecimal string")
            if not len(sequence) == 8:
                raise RawTransactionError("The given sequence has not the length of 8 characters")
            return True

    @staticmethod
    def _is_scriptSig(scriptSig: str) -> bool:
        if scriptSig:
            if not Verify.is_hex(scriptSig):
                raise RawTransactionError("The given script signature is not an hexadecimal string")
            if not len(scriptSig) == 2:
                raise RawTransactionError("The given script signature has not the length of 2 characters")
            return True

    @staticmethod
    def _is_tokenId(tokenId: int) -> bool:
        if tokenId:
            if not Verify.is_int(tokenId):
                raise RawTransactionError("The given tokenid is not an integer")
            return True

    @staticmethod
    @abstractmethod
    def deserialize(network: Any, hex: str) -> "TxBase":
        """
        Deserializes the given hex into the object that was used to call this method

        :param network: (required) network from defichain.networks
        :type network: Network
        :param hex: (required) the hey that should be deserialized
        :type hex: str
        :return: "TxBase" - the object that was used to call the method
        """
        pass

    @abstractmethod
    def __bytes__(self) -> bytes:
        pass

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=5)

    @abstractmethod
    def to_json(self) -> {}:
        """
        Returns information about the transaction object in json format
        :return: "{}" - information about the object that was used to call this method
        """
        pass

    @abstractmethod
    def verify(self) -> bool:
        """
        Verifies the correctness of all given entries in the given object

        :return: "bool" - returns True if all entries are correct
        """
        pass

    def size(self) -> int:
        """
        Calculates the size in bytes of the object that was used to call this method

        :return: "int" - size in bytes of the object that was used to call this method
        """
        return len(self.bytes())

    def serialize(self) -> str:
        """
        Serializes the object that was used to call this method

        :return: "str" - serialized object that that was used to call this method

        """
        self.verify()
        return bytes(self).hex()

    def bytes(self) -> bytes:
        """
        Bytes representation of the object that was used to call this method

        :return: "bytes" - bytes of the object that was used to call this method
        """
        self.verify()
        return bytes(self)


