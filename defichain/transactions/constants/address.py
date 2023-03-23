

# Charsets
CHARSET: str = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
CHARSET_BASE = len(CHARSET)


# Address Types
class AddressTypes:
    P2PKH: str = "P2PKH"
    P2SH: str = "P2SH"
    P2WPKH: str = "P2WPKH"


# Max Script Length
MAX_OP_LENGTH = 76
