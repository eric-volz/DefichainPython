import requests

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

BASE_URL = "https://ocean.defichain.com/"


class Ocean:
    def __init__(self, url="https://ocean.defichain.com", version="v0", network="mainnet"):
        self._attachedURL = url + "/" + version + "/" + network + "/"
        self._test_connection()

        self._conn = Connection(self._attachedURL)

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
            requests.get(self._attachedURL)
            return True
        except Exception as e:
            print(f"No connection could be established to: {self._attachedURL}")
            print(e)

