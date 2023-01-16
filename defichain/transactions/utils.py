import hashlib
from defichain.transactions.constants import FEE_PER_BYTE, TxSize


def int_to_bytes(i: int, length: int) -> bytes:
    return i.to_bytes(length, byteorder="little")


def bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, byteorder="little")


def hex_to_bytes(h: str) -> bytes:
    return bytes.fromhex(h)


def bytes_to_hex(b: bytes) -> str:
    return b.hex()


def hex_to_int(h: str) -> int:
    return int(h, 16)


def int_to_hex(i: int or str, length: int) -> str:
    return i.to_bytes(length=length, byteorder="little").hex()


def str_to_hex(s: str) -> str:
    return s.encode("utf-8").hex()


def hex_to_str(h: str) -> str:
    return bytes.fromhex(h).decode("ascii")


def is_hex(h: str) -> bool:
    try:
        hex_to_int(h)
        return True
    except:
        return False


def is_int(i: int) -> bool:
    return isinstance(i, int)


def dHash256(h: hex) -> bytes:
    return hashlib.sha256(hashlib.sha256(h).digest()).digest()


def calculate_fee_for_unsigned_transaction(tx, fee_per_byte: int = FEE_PER_BYTE) -> int:
    # https://bitcoinops.org/en/tools/calc-size/
    signed_size = tx.size() + TxSize.SIGNATURE_LENGTH + TxSize.SIGNATURE + TxSize.PUBLIC_KEY_LENGTH + \
                  TxSize.PUBLIC_KEY
    return round(signed_size * fee_per_byte)


if __name__ == '__main__':
    print(str_to_hex("hallo"))
    print(hex_to_str(str_to_hex("hallo")))
    print(is_hex("ffffffff"))
    print(is_int(0xffffffff))
