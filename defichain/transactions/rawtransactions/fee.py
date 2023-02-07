from defichain.transactions.constants import FEE_PER_BYTE, TxSize


def calculate_fee_for_unsigned_transaction(tx, fee_per_byte: int = FEE_PER_BYTE) -> int:
    signedSize = tx.size() + TxSize.SIGNATURE_LENGTH + TxSize.SIGNATURE + TxSize.PUBLIC_KEY_LENGTH + \
                  TxSize.PUBLIC_KEY
    return round(signedSize * fee_per_byte)
