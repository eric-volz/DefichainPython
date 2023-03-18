from abc import ABC
from typing import Any

from .txbase import TxBase
from defichain.exceptions.transactions import DeserializeError
from defichain.transactions.constants import OPCodes, DefiTx_SIGNATURE
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.defitx.modules.basedefitx import BaseDefiTx
from defichain.transactions.address import Address, Script
from defichain.transactions.defitx import DefiTx
from defichain.networks import Network


class TxBaseOutput(TxBase, ABC):

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxOutput":
        position = 0

        value = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        scriptSize = Calculate.get_lengthCompactSize(hex[position: position + 2])
        length_script = Calculate.read_compactSize(hex[position: position + scriptSize * 2]) * 2
        position += scriptSize * 2

        script = hex[position: position + length_script]
        position += length_script

        tokenId = Converter.hex_to_int(hex[position: position + 2]) if hex[position: position + 2] != "" else None

        return TxOutput(value=value, script=script, tokenId=tokenId)

    def __init__(self, value: int, script: str, tokenId: int = 0):
        self._value, self._script, self._tokenId = None, None, None
        self.set_value(value)
        self.set_script(script)
        self.set_tokenId(tokenId)

    def __bytes__(self):
        scriptSize = Converter.hex_to_bytes(Calculate.write_compactSize(len(self.get_bytes_script())))
        result = b''
        result += self.get_bytes_value()
        result += scriptSize
        result += self.get_bytes_script()
        if not self.get_tokenId() is None:
            result += self.get_bytes_tokenId()
        return result

    def verify(self) -> bool:
        self._is_value(self.get_value())
        self._is_tokenId(self.get_tokenId())
        return True

    # Get Information
    def get_value(self) -> int:
        return self._value

    def get_script(self) -> str:
        return self._script

    def get_tokenId(self) -> int:
        return self._tokenId

    def get_bytes_value(self) -> bytes:
        return Converter.int_to_bytes(self.get_value(), 8)

    def get_bytes_script(self) -> bytes:
        return Converter.hex_to_bytes(self.get_script())

    def get_bytes_tokenId(self) -> bytes:
        return Converter.int_to_bytes(self.get_tokenId(), 1)

    # Set Information
    def set_value(self, value: int) -> None:
        self._value = value

    def set_script(self, script: str) -> None:
        self._script = script

    def set_tokenId(self, tokenId: int) -> None:
        self._tokenId = tokenId

    def set_bytes_value(self, value: bytes) -> None:
        self.set_value(Converter.bytes_to_int(value))

    def set_bytes_script(self, script: bytes) -> None:
        self.set_script(Converter.bytes_to_hex(script))

    def set_bytes_tokenId(self, tokenId: bytes) -> None:
        self.set_tokenId(Converter.bytes_to_int(tokenId))


class TxOutput(TxBaseOutput):
    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxOutput":
        """
        Deserializes a transaction output into an output object: TxAddressOutput | TxMsgOutput | TxDefiOutput |
        TxCoinbaseOutput.

        :param network: (required) the corresponding network from the raw transaction
        :type network: Network
        :param hex: (required) the raw transaction output as hexadecimal sting
        :type hex: str
        :return: "TxInput"
        """
        output = TxBaseOutput.deserialize(network, hex)
        if output.get_script()[0: 2] == OPCodes.OP_RETURN:
            if DefiTx_SIGNATURE in output.get_script()[4: 16]:
                return TxDefiOutput.deserialize(network, hex)
            elif output.get_script()[4: 12] == "aa21a9ed":
                return TxCoinbaseOutput.deserialize(network, hex)
            else:
                return TxMsgOutput.deserialize(network, hex)
        if len(output.get_script()) > 0:
            return TxAddressOutput.deserialize(network, hex)
        return output

    def __init__(self, value: int, script: str, tokenId: int):
        """
        Output to spend the specified inputs UTXO

        :param value:
        :type value:
        :param script:
        :type script:
        :param tokenId:
        :type tokenId:
        """
        super().__init__(value, script, tokenId)

    def to_json(self) -> {}:
        json = {}
        json.update({"outputType": None})
        json.update({"value": self.get_value()})
        json.update({"script": self.get_script()})
        json.update({"tokenId": self.get_tokenId()})
        return json


class TxAddressOutput(TxOutput):
    """
    An output that specifies the address to which the UXTO of the inpus should be sent

    :param value: (required) how many UTXO to send
    :type value: int
    :param address: (required) address to send the UTXO to
    :type address: str
    :param tokenId: (optional) which token you want to send (almost always 0 -> stands for DFI)
    :type tokenId: int
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxAddressOutput":
        output = TxBaseOutput.deserialize(network, hex)
        address = Address.from_scriptPublicKey(network, output.get_script()).get_address()
        return TxAddressOutput(value=output.get_value(), address=address, tokenId=output.get_tokenId())

    def __init__(self, value: int, address: str, tokenId: int = 0):
        self._address = None
        self.set_address(address)
        super().__init__(value, Address.from_address(address).get_scriptPublicKey(), tokenId)

    def to_json(self) -> {}:
        json = {}
        json.update({"outputType": "address"})
        json.update({"value": self.get_value()})
        json.update({"address": self.get_address()})
        json.update({"script": self.get_script()})
        json.update({"tokenId": self.get_tokenId()})
        return json

    # Get Information
    def get_address(self) -> str:
        return self._address

    def get_bytes_address(self) -> bytes:
        return Converter.hex_to_bytes(self.get_address())

    # Set Information
    def set_address(self, address: str) -> None:
        address = Address.from_address(address)
        self._address = address.get_address()
        self.set_script(address.get_scriptPublicKey())

    def set_bytes_address(self, address: bytes) -> None:
        self.set_address(Converter.bytes_to_hex(address))


class TxMsgOutput(TxOutput):

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxMsgOutput":
        output = TxBaseOutput.deserialize(network, hex)
        OP_Code = output.get_script()[0: 2]
        if OP_Code != OPCodes.OP_RETURN:
            raise DeserializeError("The given output to decode is not an message output (there is not OP_RETURN)")
        length_script = Converter.hex_to_int(output.get_script()[2: 4]) * 2
        msg = Converter.hex_to_str(output.get_script()[4: 4 + length_script])
        txMsgOutput = TxMsgOutput(msg=msg, tokenId=output.get_tokenId())
        txMsgOutput.set_value(output.get_value())
        return txMsgOutput

    def __init__(self, msg: str, tokenId: int = 0):
        """
        An output witch includes a message.

        Uses OP_RETURN Code.
        TODO: Is limited to around 200 bytes

        :param msg: (required) your text in plane text like "Hello Defichain Community!"
        :type msg: str
        :param tokenId: (optional) which token you want to send (almost always 0 -> stands for DFI)
        :type tokenId: int
        """
        self._msg = None
        self.set_msg(msg)
        super().__init__(0, self.get_customScript(), tokenId)

    # Get Information
    def get_msg(self) -> str:
        return self._msg

    def get_customScript(self) -> str:
        return Converter.bytes_to_hex(Script.custom_script(self.get_msg()))

    def get_bytes_customScript(self) -> bytes:
        return Converter.hex_to_bytes(self.get_customScript())

    def get_hex_msg(self) -> str:
        return Converter.str_to_hex(self.get_msg())

    def to_json(self) -> {}:
        json = {}
        json.update({"outputType": "msg"})
        json.update({"value": self.get_value()})
        json.update({"rawMsg": self.get_hex_msg()})
        json.update({"decodesMsg": self.get_msg()})
        json.update({"script": self.get_script()})
        json.update({"tokenId": self.get_tokenId()})
        return json

    # Set Information
    def set_msg(self, msg: str) -> None:
        self._msg = msg
        self.set_script(self.get_customScript())

    def set_hex_msg(self, msg: str) -> None:
        self.set_msg(Converter.hex_to_str(msg))


class TxDefiOutput(TxOutput):
    """
    An Output witch includes a defi transaction.

    For example a "Poolswap" or "AddPoolLiquidity"

    :param value: (required) how many UTXO to send (almost always zero)
    :type value: int
    :param defiTx: (required) a DefiTx Object
    :type defiTx: DefiTx
    :param tokenId: (optional) which token you want to send (almost always 0 -> stands for DFI)
    :type tokenId: int
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxDefiOutput":
        output = TxBaseOutput.deserialize(network, hex)
        defiTx = DefiTx.deserialize(network, output.get_script())
        return TxDefiOutput(value=output.get_value(), defiTx=defiTx, tokenId=output.get_tokenId())

    def __init__(self, value, defiTx: BaseDefiTx, tokenId: int = 0):
        self._defiTx: BaseDefiTx = None
        self.set_defiTx(defiTx)
        super().__init__(value, self.get_defiTx().serialize(), tokenId)

    # Get Information
    def get_defiTx(self) -> BaseDefiTx:
        return self._defiTx

    def get_bytes_defiTx(self) -> bytes:
        return self.get_defiTx().bytes()

    def to_json(self) -> {}:
        json = {}
        json.update({"outputType": "defiTx"})
        json.update({"value": self.get_value()})
        json.update({"defiTx": self.get_defiTx().to_json()})
        json.update({"script": self.get_script()})
        json.update({"tokenId": self.get_tokenId()})
        return json

    # Set Information
    def set_defiTx(self, defiTx: BaseDefiTx) -> None:
        self._defiTx = defiTx
        self.set_script(self.get_defiTx().serialize())


class TxCoinbaseOutput(TxOutput):
    """
    An output that is specified with every coinbase transaction.

    :param script: (required) Coinbase specific output
    :type script: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxCoinbaseOutput":
        output = TxBaseOutput.deserialize(network, hex)
        txCoinbaseOutput = TxCoinbaseOutput(output.get_script())
        txCoinbaseOutput.set_value(output.get_value())
        txCoinbaseOutput.set_tokenId(output.get_tokenId())
        return txCoinbaseOutput

    def __init__(self, script: str):
        value = int("0" * 16)
        super().__init__(value, script, 0)

    def to_json(self) -> {}:
        json = {}
        json.update({"outputType": "coinbase"})
        json.update({"value": self.get_value()})
        json.update({"script": self.get_script()})
        json.update({"tokenId": self.get_tokenId()})
        return json
