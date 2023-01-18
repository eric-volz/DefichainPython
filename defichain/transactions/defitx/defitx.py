from defichain.transactions.constants import DefiTxType, MAX_OP_LENGTH, DefiTx_SIGNATURE, OPCodes
from defichain.transactions.utils import Converter

from .modules.pool import Pool


class BaseDefiTx:

    @staticmethod
    def get_hex_script_length(length: int) -> str:
        """
        Calculates the correct length parameter for a defi transaction

        If the defi transaction is loger than 76 characters, a separate length indicator is needed: in this case the
        first length operator (after op_return) is 4c (hex -> int 76). After this first length operator is the operator
        witch indicates the real length of the defi transaction.


        :param: length: number of bytes
        :return: returns length in hexadecimal string
        """
        if length <= MAX_OP_LENGTH:
            return Converter.int_to_hex(length, 1)
        return Converter.int_to_hex(MAX_OP_LENGTH, 1) + Converter.int_to_hex(length, 1)

    @staticmethod
    def package_defitx(defitx: bytes) -> str:
        """
        Packages the defi transaction. In this sate it can be implemented into a transaction and broadcasted to the
        blockchain.

        :param defitx:
        :return: the correct defi transaction
        """
        signature_dftx = Converter.hex_to_bytes(DefiTx_SIGNATURE) + defitx
        length_of_siganture_dftx = BaseDefiTx.get_hex_script_length(len(signature_dftx))

        return OPCodes.OP_RETURN + length_of_siganture_dftx + signature_dftx.hex()


class DefiTx(BaseDefiTx):

    _baseDefiTx = BaseDefiTx()

    accounts = None
    governance = None
    loans = None
    masterndoe = None
    oracles = None
    pool = Pool(_baseDefiTx)
    token = None
    vault = None
