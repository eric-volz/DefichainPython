

class TxSize:
    """
    Specifies the size in bytes for each element of a transaction
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
    SCRIPT_PUBLIC_KEY: int
    TOKEN_ID: int = 1
