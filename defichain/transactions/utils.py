import hashlib


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


def int_to_hex(i: int) -> str:
    return hex(i)


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


if __name__ == '__main__':
    print(str_to_hex("hallo"))
    print(hex_to_str(str_to_hex("hallo")))
    print(is_hex("ffffffff"))
    print(is_int(0xffffffff))

