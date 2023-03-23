FEE_PER_BYTE: int = 1


class TxSize:
    """
    Specifies the size in bytes for each element of a transaction

    https://bitcoinops.org/en/tools/calc-size/
    """
    # P2PKH Signature
    SCRIPTSIG_SIGNATURE: int = 107

    # P2SH and P2WPKH Witness
    WITNESS_SIGNATURE_LENGTH: int = 1
    WITNESS_SIGNATURE: int = 73
    PUBLIC_KEY_LENGTH: int = 1
    PUBLIC_KEY: int = 34
