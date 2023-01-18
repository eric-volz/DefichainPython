from .address import AddressTypes

FEE_PER_BYTE: int = 1


class TxSize:
    """
    Specifies the size in bytes for each element of a transaction

    https://bitcoinops.org/en/tools/calc-size/
    """
    # Overhead
    VERSION: int = 4
    MARKER: int = 1
    FLAG: int = 1
    INPUT_COUNT: int = 1
    OUTPUT_COUNT: int = 1
    LOCK_TIME: int = 4

    # Input
    TXID: int = 32
    INDEX: int = 1
    SCRIPTSIG: int = 1
    SEQUENCE: int = 4

    # Witness
    SIGNATURE_LENGTH: int = 1
    SIGNATURE: int = 73
    PUBLIC_KEY_LENGTH: int = 1
    PUBLIC_KEY: int = 34

    # Output
    VALUE: int = 8
    SCRIPT_PUBLIC_KEY_LENGTH: int = 1
    SCRIPT_PUBLIC_KEY: {} = {AddressTypes.P2PKH: 25, AddressTypes.P2SH: 23, AddressTypes.P2WPKH: 22}
    TOKEN_ID: int = 1
