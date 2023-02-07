from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .base58address import Base58Address
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.transactions.constants import OPCodes, AddressTypes

from .script import Script


class P2SH(Base58Address):  # Pay to Script Hash

    @staticmethod
    def from_publicKey(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, publicKey: str) -> "P2SH":
        """
        Generates a P2SH address object from the given public key

        :param network: (required) The network in witch the public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param publicKey: (required) public key
        :type publicKey: str
        :return: P2SH - returns the P2SH address object
        """
        return P2SH(network, PublicKey(network, publicKey).p2wpkh_address())

    @staticmethod
    def from_privateKey(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, privateKey: str) -> "P2SH":
        """
        Generates a P2SH address object from the given private key

        :param network: (required) The network in witch the private key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param privateKey: (required) private key
        :type privateKey: str
        :return: P2SH - returns the P2SH address object
        """
        return P2SH(network, PrivateKey(network, privateKey).p2wpkh_address())

    @staticmethod
    def from_scriptPublicKey(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
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
