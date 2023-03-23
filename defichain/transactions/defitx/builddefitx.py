from defichain.exceptions.transactions import RawTransactionError
from defichain.transactions.constants import DefiTx_SIGNATURE, OPCodes
from defichain.transactions.utils import Converter


class BuildDefiTx:
    @staticmethod
    def get_hex_scriptLength(length: int) -> str:
        # https://github.com/JellyfishSDK/jellyfish/blob/main/packages/jellyfish-transaction/src/script/data.ts
        """
        Calculates the correct length parameter for a defi transaction

        If the defi transaction is loger than 76 characters, a separate length indicator is needed: in this case the
        first length operator (after op_return) is 4c (hex -> int 76). After this first length operator is the operator
        witch indicates the real length of the defi transaction.

        :param: length: number of bytes
        :return: "hex" - returns length in hexadecimal string
        """
        if length < 76:
            return Converter.int_to_hex(length, 1)
        elif length <= 255:
            return "4c" + Converter.int_to_hex(length, 1)
        elif length <= 65535:
            return "4d" + Converter.int_to_hex(length, 2)
        elif length <= 16777215:
            return "4e" + Converter.int_to_hex(length, 4)
        else:
            raise RawTransactionError("Script is to large")

    @staticmethod
    def build_defiTx(defiTx: bytes) -> bytes:
        """
        Builds the defi transaction. In this sate it can be implemented into a transaction and broadcasted to the
        blockchain.

        :param defiTx: (required) - Bytes of the defi transaction from BaseDefiTx Class
        :return: "bytes" - defi transaction with OP_RETURN code and calculated length
        """
        signature_defiTx = Converter.hex_to_bytes(DefiTx_SIGNATURE) + defiTx
        length_signature_defiTx = BuildDefiTx.get_hex_scriptLength(len(signature_defiTx))

        return Converter.hex_to_bytes(OPCodes.OP_RETURN) + Converter.hex_to_bytes(length_signature_defiTx) + \
            signature_defiTx
