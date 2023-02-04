from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .base58address import Base58Address
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.transactions.constants import OPCodes, AddressTypes

from .script import Script


class P2SH(Base58Address):  # Pay to Script Hash

    @staticmethod
    def from_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str) -> "P2SH":
        """
        Generates a P2SH address object from the given public key

        :param network: (required) The network in witch the public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param public_key: (required) public key
        :type public_key: str
        :return: P2SH - returns the P2SH address object
        """
        return P2SH(network, PublicKey(network, public_key).bech32_address())

    @staticmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "P2SH":
        """
        Generates a P2SH address object from the given private key

        :param network: (required) The network in witch the private key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param private_key: (required) private key
        :type private_key: str
        :return: P2SH - returns the P2SH address object
        """
        return P2SH(network, PrivateKey(network, private_key).bech32_address())

    @staticmethod
    def from_script_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                               scriptPublicKey: str) -> "P2SH":
        """
        Generates a P2SH address object from the given script private key

        :param network: (required) The network in witch the script public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param scriptPublicKey: (required) script public key
        :type scriptPublicKey: str
        :return: P2SH - returns the P2SH address object
        """
        return P2SH(network, Base58Address.scriptPublicKey_to_address(network, scriptPublicKey))

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)

    def get_addressType(self) -> str:
        return AddressTypes.P2SH

    def get_scriptPublicKey(self) -> str:
        return Script.build_script([OPCodes.OP_HASH160, Base58Address.decode(self.get_address())[2:42], OPCodes.OP_EQUAL])

    def get_redeemScript(self) -> str:
        return self.get_scriptPublicKey()

    def get_bytes_scriptPublicKey(self) -> bytes:
        return bytes.fromhex(self.get_scriptPublicKey())

    def get_bytes_redeemScript(self) -> bytes:
        return bytes.fromhex(self.get_redeemScript())
