from .bech32address import Bech32Address
from defichain.transactions.constants import OPCodes
from defichain.transactions.utils import *


class Script(object):
    @staticmethod
    def p2wpkh(address: str) -> bytes:
        witness_version = int_to_bytes(0, 1)
        witness_program = hex_to_bytes(Bech32Address.decode(address))
        witness_length = int_to_bytes(len(witness_program), 1)
        return witness_version + witness_length + witness_program

    @staticmethod
    def p2wpkh_script_code(address: str) -> bytes:
        return bytes.fromhex(f"1976a914{Bech32Address.decode(address)}88ac")

    @staticmethod
    def script_custom(msg: str) -> bytes:
        op_return = hex_to_bytes(OPCodes.OP_RETURN)
        msg = hex_to_bytes(str_to_hex(msg))
        msg_length = int_to_bytes(len(msg), 1)
        return op_return + msg_length + msg

