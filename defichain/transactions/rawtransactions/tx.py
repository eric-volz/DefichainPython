from abc import ABC, abstractmethod
from typing import Any

from defichain.exceptions.transactions import RawTransactionError, NotYetSupportedError, DeserializeError
from defichain.networks import Network
from defichain.transactions.address import Address
from defichain.transactions.keys import PrivateKey, KeyError, PublicKey
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.constants import SIGHASH

from .txbase import TxBase
from .txinput import TxBaseInput, TxInput, TxP2PKHInput, TxP2SHInput, TxP2WPKHInput, TxCoinbaseInput
from .txoutput import TxBaseOutput, TxOutput, TxAddressOutput, TxMsgOutput, TxDefiOutput, TxCoinbaseOutput
from .witness import WitnessHash, Witness
from .sign import sign_input


class BaseTransaction(TxBase, ABC):

    def __init__(self, inputs: [], outputs: [], lockTime: int = 0):
        self._version, self._marker, self._flag, self._sigHash, self._inputs, self._outputs, self._lockTime = None, None, None, None, [], [], None
        self._signed = False
        self._coinbase = False
        self._segwit = False
        self.set_inputs(inputs)
        self.set_outputs(outputs)
        self.set_lockTime(lockTime)

    # Abstract Methods
    @abstractmethod
    def sign(self, network: Any, private_keys: [str]) -> "Transaction":
        pass

    @abstractmethod
    def _analyse(self):
        pass

    def bytes_unsigned(self) -> bytes:
        # Version
        result = self.get_bytes_version()

        # Inputs
        result += Calculate.write_compactSize(len(self.get_inputs()), "bytes")
        for input in self.get_inputs():
            result += input.get_bytes_unsignedInput()

        # Outputs
        result += Calculate.write_compactSize(len(self.get_outputs()), "bytes")
        for output in self.get_outputs():
            result += output.bytes()

        # Coinbase Add On
        if self.is_coinbase():
            result += Converter.int_to_bytes(1, 1)  # Number of Elements
            result += Converter.int_to_bytes(32, 1)  # Length of Zeros
            result += Converter.int_to_bytes(0, 32)  # Zeros

        # LockTime
        result += self.get_bytes_lockTime()
        return result

    # Calculated Information
    def get_inputsValue(self) -> "int | None":
        result = 0
        for input in self.get_inputs():
            if isinstance(input, TxP2PKHInput) or isinstance(input, TxCoinbaseInput):
                return None
            elif isinstance(input, TxP2WPKHInput) or isinstance(input, TxP2SHInput):
                if input.get_value() is None:
                    return None
            result += input.get_value()
        return result

    def get_outputsValue(self) -> int:
        result = 0
        for outputs in self.get_outputs():
            result += outputs.get_value()
        return result

    def get_fee(self) -> "int | None":
        return self.get_inputsValue() - self.get_outputsValue() if self.get_inputsValue() is not None else None

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

    def get_sigHash(self) -> int:
        return self._sigHash

    def get_witnessHash(self) -> [WitnessHash]:
        return self._witnessHash

    def get_witness(self) -> [Witness]:
        return self._witness

    def get_lockTime(self) -> int:
        return self._lockTime

    def get_txid(self) -> str:
        return Converter.bytes_to_hex(bytes(reversed(Calculate.dHash256(self.bytes_unsigned()))))

    def get_hash(self):
        hash = Calculate.dHash256(self.bytes())
        return Converter.bytes_to_hex(bytes(reversed(hash)))

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

    def get_bytes_sigHash(self) -> bytes:
        return Converter.int_to_bytes(self.get_sigHash(), 4)

    def get_bytes_lockTime(self) -> bytes:
        return Converter.int_to_bytes(self.get_lockTime(), 4)

    def is_signed(self) -> bool:
        return self._signed

    def is_segwit(self) -> bool:
        return self._segwit

    def is_coinbase(self) -> bool:
        return self._coinbase

    # Set Information
    def set_version(self, version: int) -> None:
        self._version = version

    def set_marker(self, marker: int) -> None:
        self._marker = marker

    def set_flag(self, flag: int) -> None:
        self._flag = flag

    def set_inputs(self, inputs: []) -> None:
        self._inputs = inputs
        self._analyse()

    def set_outputs(self, outputs: []) -> None:
        self._outputs = outputs
        self._analyse()

    def set_sigHash(self, sigHash: int) -> None:
        self._sigHash = sigHash

    def set_witnessHash(self, witnessHash: []) -> None:
        self._witnessHash = witnessHash

    def set_witness(self, witness: []) -> None:
        self._witness = witness

    def set_lockTime(self, lockTime: int) -> None:
        self._lockTime = lockTime

    def set_bytes_version(self, version: bytes) -> None:
        self.set_version(Converter.bytes_to_int(version))

    def set_bytes_marker(self, marker: bytes) -> None:
        self.set_marker(Converter.bytes_to_int(marker))

    def set_bytes_flag(self, flag: bytes) -> None:
        self.set_flag(Converter.bytes_to_int(flag))

    def set_bytes_sigHash(self, sigHash: bytes) -> None:
        self.set_sigHash(Converter.bytes_to_int(sigHash))

    def set_bytes_lockTime(self, lockTime: bytes) -> None:
        self.set_lockTime(Converter.bytes_to_int(lockTime))

    # Append information
    def add_input(self, input: TxBaseInput) -> None:
        input.verify()
        self._analyse()
        self._inputs.append(input)

    def add_output(self, output: TxBaseOutput) -> None:
        output.verify()
        self._analyse()
        self._outputs.append(output)

    def add_witnessHash(self, witnessHash: WitnessHash) -> None:
        witnessHash.verify()
        self._witnessHash.append(witnessHash)

    def add_witness(self, witness: Witness) -> None:
        witness.verify()
        self._witness.append(witness)


class Transaction(BaseTransaction):

    @staticmethod
    def deserialize(network: Any, hex: str) -> "Transaction":
        """
        Deserializes unsigned and signed transaction.

        Creates the respective transaction object.

        Limitations: Not all raw transactions can be deserialized for now. For example, it's not possible to deserialize
        multi signature transactions.

        :param network: (required) the corresponding network from the raw transaction
        :type network: Network
        :param hex: (required) the raw transaction as hexadecimal sting
        :type hex: str
        :return: "Transaction"
        """
        try:
            tx = Transaction([], [])
            position = 0

            # Set Version
            version = Converter.hex_to_int(hex[position: position + 8])
            tx.set_version(version)
            position += 8

            # Set Marker and Flag if exists
            if hex[position: position + 4] == "0001":
                marker = Converter.hex_to_int(hex[position: position + 2])
                tx.set_marker(marker)
                position += 2
                flag = Converter.hex_to_int(hex[position: position + 2])
                tx.set_flag(flag)
                position += 2
                tx._segwit = True

            # Find number of inputs
            length_numberOfInputs = Calculate.get_lengthCompactSize(hex[position: position + 2])
            numberOfInputs = Calculate.read_compactSize(hex[position: position + length_numberOfInputs * 2])
            position += length_numberOfInputs * 2

            # Iterate through all inputs
            inputs = []
            for _ in range(numberOfInputs):
                length_scriptSig = Converter.hex_to_int(hex[position + 72: position + 72 + 2]) * 2
                input = TxInput.deserialize(network, hex[position: position + 82 + length_scriptSig])
                inputs.append(input)
                position += 82 + length_scriptSig

            # Find number of outputs
            length_numberOfOutputs = Calculate.get_lengthCompactSize(hex[position: position + 2])
            numberOfOutputs = Calculate.read_compactSize(hex[position: position + length_numberOfOutputs * 2])
            position += length_numberOfOutputs * 2

            # Iterate through all outputs
            outputs = []
            for _ in range(numberOfOutputs):
                scriptLengthSize = Calculate.get_lengthCompactSize(hex[position + 16: position + 18])
                length_script = Calculate.read_compactSize(hex[position + 16: position + 16 + scriptLengthSize * 2]) * 2

                # If transaction version is 1 or 2 there is no token id at the back of an output
                if tx.get_version() == 1 or tx.get_version() == 2:
                    length_script -= 2

                output = TxOutput.deserialize(network, hex[position: position + 20 + length_script])
                outputs.append(output)
                position += 20 + length_script

            # If transaction is a segwit transaction: Iterate through all witnisses
            witnesses = []
            if tx.is_segwit:
                while hex[position: position + 2] == "02" or hex[position: position + 2] == "00":
                    if hex[position: position + 2] == "00":
                        if len(hex) - position <= 8:
                            break
                        position += 2
                    elif hex[position: position + 2] == "02":
                        position += 2
                        length_signature = Converter.hex_to_int(hex[position: position + 2]) * 2
                        length_publicKey = Converter.hex_to_int(hex[position + 2 + length_signature: position + 2 + length_signature + 2]) * 2
                        length_witness = 2 + length_signature + 2 + length_publicKey
                        witness = Witness.deserialize(network, hex[position: position + length_witness])
                        witnesses.append(witness)
                        position += length_witness
                        tx._signed = True

            # Match all witnisses with the corresponding input
            if tx.is_signed():
                count_witness = 0
                count_inputs = 0
                for input in inputs:
                    if isinstance(input, TxP2SHInput):
                        publicKey_address = PublicKey(network, witnesses[count_witness].get_publicKey()).p2wpkh_address()
                        script_address = Address.from_scriptPublicKey(network, input.get_scriptSig()[2:]).get_address()
                        if publicKey_address == script_address:
                            input.set_witness(witnesses[count_witness])
                            count_witness += 1
                        else:
                            raise DeserializeError("The given p2sh input script signature does not correspond with the "
                                                   "given witness")
                    elif isinstance(input, TxInput) and not input.get_scriptSig():
                        newInput = input.to_p2wpkhInput()
                        newInput.set_witness(witnesses[count_witness])
                        inputs[count_inputs] = newInput
                        count_witness += 1
                    count_inputs += 1

            tx.set_inputs(inputs)
            tx.set_outputs(outputs)
            tx.set_witness(witnesses)

            # Coinbase Transaction
            if tx.is_coinbase():

                numberOfCoinbaseElements = Converter.hex_to_int(hex[position: position + 2])
                position += 2

                length_coinbase = Converter.hex_to_int(hex[position: position + 2]) * 2
                position += 2

                coinbaseElement = Converter.hex_to_int(hex[position: position + length_coinbase])
                position += length_coinbase

            # LockTime
            lockTime = Converter.hex_to_int(hex[position: position + 8])
            tx.set_lockTime(lockTime)
            position += 8

            return tx
        except NotYetSupportedError as e:
            print("This transaction can not be decoded, because the DefiTx is not yet implemented")
        except Exception as e:
            print("This transaction can not be decoded, either this transaction is not supported or there is an error "
                  "in the code.")

    def __init__(self, inputs: [], outputs: [], lockTime: int = 0):
        """
        A transaction object that holds inputs and outputs and can sign these with a provides private key.

        :param inputs: (required) the inputs to spend
        :type inputs: [TxInput]
        :param outputs: (required) the outputs of where to spend
        :type outputs: [TxOutput]
        :param lockTime: (optional) the time to lock the inputs after they have been spent
        :type lockTime: int
        """
        super().__init__(inputs, outputs, lockTime)
        self._analyse()

    def __bytes__(self):
        # Version
        result = self.get_bytes_version()

        # Marker and Flag (Only when Segwit Tx and Signed)
        if self.is_segwit() and self.is_signed():
            result += self.get_bytes_marker()
            result += self.get_bytes_flag()

        # Inputs
        result += Calculate.write_compactSize(len(self.get_inputs()), "bytes")
        for input in self.get_inputs():
            result += input.bytes()

        # Outputs
        result += Calculate.write_compactSize(len(self.get_outputs()), "bytes")
        for output in self.get_outputs():
            result += output.bytes()

        # Witness
        if self.is_signed():
            numberOfWitnessInputs = 0
            for input in self.get_inputs():
                if isinstance(input, TxP2SHInput) or isinstance(input, TxP2WPKHInput):
                    numberOfWitnessInputs += 1

            # Append 00 if not a segwit input -> if there are more than one non segwit inputs at the end, just append
            # the double zeros one time
            stack = []
            if numberOfWitnessInputs > 0:
                for input in self.get_inputs():
                    if isinstance(input, TxP2SHInput) or isinstance(input, TxP2WPKHInput):
                        for byte in stack:
                            result += byte
                        stack = []
                        result += Converter.int_to_bytes(2, 1)
                        result += input.get_witness().bytes()
                    elif isinstance(input, TxP2PKHInput):
                        stack.append(Converter.int_to_bytes(0, 1))
                for byte in stack:
                    result += byte

        # Coinbase Add On
        if self.is_coinbase():
            result += Converter.int_to_bytes(1, 1)  # Number of Elements
            result += Converter.int_to_bytes(32, 1)  # Length of Zeros
            result += Converter.int_to_bytes(0, 32)  # Zeros

        # LockTime
        result += self.get_bytes_lockTime()

        return result

    def sign(self, network: Any, private_keys: [str]) -> "Transaction":
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
            if PrivateKey.is_privateKey(network, key):
                key = PrivateKey(network, privateKey=key)
            elif PrivateKey.is_wif(network, key):
                key = PrivateKey(network, wif=key)
            else:
                raise KeyError("Given private key is not valid")
            keys.append({"private": key.get_privateKey(), "public": key.get_publicKey()})

        # Assign private and public keys to the correct input
        for input in self.get_inputs():
            if isinstance(input, TxP2PKHInput):
                raise NotYetSupportedError()
            if not input._private_key:
                for key in keys:
                    priv = PrivateKey(network, key["private"])
                    if input.get_address() in [priv.p2sh_address(), priv.p2wpkh_address(), priv.p2sh_address()]:
                        input._private_key = key["private"]
                        input._publicKey = key["public"]

        # Sign the inputs with the given keys
        for input in self.get_inputs():
            witness_hash = WitnessHash(self, input)
            signature = sign_input(input._private_key, witness_hash.bytes_hash())
            witness = Witness(signature, input._publicKey)
            input.set_witness(witness)
        self._signed = True
        return self

    def _analyse(self):
        # Analyse Inputs
        signed = None
        for input in self.get_inputs():
            if isinstance(input, TxP2WPKHInput) or isinstance(input, TxP2SHInput):
                self._segwit = True
                if input.get_witness():
                    signed = True
                else:
                    signed = False
            elif isinstance(input, TxCoinbaseInput):
                self._coinbase = True
                self._segwit = True
                signed = True
            elif isinstance(input, TxP2PKHInput):
                if len(input.get_scriptSig()) > 50:
                    signed = True
                else:
                    signed = False
        self._signed = signed

        if not self.get_version():
            self.set_version(4)
        if self.is_segwit():
            if not self.get_marker():
                self.set_marker(0)
            if not self.get_flag():
                self.set_flag(1)
            if not self.get_sigHash():
                self.set_sigHash(SIGHASH)

    def verify(self) -> bool:
        pass

    def to_json(self) -> {}:
        json = {}
        json.update({"txid": self.get_txid()})
        json.update({"hash": self.get_hash()})
        json.update({"size": self.size()})
        json.update({"fee": self.get_fee()})
        json.update({"version": self.get_version()})
        if not self.get_marker() is None:
            json.update({"marker": self.get_marker()})
        if not self.get_flag() is None:
            json.update({"flag": self.get_flag()})
        inputs = []
        for input in self.get_inputs():
            inputs.append(input.to_json())
        json.update({"inputs": inputs})
        outputs = []
        for output in self.get_outputs():
            outputs.append(output.to_json())
        json.update({"outputs": outputs})
        json.update({"lockTime": self.get_lockTime()})
        json.update({"serialized": self.serialize()})
        return json
