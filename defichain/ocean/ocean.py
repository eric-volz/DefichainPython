import requests
from defichain.logger import Logger
from .connection import Connection

from .modules.address import Address
from .modules.blocks import Blocks
from .modules.fee import Fee
from .modules.loan import Loan
from .modules.masternodes import Masternodes
from .modules.oracles import Oracles
from .modules.poolpairs import Poolpairs
from .modules.prices import Prices
from .modules.rawTx import RawTx
from .modules.rpc import Rpc
from .modules.stats import Stats
from .modules.tokens import Tokens
from .modules.transactions import Transactions


class Ocean:
    """
    This is the main interface to communicate with the ocean protocol.

    If you want to communicate with the standard Ocean, which is also used to operate the Lightwallet,
    then do not change anything in the parameters and create only the Ocean object as in the example.

    :param url: (optional) The main URL where an ocean instance can be reached
    :type url: str
    :param version: (optional) witch version to use with this ocean connection
    :type version: str
    :param network: (optional) witch network to use with this ocean connection
    :type network: str
    :param logger: (optional) Logger Object
    :type logger: :ref:`Logger`
    :return: Ocean (object) The object to interact with the ocean protocol

    :example:

            >>> from defichain import Ocean
            >>> ocaen = Ocean()
            >>> blocks = ocaen.blocks.list()  #  returns the latest 30 blocks
            >>> print(blocks)
    """

    def __init__(self, url: str = "https://ocean.defichain.com", version: str = "v0",
                 network: str = "mainnet", logger: Logger = None) -> "Ocean":

        self._attachedURL = url + "/" + version + "/" + network + "/"
        self._test_connection()

        self._conn = Connection(self._attachedURL, logger)

        self.address = Address(self)
        self.blocks = Blocks(self)
        self.fee = Fee(self)
        self.loan = Loan(self)
        self.masternodes = Masternodes(self)
        self.oracles = Oracles(self)
        self.poolpairs = Poolpairs(self)
        self.prices = Prices(self)
        self.rawTx = RawTx(self)
        self.rpc = Rpc(self)
        self.stats = Stats(self)
        self.tokens = Tokens(self)
        self.transactions = Transactions(self)

    def _test_connection(self):
        try:
            requests.get(self._attachedURL + "stats")
            return True
        except Exception as e:
            print(f"No connection could be established to: {self._attachedURL}")
            print(f"The main URL is called: https://ocean.defichain.com")
            print("If you are not sure how to use the ocean connection correctly, "
                  "go to: https://docs.defichain-python.de/build/html/api/ocean/index.html")

