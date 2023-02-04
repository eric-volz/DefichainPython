from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .bech32address import Bech32Address
from defichain.transactions.keys import PrivateKey, PublicKey
from defichain.transactions.constants import OPCodes, AddressTypes

from .script import Script


class P2WPKH(Bech32Address):  # Native Segwit
    @staticmethod
    def from_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, public_key: str) -> "P2WPKH":
        """
        Generates a P2WPKH address object from the given public key

        :param network: (required) The network in witch the public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param public_key: (required) public key
        :type public_key: str
        :return: P2WPKH - returns the P2WPKH address object
        """
        return P2WPKH(network, PublicKey(network, public_key).bech32_address())

    @staticmethod
    def from_private_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         private_key: str) -> "P2WPKH":
        """
        Generates a P2WPKH address object from the given private key

        :param network: (required) The network in witch the private key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param private_key: (required) private key
        :type private_key: str
        :return: P2WPKH - returns the P2WPKH address object
        """
        return P2WPKH(network, PrivateKey(network, private_key).bech32_address())

    @staticmethod
    def from_script_public_key(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                               scriptPublicKey: str) -> "P2WPKH":
        """
        Generates a P2WPKH address object from the given script private key

        :param network: (required) The network in witch the script public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param scriptPublicKey: (required) script public key
        :type scriptPublicKey: str
        :return: P2WPKH - returns the P2WPKH address object
        """
        return P2WPKH(network, Bech32Address.scriptPublicKey_to_address(network, scriptPublicKey))

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)

    def get_addressType(self) -> str:
        return AddressTypes.P2WPKH

    def get_scriptPublicKey(self) -> str:
        return Script.build_script([OPCodes.OP_0, Bech32Address.decode(self.get_address())])

    def get_redeemScript(self) -> str:
        return Script.build_script([OPCodes.OP_DUP, OPCodes.OP_HASH160, Bech32Address.decode(self.get_address()),
                                    OPCodes.OP_EQUALVERIFY, OPCodes.OP_CHECKSIG])

    def get_bytes_scriptPublicKey(self) -> bytes:
        return bytes.fromhex(self.get_scriptPublicKey())

    def get_bytes_redeemScript(self) -> bytes:
        return bytes.fromhex(self.get_redeemScript())

