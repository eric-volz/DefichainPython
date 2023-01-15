# Address
CHARSET: str = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
CHARSET_BASE = len(CHARSET)


class AddressTypes:
    P2PKH: str = "P2PKH"
    P2SH: str = "P2SH"
    P2WPKH: str = "P2WPKH"
    P2WSH: str = "P2WSH"


# TxInput
SEQUENCE: str = "ffffffff"
SCRIPTSIG: str = "00"

# Transaction
SIGHASH = 1

# Script
MAX_OP_LENGTH = 76

# Signing
ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# BaseDefiTx
DefiTx_SIGNATURE: str = "44665478"  # BaseDefiTx

# Utils
FI_PER_BYTE = 1.2


class DefiTxType:
    # Accounts
    OP_DEFI_TX_UTXOS_TO_ACCOUNT: str = "55"  # U
    OP_DEFI_TX_ACCOUNT_TO_UTXOS: str = "62"  # b
    OP_DEFI_TX_ACCOUNT_TO_ACCOUNT: str = "42"  # B
    OP_DEFI_TX_ANY_ACCOUNT_TO_ACCOUNT: str = "61"  # a
    OP_DEFI_TX_FUTURE_SWAP: str = "51"  # Q

    # Governance
    OP_DEFI_TX_SET_GOVERNANCE: str = "47"  # G
    OP_DEFI_TX_SET_GOVERNANCE_HEIGHT: str = "6a"  # j
    OP_DEFI_TX_CREATE_CFP: str = "7a"  # z
    OP_DEFI_TX_CREATE_VOC: str = "45"  # E
    OP_DEFI_TX_VOTE: str = "4f"  # O

    # Loans
    OP_DEFI_TX_SET_LOAN_SCHEME: str = "4c"  # L
    OP_DEFI_TX_DESTROY_LOAN_SCHEME: str = "44"  # D
    OP_DEFI_TX_SET_DEFAULT_LOAN_SCHEME: str = "64"  # d
    OP_DEFI_TX_SET_COLLATERAL_TOKEN: str = "63"  # c
    OP_DEFI_TX_SET_LOAN_TOKEN: str = "67"  # g
    OP_DEFI_TX_UPDATE_LOAN_TOKEN: str = "78"  # x
    OP_DEFI_TX_TAKE_LOAN: str = "58"  # X
    OP_DEFI_TX_PAYBACK_LOAN: str = "48"  # H
    OP_DEFI_TX_PAYBACK_LOAN_V2: str = "6B"  # k

    # Masternode
    OP_DEFI_TX_CREATE_MASTER_NODE: str = "43"  # C
    OP_DEFI_TX_RESIGN_MASTER_NODE: str = "52"  # R
    OP_DEFI_TX_UPDATE_MASTER_NODE: str = "6d"  # m

    # Misc
    OP_DEFI_TX_AUTO_AUTH_PREP: str = "41"  # A

    # Oracles
    OP_DEFI_TX_APPOINT_ORACLE: str = "6f"  # o
    OP_DEFI_TX_REMOVE_ORACLE: str = "68"  # h
    OP_DEFI_TX_UPDATE_ORACLE: str = "74"  # t
    OP_DEFI_TX_SET_ORACLE_DATA: str = "79"  # y

    # Pool
    OP_DEFI_TX_POOL_SWAP: str = "73"  # s
    OP_DEFI_TX_COMPOSITE_SWAP: str = "69"  # i
    OP_DEFI_TX_POOL_ADD_LIQUIDITY: str = "6c"  # l
    OP_DEFI_TX_POOL_REMOVE_LIQUIDITY: str = "72"  # r
    OP_DEFI_TX_POOL_CREATE_PAIR: str = "70"  # p
    OP_DEFI_TX_POOL_UPDATE_PAIR: str = "75"  # u

    # Token
    OP_DEFI_TX_TOKEN_MINT: str = "4d"  # M
    OP_DEFI_TX_TOKEN_CREATE: str = "54"  # T
    OP_DEFI_TX_TOKEN_UPDATE: str = "4e"  # N
    OP_DEFI_TX_TOKEN_UPDATE_ANY: str = "6e"  # n

    # Vault
    OP_DEFI_TX_CREATE_VAULT: str = "56"  # V
    OP_DEFI_TX_UPDATE_VAULT: str = "76"  # v
    OP_DEFI_TX_DEPOSIT_TO_VAULT: str = "53"  # S
    OP_DEFI_TX_WITHDRAW_FROM_VAULT: str = "4A"  # J
    OP_DEFI_TX_CLOSE_VAULT: str = "65"  # e
    OP_DEFI_TX_AUCTION_BID: str = "49"  # I


class OPCodes:
    # push value
    OP_0: str = "00"
    OP_FALSE = OP_0
    OP_PUSHDATA1: str = "4c"
    OP_PUSHDATA2: str = "4d"
    OP_PUSHDATA4: str = "4e"
    OP_1NEGATE: str = "4f"
    OP_RESERVED: str = "50"
    OP_1: str = "51"
    OP_TRUE = OP_1
    OP_2: str = "52"
    OP_3: str = "53"
    OP_4: str = "54"
    OP_5: str = "55"
    OP_6: str = "56"
    OP_7: str = "57"
    OP_7: str = "57"
    OP_8: str = "58"
    OP_9: str = "59"
    OP_10: str = "5a"
    OP_11: str = "5b"
    OP_12: str = "5c"
    OP_13: str = "5d"
    OP_14: str = "5e"
    OP_15: str = "5f"
    OP_16: str = "60"

    # control
    OP_NOP: str = "61"
    OP_VER: str = "62"
    OP_IF: str = "63"
    OP_NOTIF: str = "64"
    OP_VERIF: str = "65"
    OP_VERNOTIF: str = "66"
    OP_ELSE: str = "67"
    OP_ENDIF: str = "68"
    OP_VERIFY: str = "69"
    OP_RETURN: str = "6a"

    # stack ops
    OP_TOALTSTACK: str = "6b"
    OP_FROMALTSTACK: str = "6c"
    OP_2DROP: str = "6d"
    OP_2DUP: str = "6e"
    OP_3DUP: str = "6f"
    OP_2OVER: str = "70"
    OP_2ROT: str = "71"
    OP_2SWAP: str = "72"
    OP_IFDUP: str = "73"
    OP_DEPTH: str = "74"
    OP_DROP: str = "75"
    OP_DUP: str = "76"
    OP_NIP: str = "77"
    OP_OVER: str = "78"
    OP_PICK: str = "79"
    OP_ROLL: str = "7a"
    OP_ROT: str = "7b"
    OP_SWAP: str = "7c"
    OP_TUCK: str = "7d"

    # splice ops
    OP_CAT: str = "7e"
    OP_SUBSTR: str = "7f"
    OP_LEFT: str = "80"
    OP_RIGHT: str = "81"
    OP_SIZE: str = "82"

    # bit logic
    OP_INVERT: str = "83"
    OP_AND: str = "84"
    OP_OR: str = "85"
    OP_XOR: str = "86"
    OP_EQUAL: str = "87"
    OP_EQUALVERIFY: str = "88"
    OP_RESERVED1: str = "89"
    OP_RESERVED2: str = "8a"

    # numeric
    OP_1ADD: str = "8b"
    OP_1SUB: str = "8c"
    OP_2MUL: str = "8d"
    OP_2DIV: str = "8e"
    OP_NEGATE: str = "8f"
    OP_ABS: str = "90"
    OP_NOT: str = "91"
    OP_0NOTEQUAL: str = "92"

    OP_ADD: str = "93"
    OP_SUB: str = "94"
    OP_MUL: str = "95"
    OP_DIV: str = "96"
    OP_MOD: str = "97"
    OP_LSHIFT: str = "98"
    OP_RSHIFT: str = "99"

    OP_BOOLAND: str = "9a"
    OP_BOOLOR: str = "9b"
    OP_NUMEQUAL: str = "9c"
    OP_NUMEQUALVERIFY: str = "9d"
    OP_NUMNOTEQUAL: str = "9e"
    OP_LESSTHAN: str = "9f"
    OP_GREATERTHAN: str = "a0"
    OP_LESSTHANOREQUAL: str = "a1"
    OP_GREATERTHANOREQUAL: str = "a2"
    OP_MIN: str = "a3"
    OP_MAX: str = "a4"

    OP_WITHIN: str = "a5"

    # crypto
    OP_RIPEMD160: str = "a6"
    OP_SHA1: str = "a7"
    OP_SHA256: str = "a8"
    OP_HASH160: str = "a9"
    OP_HASH256: str = "aa"
    OP_CODESEPARATOR: str = "ab"
    OP_CHECKSIG: str = "ac"
    OP_CHECKSIGVERIFY: str = "ad"
    OP_CHECKMULTISIG: str = "ae"
    OP_CHECKMULTISIGVERIFY: str = "af"

    # expansion
    OP_NOP1: str = "b0"
    OP_NOP2: str = "b1"
    OP_CHECKLOCKTIMEVERIFY = OP_NOP2
    OP_NOP3: str = "b2"
    OP_CHECKSEQUENCEVERIFY = OP_NOP3
    OP_NOP4: str = "b3"
    OP_NOP5: str = "b4"
    OP_NOP6: str = "b5"
    OP_NOP7: str = "b6"
    OP_NOP8: str = "b7"
    OP_NOP9: str = "b8"
    OP_NOP10: str = "b9"

    # template matching params
    OP_SMALLINTEGER: str = "fa"
    OP_PUBKEYS: str = "fb"
    OP_PUBKEYHASH: str = "fd"
    OP_PUBKEY: str = "fe"

    OP_INVALIDOPCODE: str = "ff"
