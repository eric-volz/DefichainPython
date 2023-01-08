from abc import ABC, abstractmethod


class RemoteData(ABC):
    """
    This class contains all abstract methods that has to implement to be usable as a remote data source
    """
    @abstractmethod
    def __init__(self, source: object):
        pass

    @abstractmethod
    def get_unspent(self, address: str) -> [{}]:
        """
        Contains all needed information about the unspent input of an address

        :param address: the address to list the unspent from
        :return: [{txid: ..., index: ..., value: ..., script_type: ..., script: ...}, ...]
        """
        pass

    @abstractmethod
    def test_tx(self, hex: str, maxFeeRate: int = None) -> bool:
        """
        Tests the given raw transaction
        :param hex: raw transaction
        :param maxFeeRate: maximum fee to pay
        :return: bool
        """
        pass

    @abstractmethod
    def send_tx(self, hex: str, maxFeeRate: int = None) -> str:
        """
        Sends the given raw transaction to the blockchain

        :param hex: raw transaction
        :param maxFeeRate: maximum fee to pay
        :return: txid
        """
        pass

