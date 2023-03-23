from defichain.exceptions.transactions import VerifyError
from .converter import Converter


class Verify:

    @staticmethod
    def is_hex(h: str) -> bool:
        try:
            Converter.hex_to_int(h)
            return True
        except:
            raise VerifyError("The given value is not a hex string")

    @staticmethod
    def is_int(i: int) -> bool:
        if isinstance(i, int):
            return True
        raise VerifyError("The given value is not an integer")

    @staticmethod
    def is_float(f: float) -> bool:
        if isinstance(f, float):
            return True
        raise VerifyError("The given value is not an float")

    @staticmethod
    def is_str(s: str) -> bool:
        if isinstance(s, str):
            return True
        raise VerifyError("The given value is not an string")

    @staticmethod
    def is_only_number_str(s: str) -> bool:
        try:
            int(s)
            return True
        except:
            return False

