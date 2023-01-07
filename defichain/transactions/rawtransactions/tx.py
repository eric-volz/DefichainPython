from abc import ABC, abstractmethod


from .txbase import TxBase
from .txinput import TxInput
from .txoutput import TxOutput
from .witness import Witness, WitnessHash
from .sign import sign_input

from defichain.transactions.address.address import DefichainMainnet
from defichain.transactions.keys import PrivateKey, KeyError
from defichain.transactions.utils import *
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
    def sign(self, private_key: str) -> None:
        pass

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
        return int_to_bytes(self.get_version(), 4)

    def get_bytes_marker(self) -> bytes:
        return int_to_bytes(self.get_marker(), 1)

    def get_bytes_flag(self) -> bytes:
        return int_to_bytes(self.get_flag(), 1)

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
        return int_to_bytes(self._sighash, 4)

    def get_bytes_locktime(self) -> bytes:
        return int_to_bytes(self._locktime, 4)

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
        self.set_version(bytes_to_int(version))

    def set_bytes_marker(self, marker: bytes) -> None:
        self.set_marker(bytes_to_int(marker))

    def set_bytes_flag(self, flag: bytes) -> None:
        self.set_flag(bytes_to_int(flag))

    def set_bytes_sighash(self, sighash: bytes) -> None:
        self.set_sighash(bytes_to_int(sighash))

    def set_bytes_locktime(self, locktime: bytes) -> None:
        self.set_locktime(bytes_to_int(locktime))

    # Append information
    def add_input(self, input: TxInput) -> None:
        input.verify()
        self._inputs.append(input)

    def add_output(self, output: TxOutput) -> None:
        output.verify()
        self._outputs.append(output)


class TransactionSegwit(BaseTransaction):

    @staticmethod
    def deserialize(hex: str) -> object:
        """TODO: Deserialize Segwit Transaction"""

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
        result += int_to_bytes(len(self.get_inputs()), 1)
        for input in self.get_inputs():
            result += input.bytes()

        # Outputs
        result += int_to_bytes(len(self.get_outputs()), 1)
        for output in self.get_outputs():
            result += output.bytes()

        # WitnessHash

        if self.get_witness():
            result += int_to_bytes(len(self.get_witness()) * 2, 1)
            for witness in self.get_witness():
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

    def sign(self, private_key: str) -> None:
        """
        Signs the raw transaction with the given private key

        :param: key: private key can be in wif or hex format
        :return: None
        """
        key = None
        if PrivateKey.is_private_key(DefichainMainnet, private_key):
            key = PrivateKey(DefichainMainnet, private_key=private_key)
        elif PrivateKey.is_wif(DefichainMainnet, private_key):
            key = PrivateKey(DefichainMainnet, wif=private_key)
        else:
            raise KeyError("Given private key is not valid")
        private_key = key.get_private_key()
        public_key = key.get_public_key()

        print(private_key)

        for input in self.get_inputs():
            witness_hash = WitnessHash(self, input)
            signature = sign_input(private_key, witness_hash.bytes_hash())
            witness = Witness(signature, public_key)
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


class TransactionLegacy(BaseTransaction):
    """TODO: Spend Legacy Inputs"""
    # raise NotYetSupportedError()


