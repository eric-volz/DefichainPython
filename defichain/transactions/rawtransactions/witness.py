from abc import ABC
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.rawtransactions.txbase import TxBase
from defichain.transactions.rawtransactions.txinput import TxBaseInput
from defichain.transactions.rawtransactions.txoutput import TxBaseOutput
from defichain.transactions.address.address import Address


class WitnessHashBase(TxBase, ABC):

    # Get Information
    @staticmethod
    def get_txid_from_input(input: TxBaseInput) -> str:
        return input.get_txid()

    @staticmethod
    def get_index_from_input(input: TxBaseInput) -> int:
        return input.get_index()

    @staticmethod
    def get_sequence_from_input(input: TxBaseInput) -> str:
        return input.get_sequence()

    @staticmethod
    def get_address_from_input(input: TxBaseInput) -> str:
        return input.get_address()

    @staticmethod
    def get_value_from_input(input: TxBaseInput) -> int:
        return input.get_value()

    @staticmethod
    def get_bytes_txid_from_input(input: TxBaseInput) -> bytes:
        return input.get_bytes_txid()

    @staticmethod
    def get_bytes_index_from_input(input: TxBaseInput) -> bytes:
        return input.get_bytes_index()

    @staticmethod
    def get_bytes_sequence_from_input(input: TxBaseInput) -> bytes:
        return input.get_bytes_sequence()

    @staticmethod
    def get_bytes_address_from_input(input: TxBaseInput) -> bytes:
        return input.get_bytes_address()

    @staticmethod
    def get_bytes_value_from_input(input: TxBaseInput) -> bytes:
        return input.get_bytes_value()

    def __init__(self, tx, input: TxBaseInput):
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

    def get_input(self) -> TxBaseInput:
        return self._input

    def get_version(self) -> int:
        return self._tx.get_version()

    def get_inputs(self) -> [TxBaseInput]:
        return self._tx.get_inputs()

    def get_outputs(self) -> [TxBaseOutput]:
        return self._tx.get_outputs()

    def get_redeem_script(self) -> str:
        return Address.from_address(self.get_address_from_input(self.get_input())).get_redeem_script()

    def get_locktime(self) -> int:
        return self._tx.get_locktime()

    def get_sighash(self) -> int:
        return self._tx.get_sighash()

    def get_bytes_version(self) -> bytes:
        return self._tx.get_bytes_version()

    def get_bytes_redeem_script(self) -> bytes:
        return Address.from_address(self.get_address_from_input(self.get_input())).get_bytes_redeem_script()

    def get_bytes_locktime(self) -> bytes:
        return self._tx.get_bytes_locktime()

    def get_bytes_sighash(self) -> bytes:
        return self._tx.get_bytes_sighash()

    def to_json(self) -> {}:
        result = {
            "version": self.get_version(),
            "hashPrevOuts": Converter.bytes_to_hex(self.hashPrevOuts()),
            "hashSequences": Converter.bytes_to_hex(self.hashSequences()),
            "outpoint": Converter.bytes_to_hex(self.outpoint(self.get_input())),
            "redeem_script": self.get_redeem_script(),
            "value": self.get_value_from_input(self.get_input()),
            "sequence": self.get_sequence_from_input(self.get_input()),
            "hashOutputs": Converter.bytes_to_hex(self.hashOutputs()),
            "locktime": self.get_locktime(),
            "sighash": self.get_sighash(),
            "hash": self.hash()
        }
        return result

    # Set Information
    def set_tx(self, tx) -> None:
        self._tx = tx

    def set_input(self, input: TxBaseInput) -> None:
        self._input = input

    # Calc Information
    def outpoint(self, input: TxBaseInput) -> bytes:
        return self.get_bytes_txid_from_input(input) + self.get_bytes_index_from_input(input)

    def hashPrevOuts(self) -> bytes:
        outpoint = b''
        for input in self.get_inputs():
            outpoint += self.outpoint(input)
        return Calculate.dHash256(outpoint)

    def hashSequences(self) -> bytes:
        sequences = b''
        for input in self.get_inputs():
            sequences += self.get_bytes_sequence_from_input(input)
        return Calculate.dHash256(sequences)

    def hashOutputs(self) -> bytes:
        outputs = b''
        for output in self.get_outputs():
            outputs += bytes(output)
        return Calculate.dHash256(outputs)


class WitnessBase(TxBase, ABC):
    def __init__(self, signature: str, public_key: str):
        self._signature, self._public_key = "", ""
        self.set_signature(signature)
        self.set_public_key(public_key)

    # Get Information
    def get_signature(self) -> str:
        return self._signature

    def get_public_key(self) -> str:
        return self._public_key

    def get_bytes_signature(self) -> bytes:
        return Converter.hex_to_bytes(self.get_signature())

    def get_bytes_public_key(self) -> bytes:
        return Converter.hex_to_bytes(self.get_public_key())

    def to_json(self) -> {}:
        result = {
            "signature": self.get_signature(),
            "public_key": self.get_public_key()
        }
        return result

    # Set Information
    def set_signature(self, signature: str) -> None:
        self._signature = signature

    def set_public_key(self, public_key: str) -> None:
        self._public_key = public_key

    def set_bytes_signature(self, signature: bytes) -> None:
        self._signature = Converter.bytes_to_hex(signature)

    def set_bytes_public_key(self, public_key: bytes) -> None:
        self._public_key = Converter.bytes_to_hex(public_key)


class WitnessHash(WitnessHashBase):

    @staticmethod
    def deserialize(hex: str) -> object:
        """TODO: Deserialize WitnessHash"""

    def __init__(self, tx, input: TxBaseInput):
        super().__init__(tx, input)

    def __bytes__(self) -> bytes:
        result = self.get_bytes_version()
        result += self.hashPrevOuts()
        result += self.hashSequences()
        result += self.outpoint(self.get_input())
        result += Converter.int_to_bytes(len(self.get_bytes_redeem_script()), 1)
        result += self.get_bytes_redeem_script()  # Length is no longer part of redeem script
        result += self.get_bytes_value_from_input(self.get_input())
        result += self.get_bytes_sequence_from_input(self.get_input())
        result += self.hashOutputs()
        result += self.get_bytes_locktime()
        result += self.get_bytes_sighash()
        return Calculate.dHash256(result)

    def __str__(self):
        string = f"""
        Witness Hash
        ------------
        Version: {Converter.bytes_to_hex(self.get_bytes_version())}
        HashPrevOut: {Converter.bytes_to_hex(self.hashPrevOuts())}
        HashSequence: {Converter.bytes_to_hex(self.hashSequences())}
        Txid: {self.get_txid_from_input(self.get_input())}
        Index: {Converter.bytes_to_int(self.get_bytes_index_from_input(self.get_input()))}
        Outpoint: {Converter.bytes_to_hex(self.outpoint(self.get_input()))}
        Redeem Script: {self.get_redeem_script()}
        Amount: {Converter.bytes_to_hex(self.get_bytes_value_from_input(self.get_input()))}
        Sequence: {Converter.bytes_to_int(self.get_bytes_sequence_from_input(self.get_input()))}
        HashOutput: {Converter.bytes_to_hex(self.hashOutputs())}
        LockTime: {Converter.bytes_to_hex(self.get_bytes_locktime())}
        SigHash: {Converter.bytes_to_hex(self.get_bytes_sighash())}
        Hash: {self.hash()}
        """
        return string

    def verify(self) -> bool:
        """TODO: Verify inputs of witness hash"""


class Witness(WitnessBase):
    @staticmethod
    def deserialize(hex: str) -> "Witness":
        signature_length = Converter.hex_to_int(hex[:2]) * 2
        public_key_length = Converter.hex_to_int(hex[2 + signature_length: 2 + signature_length + 2]) * 2
        signature = hex[2:signature_length + 2]
        public_key = hex[2 + signature_length + 2: 2 + signature_length + 2 + public_key_length]
        return Witness(signature=signature, public_key=public_key)

    def __init__(self, signature: str, public_key: str):
        super().__init__(signature, public_key)

    def __bytes__(self) -> bytes:
        signature_length = Converter.int_to_bytes(int(len(self.get_signature()) / 2), 1)
        public_key_length = Converter.int_to_bytes(int(len(self.get_public_key()) / 2), 1)
        result = signature_length
        result += self.get_bytes_signature()
        result += public_key_length
        result += self.get_bytes_public_key()
        return result

    def __str__(self) -> str:
        signature_length = Converter.int_to_bytes(int(len(self.get_signature()) / 2), 1)
        public_key_length = Converter.int_to_bytes(int(len(self.get_public_key()) / 2), 1)
        result = f"""
        Witness
        -------
        Signature Length: {signature_length}
        Signature: {self.get_signature()}
        Public Key Length: {public_key_length}
        Public Key: {self.get_public_key()}
        
        """
        return result

    def verify(self) -> bool:
        """TODO: Verify Witness"""
