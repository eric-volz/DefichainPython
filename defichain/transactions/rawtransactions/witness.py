from abc import ABC
from typing import Any

from defichain.exceptions.transactions import RawTransactionError
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.address.address import Address
from defichain.transactions.rawtransactions.txbase import TxBase
from defichain.transactions.rawtransactions.txinput import TxP2WPKHInput
from defichain.transactions.rawtransactions.txoutput import TxBaseOutput


class WitnessHashBase(TxBase, ABC):

    # Get Information
    @staticmethod
    def get_txid_from_input(input: TxP2WPKHInput) -> str:
        return input.get_txid()

    @staticmethod
    def get_index_from_input(input: TxP2WPKHInput) -> int:
        return input.get_vout()

    @staticmethod
    def get_sequence_from_input(input: TxP2WPKHInput) -> str:
        return input.get_sequence()

    @staticmethod
    def get_address_from_input(input: TxP2WPKHInput) -> str:
        return input.get_address()

    @staticmethod
    def get_value_from_input(input: TxP2WPKHInput) -> int:
        return input.get_value()

    @staticmethod
    def get_bytes_txid_from_input(input: TxP2WPKHInput) -> bytes:
        return input.get_bytes_txid()

    @staticmethod
    def get_bytes_index_from_input(input: TxP2WPKHInput) -> bytes:
        return input.get_bytes_vout()

    @staticmethod
    def get_bytes_sequence_from_input(input: TxP2WPKHInput) -> bytes:
        return input.get_bytes_sequence()

    @staticmethod
    def get_bytes_address_from_input(input: TxP2WPKHInput) -> bytes:
        return input.get_bytes_address()

    @staticmethod
    def get_bytes_value_from_input(input: TxP2WPKHInput) -> bytes:
        return input.get_bytes_value()

    def __init__(self, tx, input: TxP2WPKHInput):
        self._tx, self._input = None, None
        self.set_tx(tx)
        self.set_input(input)

    def hash(self) -> str:
        return Converter.bytes_to_hex(self.bytes())

    def bytes_hash(self) -> bytes:
        return self.bytes()

    # Get Information
    def get_transaction(self) -> TxBase:
        return self._tx

    def get_input(self) -> TxP2WPKHInput:
        return self._input

    def get_version(self) -> int:
        return self._tx.get_version()

    def get_inputs(self) -> [TxP2WPKHInput]:
        return self._tx.get_inputs()

    def get_outputs(self) -> [TxBaseOutput]:
        return self._tx.get_outputs()

    def get_redeemScript(self) -> str:
        return Address.from_address(self.get_address_from_input(self.get_input())).get_redeemScript()

    def get_lockTime(self) -> int:
        return self._tx.get_lockTime()

    def get_sigHash(self) -> int:
        return self._tx.get_sigHash()

    def get_bytes_version(self) -> bytes:
        return self._tx.get_bytes_version()

    def get_bytes_redeemScript(self) -> bytes:
        return Address.from_address(self.get_address_from_input(self.get_input())).get_bytes_redeemScript()

    def get_bytes_lockTime(self) -> bytes:
        return self._tx.get_bytes_lockTime()

    def get_bytes_sigHash(self) -> bytes:
        return self._tx.get_bytes_sigHash()

    def to_json(self) -> {}:
        result = {
            "version": self.get_version(),
            "hashPrevOuts": Converter.bytes_to_hex(self.hash_prevOuts()),
            "hashSequences": Converter.bytes_to_hex(self.hash_sequences()),
            "outpoint": Converter.bytes_to_hex(self.outpoint(self.get_input())),
            "redeem_script": self.get_redeemScript(),
            "value": self.get_value_from_input(self.get_input()),
            "sequence": self.get_sequence_from_input(self.get_input()),
            "hashOutputs": Converter.bytes_to_hex(self.hash_outputs()),
            "locktime": self.get_lockTime(),
            "sighash": self.get_sigHash(),
            "hash": self.hash()
        }
        return result

    # Set Information
    def set_tx(self, tx) -> None:
        self._tx = tx

    def set_input(self, input: TxP2WPKHInput) -> None:
        self._input = input

    # Calc Information
    def outpoint(self, input: TxP2WPKHInput) -> bytes:
        return self.get_bytes_txid_from_input(input) + self.get_bytes_index_from_input(input)

    def hash_prevOuts(self) -> bytes:
        outpoint = b''
        for input in self.get_inputs():
            outpoint += self.outpoint(input)
        return Calculate.dHash256(outpoint)

    def hash_sequences(self) -> bytes:
        sequences = b''
        for input in self.get_inputs():
            sequences += self.get_bytes_sequence_from_input(input)
        return Calculate.dHash256(sequences)

    def hash_outputs(self) -> bytes:
        outputs = b''
        for output in self.get_outputs():
            outputs += bytes(output)
        return Calculate.dHash256(outputs)


class WitnessBase(TxBase, ABC):
    def __init__(self, signature: str, publicKey: str):
        self._signature, self._publicKey = "", ""
        self.set_signature(signature)
        self.set_publicKey(publicKey)

    # Get Information
    def get_signature(self) -> str:
        return self._signature

    def get_publicKey(self) -> str:
        return self._publicKey

    def get_bytes_signature(self) -> bytes:
        return Converter.hex_to_bytes(self.get_signature())

    def get_bytes_publicKey(self) -> bytes:
        return Converter.hex_to_bytes(self.get_publicKey())

    def to_json(self) -> {}:
        lengthSignature = int(len(self.get_signature()) / 2)
        lengthPublicKey = int(len(self.get_publicKey()) / 2)

        json = {}
        json.update({"lengthSignature": lengthSignature})
        json.update({"signature": self.get_signature()})
        json.update({"lengthPublicKey": lengthPublicKey})
        json.update({"publicKey": self.get_publicKey()})
        return json

    # Set Information
    def set_signature(self, signature: str) -> None:
        self._signature = signature

    def set_publicKey(self, publicKey: str) -> None:
        self._publicKey = publicKey

    def set_bytes_signature(self, signature: bytes) -> None:
        self._signature = Converter.bytes_to_hex(signature)

    def set_bytes_publicKey(self, publicKey: bytes) -> None:
        self._publicKey = Converter.bytes_to_hex(publicKey)


class WitnessHash(WitnessHashBase):

    @staticmethod
    def deserialize(network: Any, hex: str) -> "WitnessHash":
        raise RawTransactionError("The witness hash cannot be deserialized")

    def __init__(self, tx, input: TxP2WPKHInput):
        super().__init__(tx, input)

    def __bytes__(self) -> bytes:
        result = self.get_bytes_version()
        result += self.hash_prevOuts()
        result += self.hash_sequences()
        result += self.outpoint(self.get_input())
        result += Converter.int_to_bytes(len(self.get_bytes_redeemScript()), 1)
        result += self.get_bytes_redeemScript()  # Length is no longer part of redeem script
        result += self.get_bytes_value_from_input(self.get_input())
        result += self.get_bytes_sequence_from_input(self.get_input())
        result += self.hash_outputs()
        result += self.get_bytes_lockTime()
        result += self.get_bytes_sigHash()
        return Calculate.dHash256(result)

    def verify(self) -> bool:
        """TODO: Verify inputs of witness hash"""


class Witness(WitnessBase):
    @staticmethod
    def deserialize(network: Any, hex: str) -> "Witness":
        length_signature = Converter.hex_to_int(hex[:2]) * 2
        length_publicKey = Converter.hex_to_int(hex[2 + length_signature: 2 + length_signature + 2]) * 2
        signature = hex[2:length_signature + 2]
        publicKey = hex[2 + length_signature + 2: 2 + length_signature + 2 + length_publicKey]
        return Witness(signature=signature, publicKey=publicKey)

    def __init__(self, signature: str, publicKey: str):
        super().__init__(signature, publicKey)

    def __bytes__(self) -> bytes:
        length_signature = Converter.int_to_bytes(int(len(self.get_signature()) / 2), 1)
        length_publicKey = Converter.int_to_bytes(int(len(self.get_publicKey()) / 2), 1)
        result = length_signature
        result += self.get_bytes_signature()
        result += length_publicKey
        result += self.get_bytes_publicKey()
        return result

    def verify(self) -> bool:
        """TODO: Verify Witness"""
