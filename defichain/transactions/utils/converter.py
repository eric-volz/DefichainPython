

class Converter:

    # Integer - Bytes
    @staticmethod
    def int_to_bytes(i: int, length: int) -> bytes:
        return i.to_bytes(length, byteorder="little")

    @staticmethod
    def bytes_to_int(b: bytes) -> int:
        return int.from_bytes(b, byteorder="little")

    # Hex - Bytes
    @staticmethod
    def hex_to_bytes(h: str) -> bytes:
        return bytes.fromhex(h)

    @staticmethod
    def bytes_to_hex(b: bytes) -> str:
        return b.hex()

    # Hex - Integer
    @staticmethod
    def hex_to_int(h: str) -> int:
        return int(h, 16)

    @staticmethod
    def int_to_hex(i: int or str, length: int) -> str:
        return i.to_bytes(length=length, byteorder="little").hex()

    # String - Hex
    @staticmethod
    def str_to_hex(s: str) -> str:
        return s.encode("utf-8").hex()

    @staticmethod
    def hex_to_str(h: str) -> str:
        return bytes.fromhex(h).decode("ascii")
