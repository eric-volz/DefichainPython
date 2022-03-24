from .rpc import RPC

from .modules.accounts import Accounts
from .modules.blockchain import Blockchain
from .modules.control import Control
from .modules.generating import Generating
from .modules.loan import Loan
from .modules.masternodes import Masternodes
from .modules.mining import Mining
from .modules.network import Network
from .modules.oracles import Oracles
from .modules.poolpair import Poolpair
from .modules.rawtransactions import Rawtransactions
from .modules.spv import Spv
from .modules.tokens import Tokens
from .modules.util import Util
from .modules.vault import Vault
from .modules.wallet import Wallet
from .modules.zmq import Zmq


class Node:
    def __init__(self, url, port, user, password):
        self.url = f"http://{user}:{password}@{url}:{port}"
        self.rpc = RPC(self.url)

        self.accounts = Accounts(self)
        self.blockchain = Blockchain(self)
        self.control = Control(self)
        self.generating = Generating(self)
        self.icxorderbook = None
        self.loan = Loan(self)
        self.masternodes = Masternodes(self)
        self.mining = Mining(self)
        self.network = Network(self)
        self.oracles = Oracles(self)
        self.poolpair = Poolpair(self)
        self.rawtransactions = Rawtransactions(self)
        self.spv = Spv(self)
        self.tokens = Tokens(self)
        self.util = Util(self)
        self.vault = Vault(self)
        self.wallet = Wallet(self)
        self.zmq = Zmq(self)

        self.checkConnection()

    def checkConnection(self):
        if not self.testConnection():
            raise Exception(f"There is no Connection to the Node! \n"
                            f"Check your Config: {self.url}")

    def testConnection(self):
        try:
            self.blockchain.getblockcount()
            return True
        except:
            return False
