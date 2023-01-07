
# Address
CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
CHARSET_BASE = len(CHARSET)
POSSIBLE_ADDRESS_TYPES = ("p2pkh", "p2sh", "p2wpkh", "p2wsh")

# TxInput
SEQUENCE = "ffffffff"
SCRIPTSIG = "00"

# Transaction
SIGHASH = 1

# Signing
ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


class CustomTxType:
    pass


class OPCodes:
    OP_RETURN: hex = '6a'
