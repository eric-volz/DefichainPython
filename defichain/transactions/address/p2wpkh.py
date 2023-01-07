

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .bech32address import Bech32Address
from defichain.transactions.keys import PrivateKey, PublicKey

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

    def get_script(self) -> str:
        return Script.p2wpkh(self.get_address()).hex()

    def get_script_code(self) -> str:
        return Script.p2wpkh_script_code(self.get_address()).hex()

    def get_bytes_script(self) -> bytes:
        return Script.p2wpkh(self.get_address())

    def get_bytes_script_code(self) -> bytes:
        return Script.p2wpkh_script_code(self.get_address())
