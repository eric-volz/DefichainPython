from abc import ABC
from typing import Any

from .txbase import TxBase
from defichain.exceptions.transactions import AddressError, DeserializeError
from defichain.transactions.constants import SEQUENCE
from defichain.transactions.utils import Converter
from defichain.networks import Network
from defichain.transactions.address import Address
from defichain.transactions.constants import AddressTypes


class TxBaseInput(TxBase, ABC):
    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxBaseInput":
        position = 0

        txid = Converter.bytes_to_hex(bytes(reversed(Converter.hex_to_bytes(hex[position: position + 64]))))
        position += 64

        vout = Converter.hex_to_int(hex[position: position + 8])
        position += 8

        length_scriptSig = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        scriptSig = hex[position: position + length_scriptSig]
        position += length_scriptSig

        sequence = hex[position: position + 8]
        position += 8

        return TxInput(txid=txid, vout=vout, scriptSig=scriptSig, sequence=sequence)

    def __init__(self, txid: str, vout: int, scriptSig: str = "", sequence: str = SEQUENCE):
        self._txid, self.vout, self._scriptSig, self._address, self._value, self._sequence = None, None, None, None, None, None
        self.set_txid(txid)
        self.set_vout(vout)
        self.set_scriptSig(scriptSig)
        self.set_sequence(sequence)

        self._private_key: str = ""
        self._public_key: str = ""

    def __bytes__(self) -> bytes:
        length_scriptSig = Converter.int_to_bytes(int(len(self.get_scriptSig()) / 2), 1)
        return self.get_bytes_txid() + self.get_bytes_vout() + length_scriptSig + self.get_bytes_scriptSig() + \
            self.get_bytes_sequence()

    def verify(self) -> bool:
        self._is_txid(self.get_txid())
        self._is_vout(self.get_vout())
        self._is_sequence(self.get_sequence())
        return True

    # Get Information
    def get_txid(self) -> str:
        return self._txid

    def get_vout(self) -> int:
        return self._vout

    def get_sequence(self) -> str:
        return self._sequence

    def get_scriptSig(self) -> str:
        return self._scriptSig

    def get_address(self) -> str:
        return self._address

    def get_value(self) -> int:
        return self._value

    def get_unsignedInput(self) -> str:
        return Converter.bytes_to_hex(self.get_bytes_unsignedInput())

    def get_bytes_txid(self) -> bytes:
        return bytes(reversed(Converter.hex_to_bytes(self.get_txid())))

    def get_bytes_vout(self) -> bytes:
        return Converter.int_to_bytes(self.get_vout(), 4)

    def get_bytes_sequence(self) -> bytes:
        return Converter.hex_to_bytes(self.get_sequence())

    def get_bytes_scriptSig(self) -> bytes:
        return Converter.hex_to_bytes(self.get_scriptSig())

    def get_bytes_address(self) -> bytes:
        return Converter.hex_to_bytes(self.get_address())

    def get_bytes_value(self) -> bytes:
        return Converter.int_to_bytes(self.get_value(), 8)

    def get_bytes_unsignedInput(self) -> bytes:
        return self.get_bytes_txid() + self.get_bytes_vout() + Converter.int_to_bytes(0, 1) + self.get_bytes_sequence()

    # Set Information
    def set_txid(self, txid: str) -> None:
        self._txid = txid

    def set_vout(self, vout: int) -> None:
        self._vout = vout

    def set_sequence(self, sequence: str) -> None:
        self._sequence = sequence

    def set_scriptSig(self, scriptSig: str) -> None:
        self._scriptSig = scriptSig

    def set_address(self, address: str) -> None:
        self._address = address

    def set_value(self, value: int) -> None:
        self._value = value

    def set_bytes_txid(self, txid: bytes) -> None:
        self.set_txid(Converter.bytes_to_hex(bytes(reversed(txid))))

    def set_bytes_vout(self, vout: bytes) -> None:
        self.set_vout(Converter.bytes_to_int(vout))

    def set_bytes_sequence(self, sequence: bytes) -> None:
        self.set_sequence(Converter.bytes_to_hex(sequence))

    def set_bytes_scriptSig(self, scriptSig: bytes) -> None:
        self.set_scriptSig(Converter.bytes_to_hex(scriptSig))

    def set_bytes_address(self, address: bytes) -> None:
        self.set_address(Converter.bytes_to_hex(address))

    def set_bytes_value(self, value: bytes) -> None:
        self.set_value(Converter.bytes_to_int(value))


class TxInput(TxBaseInput):
    """
    Input to spend from given txid

    :param txid: (required) previous transaction id
    :type txid: str
    :param vout: (required) previous transaction output number
    :type vout: int
    :param scriptSig: (optional) signature of P2PKH input
    :type scriptSig: str
    :param sequence: (optional) makes input replaceable when not "ffffffff"
    :type sequence: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxInput":
        """
        Deserializes unsigned transaction input into input object: TxInput.

        Deserializes signed transaction input in the corresponding input object. Only works for TxP2PKHInput |
        TxP2SHInput | TxCoinbaseInput

        :param network: (required) the corresponding network from the raw transaction
        :type network: Network
        :param hex: (required) the raw transaction input as hexadecimal sting
        :type hex: str
        :return: "TxInput"
        """
        input = TxBaseInput.deserialize(network, hex)

        # Unsigned and Signed Coinbase Input
        if input.get_txid() == "0" * 64:
            return TxCoinbaseInput.deserialize(network, hex)

        # Signed P2SH Input
        if Converter.int_to_hex(int(len(input.get_scriptSig()) / 2), 1) == "17":
            return TxP2SHInput.deserialize(network, hex)

        # Signed P2PKH Input
        if int(len(input.get_scriptSig()) / 2) > 23:
            return TxP2PKHInput.deserialize(network, hex)

        return TxInput(input.get_txid(), input.get_vout(), input.get_scriptSig(), input.get_sequence())

    def __init__(self, txid: str, vout: int, scriptSig: str = "", sequence: str = SEQUENCE):
        super().__init__(txid, vout, scriptSig, sequence)

    def to_json(self) -> {}:
        json = {}
        json.update({"inputType": "unsigned"})
        json.update({"txid": self.get_txid()})
        json.update({"vout": self.get_vout()})
        json.update({"scriptSig": self.get_scriptSig()})
        json.update({"sequence": self.get_sequence()})
        return json

    def to_p2pkhInput(self) -> "TxP2PKHInput":
        return TxP2PKHInput(self.get_txid(), self.get_vout(), self.get_scriptSig(), self.get_sequence())

    def to_p2shInput(self, network: Any) -> "TxP2SHInput":
        address = Address.from_scriptPublicKey(network, self.get_scriptSig()).get_address()
        return TxP2SHInput(self.get_txid(), self.get_vout(), address, None, self.get_sequence())

    def to_p2wpkhInput(self) -> "TxP2WPKHInput":
        return TxP2WPKHInput(self.get_txid(), self.get_vout(), "", None, self.get_sequence())


class TxP2PKHInput(TxInput):
    """
    Input to spend from P2PKH address

    :param txid: (required) previous transaction id
    :type txid: str
    :param vout: (required) previous transaction output number
    :type vout: int
    :param scriptSig: (optional) signature of P2PKH input
    :type scriptSig: str
    :param sequence: (optional) makes input replaceable when not "ffffffff"
    :type sequence: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxP2PKHInput":
        input = TxBaseInput.deserialize(network, hex)
        if input.get_scriptSig() != "":
            if len(input.get_scriptSig()) < 23:
                raise DeserializeError("The given input to decode is not an p2pkh input")

        return TxP2PKHInput(input.get_txid(), input.get_vout(), input.get_scriptSig(), input.get_sequence())

    def __init__(self, txid: str, vout: int, scriptSig: str = "", sequence: str = SEQUENCE):
        super().__init__(txid, vout, scriptSig, sequence)

    def to_json(self) -> {}:
        json = {}
        json.update({"inputType": AddressTypes.P2PKH})
        json.update({"txid": self.get_txid()})
        json.update({"vout": self.get_vout()})
        json.update({"scriptSig": self.get_scriptSig()})
        json.update({"sequence": self.get_sequence()})
        return json


class TxP2SHInput(TxInput):
    """
    Input to spend from P2SH address

    :param txid: (required) previous transaction id
    :type txid: str
    :param vout: (required) previous transaction output number
    :type vout: int
    :param address: (optional) address from which the UTXO are spend - (required for signing of the input)
    :type address: str
    :param value: (optional) previous transaction output value - (required for signing of the input)
    :type value: int
    :param sequence: (optional) makes input replaceable when not "ffffffff"
    :type sequence: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxP2SHInput":
        input = TxBaseInput.deserialize(network, hex)
        address = ""
        if input.get_scriptSig() != "":
            address = Address.from_scriptPublicKey(network, input.get_scriptSig()[2:])
            if address.get_addressType() != AddressTypes.P2WPKH:
                raise DeserializeError("The given input to decode is not an p2sh input")
            address = address.get_address()

        return TxP2SHInput(txid=input.get_txid(), vout=input.get_vout(), address=address, sequence=input.get_sequence())

    def __init__(self, txid: str, vout: int, address: str = "", value: int = None, sequence: str = SEQUENCE):
        self._witness = None
        super().__init__(txid, vout, "", sequence)
        self.set_address(address)
        self.set_value(value)

    def to_json(self) -> {}:
        json = {}
        json.update({"inputType": AddressTypes.P2SH})
        json.update({"txid": self.get_txid()})
        json.update({"vout": self.get_vout()})
        json.update({"scriptSig": self.get_scriptSig()})
        json.update({"sequence": self.get_sequence()})
        json.update({"address": self.get_address()})
        json.update({"value": self.get_value()})
        if self.get_witness():
            json.update({"witness": self.get_witness().to_json()})
        return json

    # Get Information
    def get_witness(self) -> "Witness":
        return self._witness

    def get_bytes_witness(self) -> bytes:
        return self.get_witness().bytes()

    # Set Information
    def set_address(self, address: str) -> None:
        if address != "":
            address = Address.from_address(address)
            if address.get_addressType() != AddressTypes.P2WPKH:
                raise AddressError("The given address of an P2SH input needs to be an P2WPKH address")
            else:
                self._address = address.get_address()
                length_scriptPublicKey = Converter.int_to_hex(int(len(address.get_scriptPublicKey()) / 2), 1)
                self.set_scriptSig(length_scriptPublicKey + address.get_scriptPublicKey())
        else:
            self._address = address
            self.set_scriptSig("")

    def set_witness(self, witness) -> None:
        self._witness = witness

    def set_bytes_witness(self, witness: bytes) -> None:
        self.set_witness(Converter.bytes_to_hex(witness))


class TxP2WPKHInput(TxInput):
    """
    Input to spend from P2WPKH address

    :param txid: (required) previous transaction id
    :type txid: str
    :param vout: (required) previous transaction output number
    :type vout: int
    :param address: (optional) address from which the UTXO are spend - (required for signing of the input)
    :type address: str
    :param value: (optional) previous transaction output value - (required for signing of the input)
    :type value: int
    :param sequence: (optional) makes input replaceable when not "ffffffff"
    :type sequence: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxP2WPKHInput":
        input = TxBaseInput.deserialize(network, hex)
        return TxP2WPKHInput(txid=input.get_txid(), vout=input.get_vout(), sequence=input.get_sequence())

    def __init__(self, txid: str, vout: int, address: str = "", value: int = None, sequence: str = SEQUENCE):
        self._witness = None
        super().__init__(txid, vout, "", sequence)
        self.set_address(address)
        self.set_value(value)

    def to_json(self) -> {}:
        json = {}
        json.update({"inputType": AddressTypes.P2WPKH})
        json.update({"txid": self.get_txid()})
        json.update({"vout": self.get_vout()})
        json.update({"scriptSig": self.get_scriptSig()})
        json.update({"sequence": self.get_sequence()})
        json.update({"address": self.get_address()})
        json.update({"value": self.get_value()})
        if self.get_witness():
            json.update({"witness": self.get_witness().to_json()})
        return json

    # Get Information
    def get_witness(self) -> "Witness":
        return self._witness

    def get_bytes_witness(self) -> bytes:
        return Converter.hex_to_bytes(self.get_witness())

    # Set Information
    def set_witness(self, witness) -> None:
        self._witness = witness

    def set_bytes_witness(self, witness: bytes) -> None:
        self.set_witness(Converter.bytes_to_hex(witness))


class TxCoinbaseInput(TxInput):
    """
    Input that generates UTXO from minting a block (Coinbase input)

    :param scriptSig: (optional) number of the minded block
    :type scriptSig: str
    """
    @staticmethod
    def deserialize(network: Any, hex: str) -> "TxCoinbaseInput":
        input = TxBaseInput.deserialize(network, hex)
        if input.get_txid() != "0" * 64:
            raise DeserializeError("The given input to decode is not an coinbase input")
        return TxCoinbaseInput(input.get_scriptSig())

    def __init__(self, scriptSig: str = ""):
        txid = "0" * 64
        vout = 4294967295
        super().__init__(txid, vout, scriptSig)

    def to_json(self) -> {}:
        json = {}
        json.update({"inputType": "coinbase"})
        json.update({"txid": self.get_txid()})
        json.update({"vout": self.get_vout()})
        json.update({"scriptSig": self.get_scriptSig()})
        json.update({"sequence": self.get_sequence()})
        return json
