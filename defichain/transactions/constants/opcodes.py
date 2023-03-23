
# OP Codes

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
