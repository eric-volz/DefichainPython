import math

from defichain.transactions.constants import TxSize
from .txinput import TxP2PKHInput, TxP2SHInput, TxP2WPKHInput
from .tx import Transaction


def estimate_size(tx: Transaction):
    """
    Estimates the size of the later signed transaction.

    :param tx: (required) the unsigned transaction object
    :type tx: Transaction
    :return: "int" - size of the signed transaction
    """
    # Current Size
    size = tx.size()

    # Add witness and signature size
    for input in tx.get_inputs():
        if isinstance(input, TxP2SHInput) or isinstance(input, TxP2WPKHInput):
            size += TxSize.WITNESS_SIGNATURE_LENGTH + TxSize.WITNESS_SIGNATURE + \
                    TxSize.PUBLIC_KEY_LENGTH + TxSize.PUBLIC_KEY
        elif isinstance(input, TxP2PKHInput):
            size += TxSize.SCRIPTSIG_SIGNATURE
    return size


def estimate_fee(tx: Transaction, feePerByte: float):
    """
    Estimates fees for unsigned transaction

    :param tx: (required) the unsigned transaction object
    :type tx: Transaction
    :param feePerByte: (required) the amount of fee to pay per byte
    :type feePerByte: float
    :return: "int" - the amount of fee to pay
    """

    size = estimate_size(tx)

    return round(size * feePerByte)


def estimate_vsize(tx: Transaction):
    """
    Estimates the vSize of the later signed transaction.

    :param tx: (required) the unsigned transaction object
    :type tx: Transaction
    :return: "int" - vSize of the signed transaction
    """
    unsigned_size = tx.size()
    signed_size = estimate_size(tx)

    return math.ceil(unsigned_size + (signed_size - unsigned_size) / 4)
