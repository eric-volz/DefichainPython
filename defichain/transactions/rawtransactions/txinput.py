from abc import ABC

from .txbase import TxBase
from defichain.transactions.utils import Converter
from defichain.transactions.constants import SEQUENCE, SCRIPTSIG


class TxBaseInput(TxBase, ABC):

    def __init__(self, txid: str, index: int, address: str = None, value: int = None, sequence: str = SEQUENCE, scriptsig: str = SCRIPTSIG):
        self._txid, self._index, self._address, self._value, self._sequence, self._scriptsig = None, None, None, None, None, None
        self.set_txid(txid)
        self.set_index(index)
        self.set_address(address)
        self.set_value(value)
        self.set_sequence(sequence)
        self.set_scriptsig(scriptsig)

        self._private_key: str = ""
        self._public_key: str = ""

    def __str__(self):
        result = f"""
        TxInput
        -------
        Txid: {self.get_txid()}
        Index: {self.get_index()}
        Address: {self.get_address()}
        Value: {self.get_value()}
        Sequence: {self.get_sequence()}
        Script Signature: {self.get_scriptsig()}
        Serialized: {self.serialize()}
        
        """
        return result

    def verify(self) -> bool:
        self._is_txid(self.get_txid())
        self._is_index(self.get_index())
        self._is_address(self.get_address())
        self._is_value(self.get_value())
        self._is_sequence(self.get_sequence())
        return True

    # Get Information
    def get_txid(self) -> str:
        return self._txid

    def get_index(self) -> int:
        return self._index

    def get_address(self) -> str:
        return self._address

    def get_value(self) -> int:
        return self._value

    def get_sequence(self) -> str:
        return self._sequence

    def get_scriptsig(self) -> str:
        return self._scriptsig

    def get_bytes_txid(self) -> bytes:
        return bytes(reversed(Converter.hex_to_bytes(self.get_txid())))

    def get_bytes_index(self) -> bytes:
        return Converter.int_to_bytes(self.get_index(), 4)

    def get_bytes_address(self) -> bytes:
        return Converter.hex_to_bytes(self.get_address())

    def get_bytes_value(self) -> bytes:
        return Converter.int_to_bytes(self.get_value(), 8)

    def get_bytes_sequence(self) -> bytes:
        return Converter.hex_to_bytes(self.get_sequence())

    def get_bytes_scriptsig(self) -> bytes:
        return Converter.hex_to_bytes(self.get_scriptsig())

    def to_json(self) -> {}:
        result = {
            "txid": self.get_txid(),
            "vout": self.get_index(),
            "address": self.get_address(),
            "value": self.get_value(),
            "scriptSig": self.get_scriptsig(),
            "sequence": self.get_sequence()
        }
        return result

    # Set Information
    def set_txid(self, txid: str) -> None:
        self._txid = txid

    def set_index(self, index: int) -> None:
        self._index = index

    def set_address(self, address: str) -> None:
        self._address = address

    def set_value(self, value: int) -> None:
        self._value = value

    def set_sequence(self, sequence: str) -> None:
        self._sequence = sequence

    def set_scriptsig(self, scriptsig: str) -> None:
        self._scriptsig = scriptsig

    def set_bytes_txid(self, txid: bytes) -> None:
        self.set_txid(Converter.bytes_to_hex(bytes(reversed(txid))))

    def set_bytes_index(self, index: bytes) -> None:
        self.set_index(Converter.bytes_to_int(index))

    def set_bytes_address(self, address: bytes) -> None:
        self.set_address(Converter.bytes_to_hex(address))

    def set_bytes_value(self, value: bytes) -> None:
        self.set_value(Converter.bytes_to_int(value))

    def set_bytes_sequence(self, sequence: bytes) -> None:
        self.set_sequence(Converter.bytes_to_hex(sequence))

    def set_bytes_scriptsig(self, scriptsig: bytes) -> None:
        self.set_scriptsig(Converter.bytes_to_hex(scriptsig))


class TxInput(TxBaseInput):

    @staticmethod
    def deserialize(hex) -> "TxBaseInput":
        txid = Converter.bytes_to_hex(bytes(reversed(Converter.hex_to_bytes(hex[0:64]))))
        index = Converter.hex_to_int(hex[64:72])
        scriptsig = hex[72:74]
        sequence = hex[74:82]
        return TxInput(txid=txid, index=index, sequence=sequence, scriptsig=scriptsig)

    def __init__(self, txid: str, index: int, address: str = None, value: int = None, sequence: str = SEQUENCE, scriptsig: str = SCRIPTSIG):
        super().__init__(txid, index, address, value, sequence, scriptsig)

    def __bytes__(self) -> bytes:
        return self.get_bytes_txid() + self.get_bytes_index() + self.get_bytes_scriptsig() + self.get_bytes_sequence()

