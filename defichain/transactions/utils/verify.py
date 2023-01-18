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
