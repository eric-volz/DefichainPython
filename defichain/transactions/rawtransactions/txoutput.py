from abc import ABC

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest

from .txbase import TxBase
from defichain.transactions.address import Address, Script
from defichain.transactions.defitx import DefiTx
from defichain.transactions.defitx.modules.basedefitx import BaseDefiTx
from defichain.transactions.utils import Converter


class TxBaseOutput(TxBase, ABC):

    def __init__(self, value: int, address: str, tokenId: int = 0):
        self._value, self._address, self._tokenId = None, None, None
        self.set_value(value)
        self.set_address(address)
        self.set_tokenId(tokenId)

    def __str__(self):
        result = f"""
        TxOutput
        --------
        Value: {self.get_value()}
        Address: {self.get_address()}
        TokenID: {self.get_tokenId()}
        Serialized: {self.serialize()}
        
        """
        return result

    def verify(self) -> bool:
        self._is_value(self.get_value())
        self._is_address(self.get_address())
        self._is_tokenId(self.get_tokenId())
        return True

    # Get Information
    def get_value(self) -> int:
        return self._value

    def get_address(self) -> str:
        return self._address

    def get_tokenId(self) -> int:
        return self._tokenId

    def get_bytes_value(self) -> bytes:
        return Converter.int_to_bytes(self._value, 8)

    def get_bytes_address(self) -> bytes:
        return Converter.hex_to_bytes(self._address)

    def get_bytes_tokenId(self) -> bytes:
        return Converter.int_to_bytes(self._tokenId, 1)

    def to_json(self) -> {}:
        result = {
            "value": self.get_value(),
            "address": self.get_address(),
            "tokenId": self.get_tokenId()
        }
        return result

    # Set Information
    def set_value(self, value: int) -> None:
        self._value = value

    def set_address(self, address: str) -> None:
        self._address = address

    def set_tokenId(self, tokenId: int) -> None:
        self._tokenId = tokenId

    def set_bytes_value(self, value: bytes) -> None:
        self.set_value(Converter.bytes_to_int(value))

    def set_bytes_address(self, address: bytes) -> None:
        self.set_address(Converter.bytes_to_hex(address))

    def set_bytes_tokenId(self, tokenId: bytes) -> None:
        self.set_tokenId(Converter.bytes_to_int(tokenId))


class TxOutput(TxBaseOutput):

    @staticmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, hex: str) -> "TxOutput":
        value = Converter.hex_to_int(hex[0:16])
        scriptSize = Converter.hex_to_int(hex[16:18])
        length_scriptPublicKey = scriptSize * 2
        scriptPublicKey = hex[18: 18 + length_scriptPublicKey]
        tokenId = Converter.hex_to_int(hex[18 + length_scriptPublicKey: 18 + length_scriptPublicKey + 2])

        address = Address.from_scriptPublicKey(network, scriptPublicKey).get_address()
        return TxOutput(value=value, address=address, tokenId=tokenId)

    def __init__(self, value: int, address: str, tokenId: int = 0):
        super().__init__(value, address, tokenId)

    def __bytes__(self):
        address = Address.from_address(self.get_address())
        scriptSize = Converter.int_to_bytes(len(address.get_bytes_scriptPublicKey()), 1)
        return self.get_bytes_value() + scriptSize + address.get_bytes_scriptPublicKey() + self.get_bytes_tokenId()


class TxMsgOutput(TxBaseOutput):

    @staticmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, hex: str) -> "TxMsgOutput":
        value = Converter.bytes_to_int(Converter.hex_to_bytes(hex[0:16]))
        size = Converter.hex_to_int(hex[16:18])
        OP_Code = hex[18:20]
        msg = Converter.hex_to_str(hex[22: 22 + (size - 2) * 2])
        tokenId = Converter.hex_to_int(hex[22 + (size - 2) * 2: 22 + (size - 2) * 2 + 2])

        obj = TxMsgOutput(msg)
        obj.set_value(value)
        obj.set_tokenId(tokenId)
        return obj

    def __init__(self, msg: str, tokenId: int = 0):
        super().__init__(0, "", tokenId)
        self._msg = None
        self.set_msg(msg)

    def __str__(self):
        result = f"""
        TxMsgOutput
        -----
        Value: {self.get_value()}
        RawMessage: {self.get_hex_msg()}
        DecodedMessage: {self.get_msg()}
        Serialized: {self.serialize()}
                
        """
        return result

    def __bytes__(self):
        script = self.get_bytes_customScript()
        scriptSize = Converter.int_to_bytes(len(script), 1)
        return self.get_bytes_value() + scriptSize + script + self.get_bytes_tokenId()

    # Get Information
    def get_msg(self) -> str:
        return self._msg

    def get_customScript(self) -> str:
        return Converter.bytes_to_hex(Script.script_custom(self.get_msg()))

    def get_bytes_customScript(self) -> bytes:
        return Converter.hex_to_bytes(self.get_customScript())

    def get_hex_msg(self) -> str:
        return Converter.str_to_hex(self.get_msg())

    # Set Information
    def set_msg(self, msg: str) -> None:
        self._msg = msg


class TxDefiOutput(TxBaseOutput):

    @staticmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, hex: str) -> "TxDefiOutput":
        position = 0

        value = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        lengthScript = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        defiTx = DefiTx.deserialize(network, hex[position:])

        return TxDefiOutput(value=value, defiTx=defiTx)

    def __init__(self, value, defiTx: BaseDefiTx):
        super().__init__(value, "")
        self._defiTx: BaseDefiTx = None
        self.set_defiTx(defiTx)

    def __str__(self):
        result = f"""
        TxDefiOutput
        --------------
        Value: {self.get_value()}
        DefiTx: {self.get_defiTx()}
        Serialized: {self.serialize()}

        """
        return result

    def __bytes__(self) -> bytes:
        scriptSize = Converter.int_to_bytes(len(self.get_bytes_defiTx()), 1)
        return self.get_bytes_value() + scriptSize + self.get_bytes_defiTx() + self.get_bytes_tokenId()

    # Get Information
    def get_defiTx(self) -> BaseDefiTx:
        return self._defiTx

    def get_bytes_defiTx(self) -> bytes:
        return self.get_defiTx().bytes()

    # Set Information
    def set_defiTx(self, defiTx: BaseDefiTx) -> None:
        self._defiTx = defiTx
