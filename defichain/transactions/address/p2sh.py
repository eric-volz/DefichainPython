from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .base58address import Base58Address
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.transactions.constants import OPCodes

from .script import Script


class P2SH(Base58Address):  # Pay to Script Hash

    @staticmethod
    def from_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str) -> "P2SH":
        return P2SH(network, PublicKey(network, public_key).bech32_address())

    @staticmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "P2SH":
        return P2SH(network, PrivateKey(network, private_key).bech32_address())

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)

    def get_script_public_key(self) -> str:
        return Script.build_script([OPCodes.OP_HASH160, Base58Address.decode(self.get_address())[2:42], OPCodes.OP_EQUAL])

    def get_redeem_script(self) -> str:
        return self.get_script_public_key()

    def get_bytes_script_public_key(self) -> bytes:
        return bytes.fromhex(self.get_script_public_key())

    def get_bytes_redeem_script(self) -> bytes:
        return bytes.fromhex(self.get_redeem_script())
