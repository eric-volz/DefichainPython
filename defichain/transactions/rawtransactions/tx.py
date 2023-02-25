from abc import ABC, abstractmethod

from defichain.exceptions.transactions import RawTransactionError
from defichain.networks import DefichainMainnet, DefichainTestnet
from defichain.transactions.keys import PrivateKey, KeyError
from defichain.transactions.utils import Converter
from defichain.transactions.constants import SIGHASH, OPCodes, DefiTx_SIGNATURE

from .txbase import TxBase
from .txinput import TxBaseInput, TxP2WPKHInput
from .txoutput import TxBaseOutput, TxOutput, TxMsgOutput, TxDefiOutput
from .witness import Witness, WitnessHash
from .sign import sign_input


class BaseTransaction(TxBase, ABC):

    def __init__(self, version: int, marker: int, flag: int, inputs: [], outputs: [], sigHash: int = SIGHASH,
                 lockTime: int = 0):
        self._version, self._marker, self._flag, self._inputs, self._outputs, self._sigHash, self._lockTime = None, None, None, [], [], None, None
        self._signed = False
        self.set_version(version)
        self.set_marker(marker)
        self.set_flag(flag)
        self.set_inputs(inputs)
        self.set_outputs(outputs)
        self.set_sigHash(sigHash)
        self.set_lockTime(lockTime)

    # Abstract Methods
    @abstractmethod
    def sign(self, network : DefichainMainnet or DefichainTestnet, private_keys: [str]) -> None:
        pass

    # Calculated Information
    def get_inputsValue(self) -> int:
        result = 0
        for input in self.get_inputs():
            result += input.get_value()
        return result

    def get_outputsValue(self) -> int:
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

    def get_sigHash(self) -> int:
        return self._sigHash

    def get_lockTime(self) -> int:
        return self._lockTime

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
        return Converter.int_to_bytes(self._sigHash, 4)

    def get_bytes_lockTime(self) -> bytes:
        return Converter.int_to_bytes(self._lockTime, 4)

    def is_signed(self) -> bool:
        return self._signed

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

    def set_sigHash(self, sigHash: int) -> None:
        self._sigHash = sigHash

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
        self._inputs.append(input)

    def add_output(self, output: TxBaseOutput) -> None:
        output.verify()
        self._outputs.append(output)


class Transaction(BaseTransaction):

    @staticmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet, hex: str) -> "Transaction":
        """
        For now it's only possible to deserialize Segwit transactions
        TODO:
        - deserialize transactions with P2PKH Inputs
        - deserialize transactions with P2SH inputs
        - deserialize coinbase transactions
        """
        # Decode Unsigned Segwit Transaction
        try:
            position = 0

            version = Converter.hex_to_int(hex[position: position + 8])
            position += 8

            number_of_inputs = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            inputs = []
            for n in range(number_of_inputs):
                input = TxP2WPKHInput.deserialize(network, hex[position: position + 82])
                position += 82

                inputs.append(input)

            number_of_outputs = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            outputs = []
            for n in range(number_of_outputs):
                scriptSize = Converter.hex_to_int(hex[position + 16: position + 18]) * 2
                standardSize = 16 + 2 + 2
                size = standardSize + scriptSize

                if hex[position + 16 + 2: position + 16 + 2 + 2] == OPCodes.OP_RETURN:
                    if DefiTx_SIGNATURE in hex[position + 16 + 2: position + 16 + 2 + scriptSize]:
                        output = TxDefiOutput.deserialize(network, hex[position: position + size])
                    else:
                        output = TxMsgOutput.deserialize(network, hex[position: position + size])
                else:
                    output = TxOutput.deserialize(network, hex[position: position + size])
                position += size

                outputs.append(output)

            lockTime = Converter.hex_to_int(hex[position: position + 8])
            position += 8

            tx = Transaction(inputs=inputs, outputs=outputs, lockTime=lockTime)
            tx.set_version(version)

            return tx
        except Exception as e:
            pass

        # Decode Signed Segwit Transaction
        try:
            position = 0

            version = Converter.hex_to_int(hex[position: position + 8])
            position += 8

            marker = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            flag = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            number_of_inputs = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            inputs = []
            for n in range(number_of_inputs):

                input = TxP2WPKHInput.deserialize(network, hex[position: position + 82])
                position += 82

                inputs.append(input)

            number_of_outputs = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            outputs = []
            for n in range(number_of_outputs):
                scriptSize = Converter.hex_to_int(hex[position + 16: position + 18]) * 2
                standardSize = 16 + 2 + 2
                size = standardSize + scriptSize

                if hex[position + 16 + 2: position + 16 + 2 + 2] == OPCodes.OP_RETURN:
                    if DefiTx_SIGNATURE in hex[position + 16 + 2: position + 16 + 2 + scriptSize]:
                        output = TxDefiOutput.deserialize(network, hex[position: position + size])
                    else:
                        output = TxMsgOutput.deserialize(network, hex[position: position + size])
                else:
                    output = TxOutput.deserialize(network, hex[position: position + size])
                position += size

                outputs.append(output)

            number_of_witnesses = number_of_inputs
            witnesses = []
            for n in range(number_of_witnesses):
                number_of_witnessInputs = Converter.hex_to_int(hex[position: position + 2])
                position += 2

                signature_size = Converter.hex_to_int(hex[position: position + 2]) * 2
                publicKey_size = Converter.hex_to_int(hex[position + signature_size + 2: position + signature_size + 4]) * 2
                size = 2 + signature_size + 2 + publicKey_size
                witness = Witness.deserialize(network, hex[position: position + size])
                position += size

                witnesses.append(witness)

            lockTime = Converter.hex_to_int(hex[position: position + 8])
            position += 8

            tx = Transaction(inputs=inputs, outputs=outputs, lockTime=lockTime)
            tx.set_version(version)
            tx.set_marker(marker)
            tx.set_flag(flag)
            tx.set_witness(witnesses)
            tx._signed = True

            return tx
        except Exception as e:
            pass

        raise RawTransactionError("The given raw transaction can not be decoded")

    def __init__(self, inputs: [], outputs: [], lockTime: int = 0):
        version = 4
        marker = 0
        flag = 1
        sigHash = SIGHASH

        super().__init__(version, marker, flag, inputs, outputs, sigHash, lockTime)
        self._witnessHash: [] = []
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
        result += self.get_bytes_lockTime()
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
        Locktime: {self.get_lockTime()}
        
        """
        return result

    def verify(self) -> bool:
        """TODO: Verify transaction inputs"""

    def sign(self, network: DefichainMainnet or DefichainTestnet, private_keys: [str]) -> None:
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
            self.add_witnessHash(witness_hash)
            self.add_witness(witness)
        self._signed = True

    # Get Information
    def get_witnessHash(self) -> [WitnessHash]:
        return self._witnessHash

    def get_witness(self) -> [Witness]:
        return self._witness

    def to_json(self) -> {}:
        pass

    # Set Information
    def set_witnessHash(self, witnessHash: []) -> None:
        self._witnessHash = witnessHash

    def set_witness(self, witness: []) -> None:
        self._witness = witness

    # Append Information
    def add_witnessHash(self, witnessHash: WitnessHash) -> None:
        witnessHash.verify()
        self._witnessHash.append(witnessHash)

    def add_witness(self, witness: Witness) -> None:
        witness.verify()
        self._witness.append(witness)
