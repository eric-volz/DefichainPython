from defichain.transactions.constants import TxSize
from .txinput import TxP2PKHInput, TxP2SHInput, TxP2WPKHInput
from .tx import Transaction


def estimate_fee(tx: Transaction, feePerByte: float):
    """
    Signes the transaction to find out the real size

    :param tx: (required) the transaction object
    :type tx: Transaction
    :param feePerByte: (required) the amount of fee to pay per byte
    :type feePerByte: float
    :return: "int" - the amount of fee to pay
    """
    # Current Size
    size = tx.size()

    # Add witniss and signature size
    for input in tx.get_inputs():
        if isinstance(input, TxP2SHInput) or isinstance(input, TxP2WPKHInput):
            size += TxSize.WITNESS_SIGNATURE_LENGTH + TxSize.WITNESS_SIGNATURE + \
                    TxSize.PUBLIC_KEY_LENGTH + TxSize.PUBLIC_KEY
        elif isinstance(input, TxP2PKHInput):
            size += TxSize.SCRIPTSIG_SIGNATURE
    return round(size * feePerByte)

