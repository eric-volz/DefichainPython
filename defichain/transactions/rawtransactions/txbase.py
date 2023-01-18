from abc import ABC, abstractmethod

from defichain.exceptions.transactions import RawTransactionError

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
    def _is_index(index: int) -> bool:
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
    def _is_scriptsig(scriptsig: str) -> bool:
        if scriptsig:
            if not Verify.is_hex(scriptsig):
                raise RawTransactionError("The given script signature is not an hexadecimal string")
            if not len(scriptsig) == 2:
                raise RawTransactionError("The given script signature has not the length of 2 characters")
            return True

    @staticmethod
    def _is_tokenid(tokenid: int) -> bool:
        if tokenid:
            if not Verify.is_int(tokenid):
                raise RawTransactionError("The given tokenid is not an integer")
            return True

    @staticmethod
    @abstractmethod
    def deserialize(hex: str) -> object:
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

    @abstractmethod
    def verify(self) -> bool:
        """
        Verifies the correctness of all given entries in the given object

        :return: (bool) returns True if all entries are correct
        """
        pass

    def size(self) -> int:
        return len(self.bytes())

    def serialize(self) -> str:
        self.verify()
        return bytes(self).hex()

    def bytes(self) -> bytes:
        self.verify()
        return bytes(self)


