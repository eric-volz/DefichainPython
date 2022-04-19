from .connection import Connection

from .modules.address import Address
from .modules.oracles import Oracles
from .modules.prices import Prices
from .modules.poolpairs import PoolPairs


BASE_URL = "https://ocean.defichain.com/"


class Ocean:
    def __init__(self, url="https://ocean.defichain.com/", version="v0/", network="mainnet/"):
        self.attachedURL = url + version + network

        self.conn = Connection(self.attachedURL)

        self.address = Address(self)
        #self.blocks   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Blocks.ts
        #self.fee   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Fee.ts
        #self.loan   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Loan.ts
        #self.masternodes   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/MasterNodes.ts
        self.oracles = Oracles(self)
        self.poolpairs = PoolPairs(self) #https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/PoolPairs.ts
        self.prices = Prices(self)
        #self.rawTx   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/RawTx.ts
        #self.rpc   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Rpc.ts
        #self.stats   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Stats.ts
        #self.tokens   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Tokens.ts
        #self.transactions   https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Transactions.ts
