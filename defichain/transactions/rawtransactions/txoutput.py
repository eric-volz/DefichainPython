from abc import ABC

from .txbase import TxBase
from defichain.transactions.address import Address
from defichain.transactions.address import Script
from defichain.transactions.utils import *


class TxBaseOutput(TxBase, ABC):

    def __init__(self, value: int, address: str, tokenid: int = 0):
        self._value, self._address, self._tokenid = None, None, None
        self.set_value(value)
        self.set_address(address)
        self.set_tokenid(tokenid)

    def __str__(self):
        result = f"""
        TxOutput
        --------
        Value: {self.get_value()}
        Address: {self.get_address()}
        TokenID: {self.get_tokenid()}
        Serialized: {self.serialize()}
        
        """
        return result

    def verify(self) -> bool:
        self._is_value(self.get_value())
        self._is_address(self.get_address())
        self._is_tokenid(self.get_tokenid())
        return True

    # Get Information
    def get_value(self) -> int:
        return self._value

    def get_address(self) -> str:
        return self._address

    def get_tokenid(self) -> int:
        return self._tokenid

    def get_bytes_value(self) -> bytes:
        return int_to_bytes(self._value, 8)

    def get_bytes_address(self) -> bytes:
        return hex_to_bytes(self._address)

    def get_bytes_tokenid(self) -> bytes:
        return int_to_bytes(self._tokenid, 1)

    def to_json(self) -> {}:
        result = {
            "value": self.get_value(),
            "address": self.get_address(),
            "tokenid": self.get_tokenid()
        }
        return result

    # Set Information
    def set_value(self, value: int) -> None:
        self._value = value

    def set_address(self, address: str) -> None:
        self._address = address

    def set_tokenid(self, tokenid: int) -> None:
        self._tokenid = tokenid

    def set_bytes_value(self, value: bytes) -> None:
        self.set_value(bytes_to_int(value))

    def set_bytes_address(self, address: bytes) -> None:
        self.set_address(bytes_to_hex(address))

    def set_bytes_tokenid(self, tokenid: bytes) -> None:
        self.set_tokenid(bytes_to_int(tokenid))


class TxOutput(TxBaseOutput):

    @staticmethod
    def deserialize(hex: str) -> "TxOutput":
        """TODO: Deserialize the output"""

    def __init__(self, value: int, address: str, tokenid: int = 0):
        super().__init__(value, address, tokenid)

    def __bytes__(self):
        address = Address.from_address(self.get_address())
        script_size = int_to_bytes(len(address.get_bytes_script()), 1)
        return self.get_bytes_value() + script_size + address.get_bytes_script() + self.get_bytes_tokenid()


class TxMsg(TxBaseOutput):

    @staticmethod
    def deserialize(hex: str) -> "TxMsg":
        value = bytes_to_int(hex_to_bytes(hex[0:16]))
        size = hex_to_int(hex[16:18])
        OP_Code = hex[18:20]
        msg = hex_to_str(hex[22: 22 + (size - 2) * 2])
        tokenid = hex_to_int(hex[22 + (size - 2) * 2: 22 + (size - 2) * 2 + 2])

        obj = TxMsg(msg)
        obj.set_value(value)
        obj.set_tokenid(tokenid)
        return obj

    def __init__(self, msg: str, tokenid: int = 0):
        super().__init__(0, "", tokenid)
        self._msg = msg

    def __str__(self):
        result = f"""
        TxCustomOutput
        --------------
        Value: {self.get_value()}
        RawMessage: {self.get_hex_msg()}
        DecodedMessage: {self.get_msg()}
        Serialized: {self.serialize()}
                
        """
        return result

    def __bytes__(self):
        script = self.get_bytes_custom_script()
        script_size = int_to_bytes(len(script), 1)
        return self.get_bytes_value() + script_size + script + self.get_bytes_tokenid()

    # Get Information
    def get_msg(self) -> str:
        return self._msg

    def get_custom_script(self) -> str:
        return bytes_to_hex(Script.script_custom(self.get_msg()))

    def get_bytes_custom_script(self) -> bytes:
        return hex_to_bytes(self.get_custom_script())

    def get_hex_msg(self) -> str:
        return str_to_hex(self.get_msg())

    # Set Information
    def set_msg(self, msg: str) -> None:
        self._msg = msg

