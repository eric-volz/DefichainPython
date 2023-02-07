from abc import ABC, abstractmethod

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest


class BaseAddress(ABC):

    @staticmethod
    @abstractmethod
    def from_publicKey(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                       publicKey: str) -> "BaseAddress":
        """
        Generates a specified address object from the given public key

        :param network: (required) The network in witch the public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param publicKey: (required) public key
        :type publicKey: str
        :return: BaseAddress - returns the address object for which the function is applied
        """
        pass

    @staticmethod
    @abstractmethod
    def from_privateKey(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                         privateKey: str) -> "BaseAddress":
        """
        Generates a specified address object from the given private key

        :param network: (required) The network in witch the private key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param privateKey: (required) private key
        :type privateKey: str
        :return: BaseAddress - returns the address object for which the function is applied
        """
        pass

    @staticmethod
    @abstractmethod
    def from_scriptPublicKey(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                             scriptPublicKey: str) -> "BaseAddress":
        """
        Generates a specified address object from the given script private key

        :param network: (required) The network in witch the script public key should be used
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param scriptPublicKey: (required) script public key
        :type scriptPublicKey: str
        :return: BaseAddress - returns the address object for which the function is applied
        """
        pass

    @staticmethod
    @abstractmethod
    def decode(address: str) -> str:
        """
        Decodes an address into hexadecimal.

        P2PKH address: use Base58Address or P2PKH object

        P2SH address: use Base58Address or P2SH object

        P2WPKH address: use Bech32Address or P2WpKH object

        :param address: (required) the address that needs to be decoded
        :type address: str
        :return: "hex" (str) - the decoded address
        """
        pass

    @staticmethod
    @abstractmethod
    def encode(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, scriptPublicKey: str) -> str:
        """
        Encodes a script public key into an address

        P2PKH address: use Base58Address or P2PKH object

        P2SH address: use Base58Address or P2SH object

        P2WPKH address: use Bech32Address or P2WpKH object

        :param network: (required) The network witch the script public key should be encoded for
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param scriptPublicKey: script public key
        :type scriptPublicKey: str
        :return: "hex" (str) - address of the given script public key
        """
        pass

    @staticmethod
    def scriptPublicKey_to_address(network: DefichainMainnet or DefichainTestnet or DefichainRegtest,
                                   scriptPublicKey: str) -> str:
        """
        Converts the given script public key into the corresponding address

        :param network: (required) Network
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        :param scriptPublicKey: (required) script public key
        :type: str
        :return: "address" (str) - corresponding address to the given script public key
        """
        pass

    @staticmethod
    @abstractmethod
    def verify(address: str) -> bool:
        """
        Verify the given address

        :param address: (required) the address that should be validated
        :type address: str
        :return: bool - returns true if address is valid
        """
        pass

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest):
        self._network: DefichainMainnet or DefichainTestnet or DefichainRegtest = None
        self.set_network(network)

    # Get Information
    @abstractmethod
    def get_addressType(self) -> str:
        """
        Gets the address type

        :return: AddressType
        """
        pass

    @abstractmethod
    def get_address(self) -> str:
        """
        Gets the address

        :return: string - the address
        """
        pass

    def get_network(self) -> DefichainMainnet or DefichainTestnet or DefichainRegtest:
        """
        Gets the network

        :return: Network
        """
        return self._network

    @abstractmethod
    def get_scriptPublicKey(self) -> str:
        """
        Calculates the script public key

        :return: string - script public key
        """
        pass

    @abstractmethod
    def get_redeemScript(self) -> str:
        """
        Calculates the redeem script

        :return: string - redeem script
        """
        pass

    @abstractmethod
    def get_bytes_scriptPublicKey(self) -> bytes:
        """
        Calculates the script public key

        :return: bytes - script public key
        """
        pass

    @abstractmethod
    def get_bytes_redeemScript(self) -> bytes:
        """
        Calculates the redeem script

        :return: bytes - redeem script
        """
        pass

    # Set Information

    @abstractmethod
    def set_address(self, address: str) -> None:
        """
        Sets the given new address

        Important: you have to use the correct type of address witch corresponds to the used address object

        :param address: (required) address
        :type address: str
        :return: None
        """
        pass

    def set_network(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest) -> None:
        """
        Sets the given new network

        :param network: (required) Network
        :type network: DefichainMainnet or DefichainTestnet or DefichainRegtest
        """
        self._network = network

    @abstractmethod
    def set_scriptPublicKey(self, scriptPublicKey: str) -> None:
        """
        Sets the script public key

        :param scriptPublicKey: script public key
        :type scriptPublicKey: str
        """
        pass


class UnknownAddress(BaseAddress):
    pass
