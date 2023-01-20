from .converter import Converter


class Verify:

    @staticmethod
    def is_hex(h: str) -> bool:
        try:
            Converter.hex_to_int(h)
            return True
        except:
            return False

    @staticmethod
    def is_int(i: int) -> bool:
        return isinstance(i, int)

    @staticmethod
    def is_float(f: float) -> bool:
        return isinstance(f, float)

    @staticmethod
    def is_str(s: str) -> bool:
        return isinstance(s, str)

    @staticmethod
    def is_only_number_str(s: str) -> bool:
        try:
            int(s)
            return True
        except:
            return False

