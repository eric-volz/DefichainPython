from defichain.transactions.constants import OPCodes
from defichain.transactions.utils import Converter, Calculate


class Script(object):

    @staticmethod
    def build_script(data: []) -> str:
        """
        Builds the script with the given parameters

        -> the length of the script is not included at the front of the script

        :param data: script parameters and a decoded address
        :type data: [hex]
        :return: the script that was asked for
        """
        result = ""
        for a in data:
            if len(a) > 2:
                length_address_decode = int(len(a) / 2)
                result += Converter.int_to_hex(length_address_decode, 1) + a
            else:
                result += a
        return result

    @staticmethod
    def custom_script(msg: str) -> bytes:
        op_return = Converter.hex_to_bytes(OPCodes.OP_RETURN)
        msg = Converter.hex_to_bytes(Converter.str_to_hex(msg))
        length_msg = Converter.hex_to_bytes(Calculate.write_compactSize(len(msg)))
        return op_return + length_msg + msg
