from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .bech32address import Bech32Address
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.transactions.constants import OPCodes

from .script import Script


class P2WPKH(Bech32Address):  # Native Segwit

    @staticmethod
    def from_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str) -> "P2WPKH":
        return P2WPKH(network, PublicKey(network, public_key).bech32_address())

    @staticmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "P2WPKH":
        return P2WPKH(network, PrivateKey(network, private_key).bech32_address())

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)

    def get_script_public_key(self) -> str:
        return Script.build_script([OPCodes.OP_0, Bech32Address.decode(self.get_address())])

    def get_redeem_script(self) -> str:
        return Script.build_script([OPCodes.OP_DUP, OPCodes.OP_HASH160, Bech32Address.decode(self.get_address()),
                                    OPCodes.OP_EQUALVERIFY, OPCodes.OP_CHECKSIG])

    def get_bytes_script_public_key(self) -> bytes:
        return bytes.fromhex(self.get_script_public_key())

    def get_bytes_redeem_script(self) -> bytes:
        return bytes.fromhex(self.get_redeem_script())

