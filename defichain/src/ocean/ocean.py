from .connection import Connection

from .modules.address import Address
from .modules.blocks import Blocks
from .modules.fee import Fee
from .modules.loan import Loan
from .modules.masternodes import Masternodes
from .modules.oracles import Oracles
from .modules.poolpairs import Poolpairs
from .modules.prices import Prices

BASE_URL = "https://ocean.defichain.com/"


class Ocean:
    def __init__(self, url="https://ocean.defichain.com/", version="v0/", network="mainnet/"):
        self._attachedURL = url + version + network

        self._conn = Connection(self._attachedURL)

        self.address = Address(self)
        self.blocks = Blocks(self)
        self.fee = Fee(self)
        self.loan = Loan(self)
        self.masternodes = Masternodes(self)
        self.oracles = Oracles(self)
        self.poolpairs = Poolpairs(self)
        self.prices = Prices(self)
        #self.rawTx   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/RawTx.ts
        #self.rpc   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Rpc.ts
        #self.stats   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Stats.ts
        #self.tokens   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Tokens.ts
        #self.transactions   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Transactions.ts
