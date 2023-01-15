from defichain.exceptions.transactions.notsupported import NotYetSupportedError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .base58address import Base58Address
from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .base58address import Base58Address
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.transactions.constants import OPCodes

from .script import Script


class P2PKH(Base58Address):  # Legacy
    """ TODO: Implement P2PKH Address"""

    @staticmethod
    def from_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                        public_key: str) -> "P2PKH":
        return P2PKH(network, PublicKey(network, public_key).legacy_address())

    @staticmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "P2PKH":
        return P2PKH(network, PrivateKey(network, private_key).legacy_address())

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)

    def get_script_public_key(self) -> str:
        return Script.build_script([OPCodes.OP_DUP, OPCodes.OP_HASH160, Base58Address.decode(self.get_address())[2:42],
                                    OPCodes.OP_EQUALVERIFY, OPCodes.OP_CHECKSIG])

    def get_redeem_script(self) -> str:
        return self.get_script_public_key()

    def get_bytes_script_public_key(self) -> bytes:
        return bytes.fromhex(self.get_script_public_key())

    def get_bytes_redeem_script(self) -> bytes:
        return bytes.fromhex(self.get_redeem_script())


