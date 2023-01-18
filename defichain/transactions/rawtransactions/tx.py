from abc import ABC, abstractmethod

from defichain.exceptions.transactions import RawTransactionError

from .txbase import TxBase
from .txinput import TxBaseInput
from .txoutput import TxBaseOutput
from .witness import Witness, WitnessHash
from .sign import sign_input

from defichain.networks import DefichainMainnet
from defichain.transactions.keys import PrivateKey, KeyError
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter
from defichain.transactions.constants import SIGHASH


class BaseTransaction(TxBase, ABC):

    def __init__(self, version: int, marker: int, flag: int, inputs: [], outputs: [], sighash: int = SIGHASH,
                 locktime: int = 0):
        self._version, self._marker, self._flag, self._inputs, self._outputs, self._sighash, self._locktime = None, None, None, [], [], None, None
        self._signed = False
        self.set_version(version)
        self.set_marker(marker)
        self.set_flag(flag)
        self.set_inputs(inputs)
        self.set_outputs(outputs)
        self.set_sighash(sighash)
        self.set_locktime(locktime)

    # Abstract Methods
    @abstractmethod
    def sign(self, private_keys: [str]) -> None:
        pass

    # Calculated Information
    def get_inputs_value(self) -> int:
        result = 0
        for input in self.get_inputs():
            result += input.get_value()
        return result

    def get_outputs_value(self) -> int:
        result = 0
        for outputs in self.get_outputs():
            result += outputs.get_value()
        return result

    # Get Information
    def get_version(self) -> int:
        return self._version

    def get_marker(self) -> int:
        return self._marker

    def get_flag(self) -> int:
        return self._flag

    def get_inputs(self) -> []:
        return self._inputs

    def get_outputs(self) -> []:
        return self._outputs

    def get_sighash(self) -> int:
        return self._sighash

    def get_locktime(self) -> int:
        return self._locktime

    def get_bytes_version(self) -> bytes:
        return Converter.int_to_bytes(self.get_version(), 4)

    def get_bytes_marker(self) -> bytes:
        return Converter.int_to_bytes(self.get_marker(), 1)

    def get_bytes_flag(self) -> bytes:
        return Converter.int_to_bytes(self.get_flag(), 1)

    def get_bytes_inputs(self) -> bytes:
        result = b''
        for input in self._inputs:
            result += input.bytes()
        return result

    def get_bytes_outputs(self) -> bytes:
        result = b''
        for output in self._outputs:
            result += output.bytes()
        return result

    def get_bytes_sighash(self) -> bytes:
        return Converter.int_to_bytes(self._sighash, 4)

    def get_bytes_locktime(self) -> bytes:
        return Converter.int_to_bytes(self._locktime, 4)

    # Set Information
    def set_version(self, version: int) -> None:
        self._version = version

    def set_marker(self, marker: int) -> None:
        self._marker = marker

    def set_flag(self, flag: int) -> None:
        self._flag = flag

    def set_inputs(self, inputs: []) -> None:
        self._inputs = inputs

    def set_outputs(self, outputs: []) -> None:
        self._outputs = outputs

    def set_sighash(self, sighash: int) -> None:
        self._sighash = sighash

    def set_locktime(self, locktime: int) -> None:
        self._locktime = locktime

    def set_bytes_version(self, version: bytes) -> None:
        self.set_version(Converter.bytes_to_int(version))

    def set_bytes_marker(self, marker: bytes) -> None:
        self.set_marker(Converter.bytes_to_int(marker))

    def set_bytes_flag(self, flag: bytes) -> None:
        self.set_flag(Converter.bytes_to_int(flag))

    def set_bytes_sighash(self, sighash: bytes) -> None:
        self.set_sighash(Converter.bytes_to_int(sighash))

    def set_bytes_locktime(self, locktime: bytes) -> None:
        self.set_locktime(Converter.bytes_to_int(locktime))

    # Append information
    def add_input(self, input: TxBaseInput) -> None:
        input.verify()
        self._inputs.append(input)

    def add_output(self, output: TxBaseOutput) -> None:
        output.verify()
        self._outputs.append(output)


class Transaction(BaseTransaction):

    @staticmethod
    def deserialize(hex: str) -> object:
        """TODO: Deserialize Transactions"""

    def __init__(self, inputs: [], outputs: [], locktime: int = 0):
        version = 4
        marker = 0
        flag = 1
        sighash = SIGHASH

        super().__init__(version, marker, flag, inputs, outputs, sighash, locktime)
        self._witness_hash: [] = []
        self._witness: [] = []

    def __bytes__(self):
        # Version
        result = self.get_bytes_version()

        if self._signed:
            result += self.get_bytes_marker()  # defi segwit transaction has no marker
            result += self.get_bytes_flag()  # defi segwit transaction has no flag

        # Inputs
        result += Converter.int_to_bytes(len(self.get_inputs()), 1)
        for input in self.get_inputs():
            result += input.bytes()

        # Outputs
        result += Converter.int_to_bytes(len(self.get_outputs()), 1)
        for output in self.get_outputs():
            result += output.bytes()

        # WitnessHash

        if self.get_witness():
            for witness in self.get_witness():
                result += Converter.int_to_bytes(2, 1)
                result += witness.bytes()

        # Locktime
        result += self.get_bytes_locktime()
        return result

    def __str__(self) -> str:
        result = f"""
        Segwit Transaction
        ------------------
        Version: {self.get_version()}
        Marker: {self.get_marker()}
        Flag: {self.get_flag()}
        Number of Inputs: {len(self.get_inputs())}
        Number of Outputs: {len(self.get_outputs())}
        Number of Witnesses: {len(self.get_witness())}
        Locktime: {self.get_locktime()}
        
        """
        return result

    def verify(self) -> bool:
        """TODO: Verify transaction inputs"""

    def sign(self, private_keys: [str]) -> None:
        """
        Signs the raw transaction with the given private keys

        :param: key: private key can be in wif or hex format
        :return: None
        """
        if not isinstance(private_keys, list):
            raise RawTransactionError("The given private keys have to be parsed in a list: [key, key, ...]")

        # Check if wif and calc hexadecimal private key
        keys = []
        for key in private_keys:
            if PrivateKey.is_private_key(DefichainMainnet, key):
                key = PrivateKey(DefichainMainnet, private_key=key)
            elif PrivateKey.is_wif(DefichainMainnet, key):
                key = PrivateKey(DefichainMainnet, wif=key)
            else:
                raise KeyError("Given private key is not valid")
            keys.append({"private": key.get_private_key(), "public": key.get_public_key()})

        # Assign private and public keys to the correct input
        for input in self.get_inputs():
            if not input._private_key:
                network = Address.from_address(input.get_address()).get_network()
                for key in keys:
                    priv = PrivateKey(network, key["private"])
                    if input.get_address() in [priv.default_address(), priv.bech32_address(), priv.default_address()]:
                        input._private_key = key["private"]
                        input._public_key = key["public"]

        # Sign the inputs with the given keys
        for input in self.get_inputs():
            witness_hash = WitnessHash(self, input)
            signature = sign_input(input._private_key, witness_hash.bytes_hash())
            witness = Witness(signature, input._public_key)
            self.add_witness_hash(witness_hash)
            self.add_witness(witness)
        self._signed = True

    # Get Information
    def get_witness_hash(self) -> [WitnessHash]:
        return self._witness_hash

    def get_witness(self) -> [Witness]:
        return self._witness

    def to_json(self) -> {}:
        pass

    # Set Information
    def set_witness_hash(self, witness_hash: []) -> None:
        self._witness_hash = witness_hash

    def set_witness(self, witness: []) -> None:
        self._witness = witness

    # Append Information
    def add_witness_hash(self, witness_hash: WitnessHash) -> None:
        witness_hash.verify()
        self._witness_hash.append(witness_hash)

    def add_witness(self, witness: Witness) -> None:
        witness.verify()
        self._witness.append(witness)
