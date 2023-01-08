from defichain.transactions.constants import DefiTxType, MAX_OP_LENGTH, DefiTx_SIGNATURE, OPCodes
from defichain.transactions.utils import *

from .modules.pool import Pool


class BaseDefiTx:

    @staticmethod
    def get_hex_script_length(length: int) -> str:
        """
        Calculates the correct length parameter for a defi transaction

        :param: length: number of bytes
        :return: returns length in hexadecimal string
        """
        if length <= MAX_OP_LENGTH:
            return int_to_hex(length, 1)
        return int_to_hex(MAX_OP_LENGTH, 1) + int_to_hex(length, 1)

    @staticmethod
    def package_dftx(dftx: bytes) -> str:
        signature_dftx = hex_to_bytes(DefiTx_SIGNATURE) + dftx
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