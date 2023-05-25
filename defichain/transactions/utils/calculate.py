import hashlib
import io


class Calculate:

    @staticmethod
    def dHash256(h: hex) -> bytes:
        return hashlib.sha256(hashlib.sha256(h).digest()).digest()

    @staticmethod
    def length_varInt(hex: str) -> int:
        size = 0
        split = [hex[i:i + 2] for i in range(0, len(hex), 2)]
        for s in split:
            integer = int.from_bytes(bytes.fromhex(s), byteorder="little")
            if integer < 0x80:
                size += 1
                break
            else:
                size += 1
        return size

    @staticmethod
    def write_varInt(n: int) -> str:
        # https://github.com/JellyfishSDK/jellyfish/blob/d57b37bb2b10dfb44389c0d1f6a0c6428fa82d7e/packages/jellyfish-buffer/src/VarInt.ts#L21
        # https://github.com/DeFiCh/ain/blob/0edc8e002ddc634dcb80785b9e9e01606fd8e4f7/src/serialize.h#L355
        buffer = [None for _ in range(20)]
        length = 0

        while True:
            buffer[length] = (n & 0x7F) | (0x80 if length else 0x00)
            if n <= 0x7F:
                break
            n = (n >> 7) - 1
            length += 1
        result = []
        for b in list(reversed(buffer)):
            result.append(int(b).to_bytes(length=1, byteorder="little").hex()) if b else None
        if not length + 1 == len(result):
            result.append("00")
        return "".join(result)

    @staticmethod
    def read_varInt(hex: str) -> int:
        buffer = io.BytesIO(bytes.fromhex(hex))

        n = 0
        while True:
            buff = buffer.read(1)[0]
            n = (n << 7) | (buff & 0x7f)
            if (buff & 0x80) != 0:
                n += 1
            else:
                return n

    @staticmethod
    def length_compactSize(hex: str) -> int:
        indicator = hex[0:2]
        if indicator == "fd":
            return 3
        elif indicator == "fe":
            return 5
        elif indicator == "ff":
            return 9
        else:
            return 1

    @staticmethod
    def write_compactSize(n: int, unit="hex") -> "str | bytes":
        if n < 0xfd:
            result = n.to_bytes(length=1, byteorder="little").hex()
        elif n <= 0xffff:
            result = "fd" + n.to_bytes(length=2, byteorder="little").hex()
        elif n <= 0xffffffff:
            result = "fe" + n.to_bytes(length=4, byteorder="little").hex()
        else:
            result = "ff" + n.to_bytes(length=8, byteorder="little").hex()
        if unit == "hex":
            return result
        elif unit == "bytes":
            return bytes.fromhex(result)
        else:
            raise Exception("Unit is not available")

    @staticmethod
    def read_compactSize(hex: str) -> int:
        if hex[0:2] == "fd":
            return int.from_bytes(bytes.fromhex(hex[2:6]), byteorder="little")
        elif hex[0:2] == "fe":
            return int.from_bytes(bytes.fromhex(hex[2:10]), byteorder="little")
        elif hex[0:2] == "ff":
            return int.from_bytes(bytes.fromhex(hex[2:18]), byteorder="little")
        else:
            return int.from_bytes(bytes.fromhex(hex), byteorder="little")

    @staticmethod
    def addressAmountSum(addressAmount: {}) -> "int | float":
        resultValue = 0
        for address in addressAmount:
            if isinstance(addressAmount[address], list):
                for amount in addressAmount[address]:
                    value, token = amount.split('@')
                    if "." in value:
                        resultValue += float(value)
                    else:
                        resultValue += int(value)
            else:
                value, token = addressAmount[address].split('@')
                if "." in value:
                    resultValue += float(value)
                else:
                    resultValue += int(value)
        return resultValue


if __name__ == "__main__":
    c = Calculate.write_varInt(2 ** 32)
    print(c)
    print(Calculate.read_varInt(c))
    print(2**32)
